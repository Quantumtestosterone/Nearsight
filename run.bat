@echo off
SET DIR=%~dp0
SET VENV_DIR=%DIR%venv

IF NOT EXIST "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
)

call "%VENV_DIR%\Scripts\activate.bat"

echo Installing/Upgrading pip...
python -m pip install --upgrade pip

echo Installing/Upgrading dependencies...
pip install -r "%DIR%requirements.txt"

echo Installing PyQt5...
pip install PyQt5

echo Running the program...
python "%DIR%main.py"

pause