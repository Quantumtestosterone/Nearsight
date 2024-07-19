import sys
import base64
import io
import time
from openai import OpenAI
import pyautogui
from dotenv import load_dotenv
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, 
                             QWidget, QLabel, QLineEdit, QGroupBox, QGridLayout, QScrollArea, QRubberBand, QComboBox)
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal, QRect, QPoint
from PyQt5.QtGui import QPixmap, QImage, QColor, QPainter, QPen
from PIL import Image, ImageDraw, ImageFont

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

class ScreenshotArea(QWidget):
    """Widget for selecting a custom screenshot area"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 512, 512)  # Initial size
        self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
        self.rubberband.setGeometry(self.rect())
        self.rubberband.show()

    def paintEvent(self, event):
        """Draw border around the screenshot area"""
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        """Handle mouse press for moving the area"""
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        """Handle mouse move for moving the area"""
        if event.buttons() == Qt.LeftButton:
            self.move(self.mapToParent(event.pos() - self.offset))

    def resize_area(self, size):
        """Resize the screenshot area"""
        self.setGeometry(self.x(), self.y(), size[0], size[1])
        self.rubberband.setGeometry(self.rect())

class MainWindow(QMainWindow):
    """Main application window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Analyzer")
        self.setGeometry(100, 100, 1200, 800)

        main_layout = QHBoxLayout()

        # Left side (controls and input)
        left_layout = QVBoxLayout()

        # System prompt
        system_prompt_group = QGroupBox("System Prompt")
        system_prompt_layout = QVBoxLayout()
        self.system_prompt_input = QTextEdit()
        self.system_prompt_input.setPlaceholderText("Enter system prompt here...")
        self.system_prompt_input.setText("You are an AI assistant capable of analyzing both text messages and images. When an image is provided, you can see and describe it. Always consider the context of previous messages and images in your responses.")
        system_prompt_layout.addWidget(self.system_prompt_input)
        system_prompt_group.setLayout(system_prompt_layout)
        left_layout.addWidget(system_prompt_group)

        # Control buttons
        control_group = QGroupBox("Control")
        control_layout = QGridLayout()
        self.auto_button = QPushButton("Auto")
        self.auto_button.clicked.connect(self.toggle_auto_mode)
        self.show_screen_button = QPushButton("Show Screen: Off")
        self.show_screen_button.clicked.connect(self.toggle_show_screen)
        self.send_message_button = QPushButton("Send Message")
        self.send_message_button.clicked.connect(self.send_message)
        self.clear_history_button = QPushButton("Clear History")
        self.clear_history_button.clicked.connect(self.clear_history)
        self.toggle_screenshot_area_button = QPushButton("Toggle Screenshot Area")
        self.toggle_screenshot_area_button.clicked.connect(self.toggle_screenshot_area)
        self.screenshot_size_combo = QComboBox()
        self.screenshot_size_combo.addItems(["Low (512x512)", "Medium (768x768)", "High (1024x1024)"])
        self.screenshot_size_combo.currentIndexChanged.connect(self.change_screenshot_size)
        
        # Model selection
        self.model_combo = QComboBox()
        self.model_combo.addItems(["gpt-4o-mini", "gpt-4-turbo", "gpt-4o"])
        
        control_layout.addWidget(self.auto_button, 0, 0)
        control_layout.addWidget(self.show_screen_button, 0, 1)
        control_layout.addWidget(self.send_message_button, 1, 0)
        control_layout.addWidget(self.clear_history_button, 1, 1)
        control_layout.addWidget(self.toggle_screenshot_area_button, 2, 0)
        control_layout.addWidget(self.screenshot_size_combo, 2, 1)
        control_layout.addWidget(QLabel("Model:"), 3, 0)
        control_layout.addWidget(self.model_combo, 3, 1)
        control_group.setLayout(control_layout)
        left_layout.addWidget(control_group)

        # Message input
        message_group = QGroupBox("Message")
        message_layout = QVBoxLayout()
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Enter your message here...")
        message_layout.addWidget(self.message_input)
        message_group.setLayout(message_layout)
        left_layout.addWidget(message_group)

        main_layout.addLayout(left_layout, 1)

        # Right side (output and image)
        right_layout = QVBoxLayout()

        # Output text
        output_group = QGroupBox("Analysis Output")
        output_layout = QVBoxLayout()
        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)
        output_layout.addWidget(self.text_output)
        output_group.setLayout(output_layout)
        right_layout.addWidget(output_group, 2)

        # Image display
        image_group = QGroupBox("Last Screenshot")
        image_layout = QVBoxLayout()
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        image_scroll = QScrollArea()
        image_scroll.setWidget(self.image_label)
        image_scroll.setWidgetResizable(True)
        image_layout.addWidget(image_scroll)
        image_group.setLayout(image_layout)
        right_layout.addWidget(image_group, 1)

        main_layout.addLayout(right_layout, 2)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.timer = QTimer()
        self.timer.timeout.connect(self.run_analysis)
        self.auto_mode = False
        self.show_screen = False

        self.analysis_thread = None
        self.conversation_history = []

        self.screenshot_area = ScreenshotArea()
        self.screenshot_area.hide()

    def toggle_auto_mode(self):
        """Toggle automatic analysis mode"""
        self.auto_mode = not self.auto_mode
        if self.auto_mode:
            self.auto_button.setText("Stop Auto")
            self.run_analysis()
        else:
            self.auto_button.setText("Auto")
            self.timer.stop()

    def toggle_show_screen(self):
        """Toggle screen display"""
        self.show_screen = not self.show_screen
        self.show_screen_button.setText(f"Show Screen: {'On' if self.show_screen else 'Off'}")
        if self.show_screen:
            self.display_image(self.capture_screenshot())

    def toggle_screenshot_area(self):
        """Toggle visibility of custom screenshot area"""
        if self.screenshot_area.isVisible():
            self.screenshot_area.hide()
        else:
            self.screenshot_area.show()

    def change_screenshot_size(self, index):
        """Change size of custom screenshot area"""
        sizes = [(512, 512), (768, 768), (1024, 1024)]
        self.screenshot_area.resize_area(sizes[index])

    def send_message(self):
        """Send a message for analysis"""
        message = self.message_input.toPlainText()
        screenshot = self.capture_screenshot() if self.show_screen else self.create_blank_image()
        if message or self.show_screen:
            self.run_analysis(screenshot, message)
            self.message_input.clear()  # Clear the message input after sending

    def run_analysis(self, screenshot=None, message=None):
        """Run the AI analysis"""
        if self.analysis_thread and self.analysis_thread.isRunning():
            return  # Don't start a new analysis if one is already running

        if screenshot is None:
            screenshot = self.capture_screenshot()
        else:
            self.display_image(screenshot)

        system_prompt = self.system_prompt_input.toPlainText()
        
        # Add user message to conversation history
        user_content = []
        if message:
            user_content.append({"type": "text", "text": message})
        user_content.append({
            "type": "image_url", 
            "image_url": {
                "url": f"data:image/png;base64,{self.image_to_base64(screenshot)}",
                "detail": "low"
            }
        })
        
        self.conversation_history.append({"role": "user", "content": user_content})
        self.text_output.append(f'<span style="color: red; font-weight: bold;">User:</span> {message if message else "[No message]"}<br>[Image attached]<br><br>')

        # Get selected model
        selected_model = self.model_combo.currentText()

        self.analysis_thread = AnalysisThread(screenshot, message, system_prompt, self.conversation_history, selected_model)
        self.analysis_thread.analysis_complete.connect(self.handle_analysis_result)
        self.analysis_thread.start()

    def handle_analysis_result(self, analysis, screenshot_time, analysis_time, total_time):
        """Handle the result of the AI analysis"""
        output = f'<span style="color: blue; font-weight: bold;">Assistant:</span> {analysis}<br><br>'
        if screenshot_time > 0:
            output += f"Screenshot capture time: {screenshot_time:.2f} ms<br>"
        output += f"Analysis time: {analysis_time:.2f} ms<br>"
        output += f"Total time: {total_time:.2f} ms<br><br>"
        output += "-" * 50 + "<br><br>"

        self.text_output.append(output)

        # Update conversation history with assistant's response
        self.conversation_history.append({"role": "assistant", "content": analysis})

        # Limit conversation history to last 10 exchanges (20 messages)
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]

        if self.auto_mode:
            self.timer.start(100)  # Small delay before next analysis

    def capture_screenshot(self):
        """Capture a screenshot"""
        if self.screenshot_area.isVisible():
            screenshot = pyautogui.screenshot(region=(
                self.screenshot_area.x(),
                self.screenshot_area.y(),
                self.screenshot_area.width(),
                self.screenshot_area.height()
            ))
        else:
            screenshot = pyautogui.screenshot()
        
        # Resize to 512x512 for API
        screenshot = screenshot.resize((512, 512), Image.LANCZOS)

        # Add coordinate overlay
        draw = ImageDraw.Draw(screenshot)
        font = ImageFont.truetype("arial.ttf", 12)
        draw.text((5, 5), f"Size: {screenshot.width}x{screenshot.height}", fill="red", font=font)

        return screenshot

    def create_blank_image(self):
        """Create a blank image"""
        return Image.new('RGB', (512, 512), color='white')

    def image_to_base64(self, image):
        """Convert image to base64 string"""
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8')

    def display_image(self, image):
        """Display the image in the UI"""
        qimage = QImage(image.tobytes(), image.width, image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        self.text_output.clear()
        self.text_output.append("Conversation history cleared.<br>")

class AnalysisThread(QThread):
    """Thread for running AI analysis"""
    analysis_complete = pyqtSignal(str, float, float, float)

    def __init__(self, screenshot, message, system_prompt, conversation_history, model):
        super().__init__()
        self.screenshot = screenshot
        self.message = message
        self.system_prompt = system_prompt
        self.conversation_history = conversation_history
        self.model = model

    def run(self):
        """Run the AI analysis"""
        start_time = time.perf_counter()
        
        messages = [
            {"role": "system", "content": self.system_prompt},
        ] + self.conversation_history

        analysis_start = time.perf_counter()

        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=300,
        )
        analysis = response.choices[0].message.content

        end_time = time.perf_counter()

        screenshot_time = (analysis_start - start_time) * 1000
        analysis_time = (end_time - analysis_start) * 1000
        total_time = (end_time - start_time) * 1000

        self.analysis_complete.emit(analysis, screenshot_time, analysis_time, total_time)

def main():
    """Main function to run the application"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()