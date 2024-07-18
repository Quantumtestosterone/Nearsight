Developer quickstart
Get up and running with the OpenAI API
The OpenAI API provides a simple interface for developers to create an intelligence layer in their applications, powered by OpenAI's state of the art models. The Chat Completions endpoint powers ChatGPT and provides a simple way to take text as input and use a model like GPT-4o to generate an output.

Want to jump straight to the code?
Skip the quickstart and dive into the API reference.

This quickstart is designed to help get your local development environment set up and send your first API request. If you are an experienced developer or want to just dive into using the OpenAI API, the API reference of GPT guide are a great place to start. Throughout this quickstart, you will learn:

How to set up your development environment
How to install the latest SDKs
Some of the basic concepts of the OpenAI API
How to send your first API request
If you run into any challenges or have questions getting started, please join our developer forum.

Account setup
First, create an OpenAI account or sign in. Next, navigate to the API key page and "Create new secret key", optionally naming the key. Make sure to save this somewhere safe and do not share it with anyone.

Quickstart language selection
Select the tool or language you want to get started using the OpenAI API with.

Python is a popular programming language that is commonly used for data applications, web development, and many other programming tasks due to its ease of use. OpenAI provides a custom Python library which makes working with the OpenAI API in Python simple and efficient.

Step 1: Setting up Python
Install Python
To use the OpenAI Python library, you will need to ensure you have Python installed. Some computers come with Python pre-installed while others require that you set it up yourself. To test if you have Python installed, you can navigate to your Terminal or Command line:

MacOS: Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
Windows: Open Command Prompt: You can find it by searching "cmd" in the start menu.
Next, enter the word python and then press return/enter. If you enter into the Python interpreter, then you have Python installed on your computer already and you can go to the next step. If you get an error message that says something like "Error: command python not found", you likely need to install Python and make it available in your terminal / command line.

To download Python, head to the official Python website and download the latest version. To use the OpenAI Python library, you need at least Python 3.7.1 or newer. If you are installing Python for the first time, you can follow the official Python installation guide for beginners.

Set up a virtual environment (optional)
Once you have Python installed, it is a good practice to create a virtual python environment to install the OpenAI Python library. Virtual environments provide a clean working space for your Python packages to be installed so that you do not have conflicts with other libraries you install for other projects. You are not required to use a virtual environment, so skip to step 3 if you do not want to set one up.

To create a virtual environment, Python supplies a built in venv module which provides the basic functionality needed for the virtual environment. Running the command below will create a virtual environment named "openai-env" inside the current folder you have selected in your terminal / command line:

python -m venv openai-env
Once you’ve created the virtual environment, you need to activate it. On Windows, run:

openai-env\Scripts\activate
On Unix or MacOS, run:

source openai-env/bin/activate
You should see the terminal / command line interface change slightly after you active the virtual environment, it should now show "openai-env" to the left of the cursor input section. For more details on working wit virtual environments, please refer to the official Python documentation.

Install the OpenAI Python library
Once you have Python 3.7.1 or newer installed and (optionally) set up a virtual environment, the OpenAI Python library can be installed. From the terminal / command line, run:

pip install --upgrade openai
Once this completes, running pip list will show you the Python libraries you have installed in your current environment, which should confirm that the OpenAI Python library was successfully installed.

Step 2: Set up your API key
Set up your API key for all projects (recommended)
The main advantage to making your API key accessible for all projects is that the Python library will automatically detect it and use it without having to write any code.

MacOS
Windows
Open Command Prompt: You can find it by searching "cmd" in the start menu.

Set environment variable in the current session: To set the environment variable in the current session, use the command below, replacing your-api-key-here with your actual API key:

setx OPENAI_API_KEY "your-api-key-here"
This command will set the OPENAI_API_KEY environment variable for the current session.

Permanent setup: To make the setup permanent, add the variable through the system properties as follows:

Right-click on 'This PC' or 'My Computer' and select 'Properties'.
Click on 'Advanced system settings'.
Click the 'Environment Variables' button.
In the 'System variables' section, click 'New...' and enter OPENAI_API_KEY as the variable name and your API key as the variable value.
Verification: To verify the setup, reopen the command prompt and type the command below. It should display your API key: echo %OPENAI_API_KEY%

Set up your API key for a single project
If you only want your API key to be accessible to a single project, you can create a local .env file which contains the API key and then explicitly use that API key with the Python code shown in the steps to come.

Start by going to the project folder you want to create the .env file in.

In order for your .env file to be ignored by version control, create a .gitignore file in the root of your project directory. Add a line with .env on it which will make sure your API key or other secrets are not accidentally shared via version control.

Once you create the .gitignore and .env files using the terminal or an integrated development environment (IDE), copy your secret API key and set it as the OPENAI_API_KEY in your .env file. If you haven't created a secret key yet, you can do so on the API key page.

The .env file should look like the following:

# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

OPENAI_API_KEY=abc123
The API key can be imported by running the code below:

from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )
Step 3: Sending your first API request
Making an API request
After you have Python configured and set up an API key, the final step is to send a request to the OpenAI API using the Python library. To do this, create a file named openai-test.py using th terminal or an IDE.

Inside the file, copy and paste one of the examples below:

ChatCompletions

ChatCompletions
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
To run the code, enter python openai-test.py into the terminal / command line.

The Chat Completions example highlights just one area of strength for our models: creative ability. Explaining recursion (the programming topic) in a well formatted poem is something both the best developers and best poets would struggle with. In this case, gpt-4o-mini does it effortlessly.

Next steps
Now that you have made you first OpenAI API request, you can explore the following resources:

For more detailed information on our core Chat Completions API, see our Chat Completions guide
Visit the OpenAI Cookbook for in-depth example API use-cases, as well as code snippets for common tasks
Want some inspiration to prompt our models? Check out our library of example prompts
Want to try the API without writing any code? Start experimenting in the Playground
Keep our usage policies in mind as you start building
Explore our other endpoints


Key Concepts
At OpenAI, protecting user data is fundamental to our mission. We do not train our models on inputs and outputs through our API. Learn more on our API data privacy page.

Text generation models
OpenAI's text generation models (often referred to as generative pre-trained transformers or "GPT" models for short), like GPT-4 and GPT-3.5, have been trained to understand natural and formal language. Models like GPT-4 allows text outputs in response to their inputs. The inputs to these models are also referred to as "prompts". Designing a prompt is essentially how you "program" a model like GPT-4, usually by providing instructions or some examples of how to successfully complete a task. Models like GPT-4 can be used across a great variety of tasks including content or code generation, summarization, conversation, creative writing, and more. Read more in our introductory text generation guide and in our prompt engineering guide.

Assistants
Assistants refer to entities, which in the case of the OpenAI API are powered by large language models like GPT-4, that are capable of performing tasks for users. These assistants operate based on the instructions embedded within the context window of the model. They also usually have access to tools which allows the assistants to perform more complex tasks like running code or retrieving information from a file. Read more about assistants in our Assistants API Overview.

Embeddings
An embedding is a vector representation of a piece of data (e.g. some text) that is meant to preserve aspects of its content and/or its meaning. Chunks of data that are similar in some way will tend to have embeddings that are closer together than unrelated data. OpenAI offers text embedding models that take as input a text string and produce as output an embedding vector. Embeddings are useful for search, clustering, recommendations, anomaly detection, classification, and more. Read more about embeddings in our embeddings guide.

Tokens
Text generation and embeddings models process text in chunks called tokens. Tokens represent commonly occurring sequences of characters. For example, the string " tokenization" is decomposed as " token" and "ization", while a short and common word like " the" is represented as a single token. Note that in a sentence, the first token of each word typically starts with a space character. Check out our tokenizer tool to test specific strings and see how they are translated into tokens. As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text.

One limitation to keep in mind is that for a text generation model the prompt and the generated output combined must be no more than the model's maximum context length. For embeddings models (which do not output tokens), the input must be shorter than the model's maximum context length. The maximum context lengths for each text generation and embeddings model can be found in the model index.


Models
Flagship models
GPT-4o
Our high-intelligence flagship model for complex, multi‑step tasks

 Text and image input, text output
 128k context length
 Input: $5 | Output: $15*
GPT-4o mini New
Our affordable and intelligent small model for fast, lightweight tasks

 Text and image input, text output
 128k context length
 Input: $0.15 | Output: $0.60*
* prices per 1 million tokens

Models overview
The OpenAI API is powered by a diverse set of models with different capabilities and price points. You can also make customizations to our models for your specific use case with fine-tuning.

MODEL	DESCRIPTION
GPT-4o	Our high-intelligence flagship model for complex, multi-step tasks
GPT-4o mini	Our affordable and intelligent small model for fast, lightweight tasks
GPT-4 Turbo and GPT-4	The previous set of high-intelligence models
GPT-3.5 Turbo	A fast, inexpensive model for simple tasks
DALL·E	A model that can generate and edit images given a natural language prompt
TTS	A set of models that can convert text into natural sounding spoken audio
Whisper	A model that can convert audio into text
Embeddings	A set of models that can convert text into a numerical form
Moderation	A fine-tuned model that can detect whether text may be sensitive or unsafe
GPT base	A set of models without instruction following that can understand as well as generate natural language or code
Deprecated	A full list of models that have been deprecated along with the suggested replacement
We have also published open source models including Point-E, Whisper, Jukebox, and CLIP.

Continuous model upgrades
gpt-4o, gpt-4o-mini, gpt-4-turbo, gpt-4, and gpt-3.5-turbo point to their respective latest model version. You can verify this by looking at the response object after sending a request. The response will include the specific model version used (e.g. gpt-3.5-turbo-1106).

We also offer pinned model versions that developers can continue using for at least three months after an updated model has been introduced. With the new cadence of model updates, we are also giving people the ability to contribute evals to help us improve the model for different use cases. If you are interested, check out the OpenAI Evals repository.

Learn more about model deprecation on our deprecation page.

GPT-4o
GPT-4o (“o” for “omni”) is our most advanced model. It is multimodal (accepting text or image inputs and outputting text), and it has the same high intelligence as GPT-4 Turbo but is much more efficient—it generates text 2x faster and is 50% cheaper. Additionally, GPT-4o has the best vision and performance across non-English languages of any of our models. GPT-4o is available in the OpenAI API to paying customers. Learn how to use GPT-4o in our text generation guide.

MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-4o	GPT-4o
Our high-intelligence flagship model for complex, multi-step tasks. GPT-4o is cheaper and faster than GPT-4 Turbo. Currently points to gpt-4o-2024-05-13.	128,000 tokens	Up to Oct 2023
gpt-4o-2024-05-13	gpt-4o currently points to this version.	128,000 tokens	Up to Oct 2023
GPT-4o mini
GPT-4o mini (“o” for “omni”) is our most advanced model in the small models category, and our cheapest model yet. It is multimodal (accepting text or image inputs and outputting text), has higher intelligence than gpt-3.5-turbo but is just as fast. It is meant to be used for smaller tasks, including vision tasks.

We recommend choosing gpt-4o-mini where you would have previously used gpt-3.5-turbo as this model is more capable and cheaper.

MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-4o-mini	New GPT-4o-mini
Our affordable and intelligent small model for fast, lightweight tasks. GPT-4o mini is cheaper and more capable than GPT-3.5 Turbo. Currently points to gpt-4o-mini-2024-07-18.	128,000 tokens	Up to Oct 2023
gpt-4o-mini-2024-07-18	gpt-4o-mini currently points to this version.	128,000 tokens	Up to Oct 2023
GPT-4 Turbo and GPT-4
GPT-4 is a large multimodal model (accepting text or image inputs and outputting text) that can solve difficult problems with greater accuracy than any of our previous models, thanks to its broader general knowledge and advanced reasoning capabilities. GPT-4 is available in the OpenAI API to paying customers. Like gpt-3.5-turbo, GPT-4 is optimized for chat but works well for traditional completions tasks using the Chat Completions API. Learn how to use GPT-4 in our text generation guide.

MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-4-turbo	The latest GPT-4 Turbo model with vision capabilities. Vision requests can now use JSON mode and function calling. Currently points to gpt-4-turbo-2024-04-09.	128,000 tokens	Up to Dec 2023
gpt-4-turbo-2024-04-09	GPT-4 Turbo with Vision model. Vision requests can now use JSON mode and function calling. gpt-4-turbo currently points to this version.	128,000 tokens	Up to Dec 2023
gpt-4-turbo-preview	GPT-4 Turbo preview model. Currently points to gpt-4-0125-preview.	128,000 tokens	Up to Dec 2023
gpt-4-0125-preview	GPT-4 Turbo preview model intended to reduce cases of “laziness” where the model doesn’t complete a task. Returns a maximum of 4,096 output tokens. Learn more.	128,000 tokens	Up to Dec 2023
gpt-4-1106-preview	GPT-4 Turbo preview model featuring improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. This is a preview model. Learn more.	128,000 tokens	Up to Apr 2023
gpt-4	Currently points to gpt-4-0613. See continuous model upgrades.	8,192 tokens	Up to Sep 2021
gpt-4-0613	Snapshot of gpt-4 from June 13th 2023 with improved function calling support.	8,192 tokens	Up to Sep 2021
gpt-4-0314	Legacy Snapshot of gpt-4 from March 14th 2023.	8,192 tokens	Up to Sep 2021
For many basic tasks, the difference between GPT-4 and GPT-3.5 models is not significant. However, in more complex reasoning situations, GPT-4 is much more capable than any of our previous models.

Multilingual capabilities
GPT-4 outperforms both previous large language models and as of 2023, most state-of-the-art systems (which often have benchmark-specific training or hand-engineering). On the MMLU benchmark, an English-language suite of multiple-choice questions covering 57 subjects, GPT-4 not only outperforms existing models by a considerable margin in English, but also demonstrates strong performance in other languages.

GPT-3.5 Turbo
GPT-3.5 Turbo models can understand and generate natural language or code and have been optimized for chat using the Chat Completions API but work well for non-chat tasks as well.

As of July 2024, gpt-4o-mini should be used in place of gpt-3.5-turbo, as it is cheaper, more capable, multimodal, and just as fast. gpt-3.5-turbo is still available for use in the API.

MODEL	DESCRIPTION	CONTEXT WINDOW	TRAINING DATA
gpt-3.5-turbo-0125	The latest GPT-3.5 Turbo model with higher accuracy at responding in requested formats and a fix for a bug which caused a text encoding issue for non-English language function calls. Returns a maximum of 4,096 output tokens. Learn more.	16,385 tokens	Up to Sep 2021
gpt-3.5-turbo	Currently points to gpt-3.5-turbo-0125.	16,385 tokens	Up to Sep 2021
gpt-3.5-turbo-1106	GPT-3.5 Turbo model with improved instruction following, JSON mode, reproducible outputs, parallel function calling, and more. Returns a maximum of 4,096 output tokens. Learn more.	16,385 tokens	Up to Sep 2021
gpt-3.5-turbo-instruct	Similar capabilities as GPT-3 era models. Compatible with legacy Completions endpoint and not Chat Completions.	4,096 tokens	Up to Sep 2021
DALL·E
DALL·E is a AI system that can create realistic images and art from a description in natural language. DALL·E 3 currently supports the ability, given a prompt, to create a new image with a specific size. DALL·E 2 also support the ability to edit an existing image, or create variations of a user provided image.

DALL·E 3 is available through our Images API along with DALL·E 2. You can try DALL·E 3 through ChatGPT Plus.

MODEL	DESCRIPTION
dall-e-3	The latest DALL·E model released in Nov 2023. Learn more.
dall-e-2	The previous DALL·E model released in Nov 2022. The 2nd iteration of DALL·E with more realistic, accurate, and 4x greater resolution images than the original model.
TTS
TTS is an AI model that converts text to natural sounding spoken text. We offer two different model variates, tts-1 is optimized for real time text to speech use cases and tts-1-hd is optimized for quality. These models can be used with the Speech endpoint in the Audio API.

MODEL	DESCRIPTION
tts-1	The latest text to speech model, optimized for speed.
tts-1-hd	The latest text to speech model, optimized for quality.
Whisper
Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a multi-task model that can perform multilingual speech recognition as well as speech translation and language identification. The Whisper v2-large model is currently available through our API with the whisper-1 model name.

Currently, there is no difference between the open source version of Whisper and the version available through our API. However, through our API, we offer an optimized inference process which makes running Whisper through our API much faster than doing it through other means. For more technical details on Whisper, you can read the paper.

Embeddings
Embeddings are a numerical representation of text that can be used to measure the relatedness between two pieces of text. Embeddings are useful for search, clustering, recommendations, anomaly detection, and classification tasks. You can read more about our latest embedding models in the announcement blog post.

MODEL	DESCRIPTION	OUTPUT DIMENSION
text-embedding-3-large	Most capable embedding model for both english and non-english tasks	3,072
text-embedding-3-small	Increased performance over 2nd generation ada embedding model	1,536
text-embedding-ada-002	Most capable 2nd generation embedding model, replacing 16 first generation models	1,536
Moderation
The Moderation models are designed to check whether content complies with OpenAI's usage policies. The models provide classification capabilities that look for content in the following categories: hate, hate/threatening, self-harm, sexual, sexual/minors, violence, and violence/graphic. You can find out more in our moderation guide.

Moderation models take in an arbitrary sized input that is automatically broken up into chunks of 4,096 tokens. In cases where the input is more than 32,768 tokens, truncation is used which in a rare condition may omit a small number of tokens from the moderation check.

The final results from each request to the moderation endpoint shows the maximum value on a per category basis. For example, if one chunk of 4K tokens had a category score of 0.9901 and the other had a score of 0.1901, the results would show 0.9901 in the API response since it is higher.

MODEL	DESCRIPTION	MAX TOKENS
text-moderation-latest	Currently points to text-moderation-007.	32,768
text-moderation-stable	Currently points to text-moderation-007.	32,768
text-moderation-007	Most capable moderation model across all categories.	32,768
GPT base
GPT base models can understand and generate natural language or code but are not trained with instruction following. These models are made to be replacements for our original GPT-3 base models and use the legacy Completions API. Most customers should use GPT-3.5 or GPT-4.

MODEL	DESCRIPTION	MAX TOKENS	TRAINING DATA
babbage-002	Replacement for the GPT-3 ada and babbage base models.	16,384 tokens	Up to Sep 2021
davinci-002	Replacement for the GPT-3 curie and davinci base models.	16,384 tokens	Up to Sep 2021
How we use your data
Your data is your data.

As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly opt in). One advantage to opting in is that the models may get better at your use case over time.

To help identify abuse, API data may be retained for up to 30 days, after which it will be deleted (unless otherwise required by law). For trusted customers with sensitive applications, zero data retention may be available. With zero data retention, request and response bodies are not persisted to any logging mechanism and exist only in memory in order to serve the request.

Note that this data policy does not apply to OpenAI's non-API consumer services like ChatGPT or DALL·E Labs.

Default usage policies by endpoint
ENDPOINT	DATA USED FOR TRAINING	DEFAULT RETENTION	ELIGIBLE FOR ZERO RETENTION
/v1/chat/completions*	No	30 days	Yes, except image inputs*
/v1/assistants	No	30 days **	No
/v1/threads	No	30 days **	No
/v1/threads/messages	No	30 days **	No
/v1/threads/runs	No	30 days **	No
/v1/vector_stores	No	30 days **	No
/v1/threads/runs/steps	No	30 days **	No
/v1/images/generations	No	30 days	No
/v1/images/edits	No	30 days	No
/v1/images/variations	No	30 days	No
/v1/embeddings	No	30 days	Yes
/v1/audio/transcriptions	No	Zero data retention	-
/v1/audio/translations	No	Zero data retention	-
/v1/audio/speech	No	30 days	Yes
/v1/files	No	Until deleted by customer	No
/v1/fine_tuning/jobs	No	Until deleted by customer	No
/v1/batches	No	Until deleted by customer	No
/v1/moderations	No	Zero data retention	-
/v1/completions	No	30 days	Yes
* Image inputs via the gpt-4-turbo model (or previously gpt-4-vision-preview) are not eligible for zero retention.

** Objects related to the Assistants API are deleted from our servers 30 days after you delete them via the API or the dashboard. Objects that are not deleted via the API or dashboard are retained indefinitely.

For details, see our API data usage policies. To learn more about zero retention, get in touch with our sales team.

Model endpoint compatibility
ENDPOINT	LATEST MODELS
/v1/assistants	All GPT-4 and GPT-3.5 Turbo models. The retrieval tool requires gpt-4-turbo-preview (and subsequent dated model releases) or gpt-3.5-turbo-1106 (and subsequent versions).
/v1/audio/transcriptions	whisper-1
/v1/audio/translations	whisper-1
/v1/audio/speech	tts-1, tts-1-hd
/v1/chat/completions	gpt-4 and dated model releases, gpt-4-turbo-preview and dated model releases, gpt-3.5-turbo and dated model releases, fine-tuned versions of gpt-3.5-turbo
/v1/completions (Legacy)	gpt-3.5-turbo-instruct, babbage-002, davinci-002
/v1/embeddings	text-embedding-3-small, text-embedding-3-large, text-embedding-ada-002
/v1/fine_tuning/jobs	gpt-3.5-turbo, babbage-002, davinci-002
/v1/moderations	text-moderation-stable, text-moderation-latest
/v1/images/generations	dall-e-2, dall-e-3


Libraries
Python library
We provide a Python library, which you can install by running:

pip install openai
Once installed, you can use the library and your secret key to run the following:

from openai import OpenAI
client = OpenAI(
    # Defaults to os.environ.get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello world"}]
)
The bindings also will install a command-line utility you can use as follows:

$ openai api chat_completions.create -m gpt-4o-mini -g user "Hello world"
TypeScript / JavaScript library

We provide a TypeScript / JavaScript library with support for Node.js and various other runtimes. Install it by running:

npm install --save openai
# or
yarn add openai
Once installed, you can use the library and your secret key to run the following:

import OpenAI from "openai";

const openai = new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
});

const chatCompletion = await openai.chat.completions.create({
    messages: [{ role: "user", content: "Say this is a test" }],
    model: "gpt-4o-mini",
});
.NET library Beta
We provide a .NET library, which you can install by running:

dotnet add package OpenAI --prerelease
Once installed, you can use the library and your secret key to run the following:

using OpenAI.Chat;

ChatClient client = new("gpt-4o-mini", Environment.GetEnvironmentVariable("OPENAI_API_KEY"));

ChatCompletion chatCompletion = client.CompleteChat(
    [
        new UserChatMessage("Say 'this is a test.'"),
    ]);
Azure OpenAI libraries
Microsoft's Azure team maintains libraries that are compatible with both the OpenAI API and Azure OpenAI services. Read the library documentation below to learn how you can use them with the OpenAI API.

Azure OpenAI client library for .NET
Azure OpenAI client library for JavaScript
Azure OpenAI client library for Java
Azure OpenAI client library for Go
Community libraries
The libraries below are built and maintained by the broader developer community. If you'd like to add a new library here, please follow the instructions in our help center article on adding community libraries. You can also watch our OpenAPI specification repository on GitHub to get timely updates on when we make changes to our API.

Please note that OpenAI does not verify the correctness or security of these projects. Use them at your own risk!

C# / .NET
Betalgo.OpenAI by Betalgo
OpenAI-API-dotnet by OkGoDoIt
OpenAI-DotNet by RageAgainstThePixel
C++
liboai by D7EAD
Clojure
openai-clojure by wkok
Crystal
openai-crystal by sferik
Dart/Flutter
openai by anasfik
Delphi
DelphiOpenAI by HemulGM
Elixir
openai.ex by mgallo
Go
go-gpt3 by sashabaranov
Java
openai-java by Theo Kanning
Julia
OpenAI.jl by rory-linehan
Kotlin
openai-kotlin by Mouaad Aallam
Node.js
openai-api by Njerschow
openai-api-node by erlapso
gpt-x by ceifa
gpt3 by poteat
gpts by thencc
@dalenguyen/openai by dalenguyen
tectalic/openai by tectalic
PHP
orhanerday/open-ai by orhanerday
tectalic/openai by tectalic
openai-php client by openai-php
Python
chronology by OthersideAI
R
rgpt3 by ben-aaron188
Ruby
openai by nileshtrivedi
ruby-openai by alexrudall
Rust
async-openai by 64bit
fieri by lbkolev
Scala
openai-scala-client by cequence-io
Swift
OpenAIKit by dylanshine
OpenAI by MacPaw
Unity
OpenAi-Api-Unity by hexthedev
com.openai.unity by RageAgainstThePixel
Unreal Engine
OpenAI-Api-Unreal by KellanM

Text generation models
OpenAI's text generation models (often called generative pre-trained transformers or large language models) have been trained to understand natural language, code, and images. The models provide text outputs in response to their inputs. The text inputs to these models are also referred to as "prompts". Designing a prompt is essentially how you “program” a large language model model, usually by providing instructions or some examples of how to successfully complete a task.

Using OpenAI's text generation models, you can build applications to:

Draft documents
Write computer code
Answer questions about a knowledge base
Analyze texts
Give software a natural language interface
Tutor in a range of subjects
Translate languages
Simulate characters for games
Prompt examples
Explore prompt examples for inspiration

To use one of these models via the OpenAI API, you’ll send a request to the Chat Completions API containing the inputs and your API key, and receive a response containing the model’s output.

You can experiment with various models in the chat playground. If you’re not sure which model to use then try gpt-4o if you need high intelligence or gpt-4o-mini if you need the fastest speed and lowest cost.

Quickstart
Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it's just as useful for single-turn tasks without any conversation.

An example Chat Completions API call looks like the following:

python

python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a LLM?"}
  ]
)
To learn more, you can view the Chat Completions guide.

Prompt engineering
An awareness of the best practices for working with OpenAI models can make a significant difference in application performance. The failure modes that each exhibit and the ways of working around or correcting those failure modes are not always intuitive. There is an entire field related to working with language models which has come to be known as "prompt engineering", but as the field has progressed its scope has outgrown merely engineering the prompt into engineering systems that use model queries as components.

To learn more, read our guide on prompt engineering which covers methods to improve model reasoning, reduce the likelihood of model hallucinations, and more.

You can also find many useful resources including code samples in the OpenAI Cookbook.

FAQ
Which model should I use?
We generally recommend that you default to using either gpt-4o or gpt-4o-mini.

If your use case requires high intelligence or reasoning about images as well as text, we recommend you evaluate both gpt-4o and gpt-4-turbo (although they have very similar intelligence, note that gpt-4o is both faster and cheaper).

If your use case requires the fastest speed and lowest cost, we recommend gpt-4o-mini since it is optimized for these aspects.

We recommend using gpt-4o-mini where you would have previously used gpt-3.5-turbo as it is cheaper with higher intelligence, has a larger context window (up to 128,000 tokens compared to 4,096 tokens for gpt-3.5-turbo), and is multimodal.

You can experiment in the playground to investigate which models provide the best price performance trade-off for your usage. A common design pattern is to use several distinct query types which are each dispatched to the model appropriate to handle them.

How should I set the temperature parameter?
Lower values for temperature result in more consistent outputs (e.g. 0.2), while higher values generate more diverse and creative results (e.g. 1.0). Select a temperature value based on the desired trade-off between coherence and creativity for your specific application. The temperature can range is from 0 to 2.

Is fine-tuning available for the latest models?
See the fine-tuning guide for the latest information on which models are available for fine-tuning and how to get started.

Do you store the data that is passed into the API?
As of March 1st, 2023, we retain your API data for 30 days but no longer use your data sent via the API to improve our models. Learn more in our data usage policy. Some endpoints offer zero retention.

How can I make my application more safe?
If you want to add a moderation layer to the outputs of the Chat API, you can follow our moderation guide to prevent content that violates OpenAI’s usage policies from being shown. We also encourage you to read our safety guide for more information on how to build safer systems.

Should I use ChatGPT or the API?
ChatGPT offers a chat interface for our models and a range of built-in features such as integrated browsing, code execution, plugins, and more. By contrast, using OpenAI’s API provides more flexibility but requires that you write code or send the requests to our models programmatically.


Vision
Learn how to use vision capabilities to understand images.

Introduction
GPT-4o, GPT-4o mini, and GPT-4 Turbo have vision capabilities, meaning the models can take in images and answer questions about them. Historically, language model systems have been limited by taking in a single input modality, text.

Quickstart
Images are made available to the model in two main ways: by passing a link to the image or by passing the base64 encoded image directly in the request. Images can be passed in the user messages.

What's in this image?
python

python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])
The model is best at answering general questions about what is present in the images. While it does understand the relationship between objects in images, it is not yet optimized to answer detailed questions about the location of certain objects in an image. For example, you can ask it what color a car is or what some ideas for dinner might be based on what is in you fridge, but if you show it an image of a room and ask it where the chair is, it may not answer the question correctly.

It is important to keep in mind the limitations of the model as you explore what use-cases visual understanding can be applied to.

Video understanding with vision
Learn how to use use GPT-4 with Vision to understand videos in the OpenAI Cookbook

Uploading base 64 encoded images
If you have an image or set of images locally, you can pass those to the model in base 64 encoded format, here is an example of this in action:

import base64
import requests

# OpenAI API Key
api_key = "YOUR_OPENAI_API_KEY"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "path_to_your_image.jpg"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())
Multiple image inputs
The Chat Completions API is capable of taking in and processing multiple image inputs in both base64 encoded format or as an image URL. The model will process each image and use the information from all of them to answer the question.

Multiple image inputs
python

python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are in these images? Is there any difference between them?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
print(response.choices[0])
Here the model is shown two copies of the same image and can answer questions about both or each of the images independently.

Low or high fidelity image understanding
By controlling the detail parameter, which has three options, low, high, or auto, you have control over how the model processes the image and generates its textual understanding. By default, the model will use the auto setting which will look at the image input size and decide if it should use the low or high setting.

low will enable the "low res" mode. The model will receive a low-res 512px x 512px version of the image, and represent the image with a budget of 85 tokens. This allows the API to return faster responses and consume fewer input tokens for use cases that do not require high detail.
high will enable "high res" mode, which first allows the model to first see the low res image (using 85 tokens) and then creates detailed crops using 170 tokens for each 512px x 512px tile.
Choosing the detail level
python

python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)
Managing images
The Chat Completions API, unlike the Assistants API, is not stateful. That means you have to manage the messages (including images) you pass to the model yourself. If you want to pass the same image to the model multiple times, you will have to pass the image each time you make a request to the API.

For long running conversations, we suggest passing images via URL's instead of base64. The latency of the model can also be improved by downsizing your images ahead of time to be less than the maximum size they are expected them to be. For low res mode, we expect a 512px x 512px image. For high res mode, the short side of the image should be less than 768px and the long side should be less than 2,000px.

After an image has been processed by the model, it is deleted from OpenAI servers and not retained. We do not use data uploaded via the OpenAI API to train our models.

Limitations
While GPT-4 with vision is powerful and can be used in many situations, it is important to understand the limitations of the model. Here are some of the limitations we are aware of:

Medical images: The model is not suitable for interpreting specialized medical images like CT scans and shouldn't be used for medical advice.
Non-English: The model may not perform optimally when handling images with text of non-Latin alphabets, such as Japanese or Korean.
Small text: Enlarge text within the image to improve readability, but avoid cropping important details.
Rotation: The model may misinterpret rotated / upside-down text or images.
Visual elements: The model may struggle to understand graphs or text where colors or styles like solid, dashed, or dotted lines vary.
Spatial reasoning: The model struggles with tasks requiring precise spatial localization, such as identifying chess positions.
Accuracy: The model may generate incorrect descriptions or captions in certain scenarios.
Image shape: The model struggles with panoramic and fisheye images.
Metadata and resizing: The model doesn't process original file names or metadata, and images are resized before analysis, affecting their original dimensions.
Counting: May give approximate counts for objects in images.
CAPTCHAS: For safety reasons, we have implemented a system to block the submission of CAPTCHAs.
Calculating costs
Image inputs are metered and charged in tokens, just as text inputs are. The token cost of a given image is determined by two factors: its size, and the detail option on each image_url block. All images with detail: low cost 85 tokens each. detail: high images are first scaled to fit within a 2048 x 2048 square, maintaining their aspect ratio. Then, they are scaled such that the shortest side of the image is 768px long. Finally, we count how many 512px squares the image consists of. Each of those squares costs 170 tokens. Another 85 tokens are always added to the final total.

Here are some examples demonstrating the above.

A 1024 x 1024 square image in detail: high mode costs 765 tokens
1024 is less than 2048, so there is no initial resize.
The shortest side is 1024, so we scale the image down to 768 x 768.
4 512px square tiles are needed to represent the image, so the final token cost is 170 * 4 + 85 = 765.
A 2048 x 4096 image in detail: high mode costs 1105 tokens
We scale down the image to 1024 x 2048 to fit within the 2048 square.
The shortest side is 1024, so we further scale down to 768 x 1536.
6 512px tiles are needed, so the final token cost is 170 * 6 + 85 = 1105.
A 4096 x 8192 image in detail: low most costs 85 tokens
Regardless of input size, low detail images are a fixed cost.
FAQ
Can I fine-tune the image capabilities in gpt-4?
No, we do not support fine-tuning the image capabilities of gpt-4 at this time.

Can I use gpt-4 to generate images?
No, you can use dall-e-3 to generate images and gpt-4o, gpt-4o-mini or gpt-4-turbo to understand images.

What type of files can I upload?
We currently support PNG (.png), JPEG (.jpeg and .jpg), WEBP (.webp), and non-animated GIF (.gif).

Is there a limit to the size of the image I can upload?
Yes, we restrict image uploads to 20MB per image.

Can I delete an image I uploaded?
No, we will delete the image for you automatically after it has been processed by the model.

Where can I learn more about the considerations of GPT-4 with Vision?
You can find details about our evaluations, preparation, and mitigation work in the GPT-4 with Vision system card.

We have further implemented a system to block the submission of CAPTCHAs.

How do rate limits for GPT-4 with Vision work?
We process images at the token level, so each image we process counts towards your tokens per minute (TPM) limit. See the calculating costs section for details on the formula used to determine token count per image.

Can GPT-4 with Vision understand image metadata?
No, the model does not receive image metadata.

What happens if my image is unclear?
If an image is ambiguous or unclear, the model will do its best to interpret it. However, the results may be less accurate. A good rule of thumb is that if an average human cannot see the info in an image at the resolutions used in low/high res mode, then the model cannot either.


Function calling
Learn how to connect large language models to external tools.

Introduction
In an API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call one or many functions. The Chat Completions API does not call the function; instead, the model generates JSON that you can use to call the function in your code.

The latest models (gpt-4o, gpt-4-turbo, and gpt-4o-mini) have been trained to both detect when a function should to be called (depending on the input) and to respond with JSON that adheres to the function signature more closely than previous models. With this capability also comes potential risks. We strongly recommend building in user confirmation flows before taking actions that impact the world on behalf of users (sending an email, posting something online, making a purchase, etc).

This guide is focused on function calling with the Chat Completions API, for details on function calling in the Assistants API, please see the Assistants Tools page.

Common use cases
Function calling allows you to more reliably get structured data back from the model. For example, you can:

Create assistants that answer questions by calling external APIs
e.g. define functions like send_email(to: string, body: string), or get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')
Convert natural language into API calls
e.g. convert "Who are my top customers?" to get_customers(min_revenue: int, created_before: string, limit: int) and call your internal API
Extract structured data from text
e.g. define a function called extract_data(name: string, birthday: string), or sql_query(query: string)
...and much more!

The basic sequence of steps for function calling is as follows:

Call the model with the user query and a set of functions defined in the functions parameter.
The model can choose to call one or more functions; if so, the content will be a stringified JSON object adhering to your custom schema (note: the model may hallucinate parameters).
Parse the string into JSON in your code, and call your function with the provided arguments if they exist.
Call the model again by appending the function response as a new message, and let the model summarize the results back to the user.
Supported models
Not all model versions are trained with function calling data. Function calling is supported with the following models: gpt-4o, gpt-4o-2024-05-13, gpt-4o-mini, gpt-4o-mini-2024-07-18, gpt-4-turbo, gpt-4-turbo-2024-04-09, gpt-4-turbo-preview, gpt-4-0125-preview, gpt-4-1106-preview, gpt-4, gpt-4-0613, gpt-3.5-turbo, gpt-3.5-turbo-0125, gpt-3.5-turbo-1106, and gpt-3.5-turbo-0613.

In addition, parallel function calls is supported on the following models: gpt-4o, gpt-4o-2024-05-13, gpt-4o-mini, gpt-4o-mini-2024-07-18, gpt-4-turbo, gpt-4-turbo-2024-04-09, gpt-4-turbo-preview, gpt-4-0125-preview, gpt-4-1106-preview, gpt-3.5-turbo-0125, and gpt-3.5-turbo-1106.

Function calling behavior
The default behavior for tool_choice is tool_choice: "auto". This lets the model decide whether to call functions and, if so, which functions to call.

We offer three ways to customize the default behavior depending on your use case:

To force the model to always call one or more functions, you can set tool_choice: "required". The model will then select which function(s) to call.
To force the model to call only one specific function, you can set tool_choice: {"type": "function", "function": {"name": "my_function"}}.
To disable function calling and force the model to only generate a user-facing message, you can set tool_choice: "none".
Parallel function calling
Parallel function calling is the model's ability to perform multiple function calls together, allowing the effects and results of these function calls to be resolved in parallel. This is especially useful if functions take a long time, and reduces round trips with the API. For example, the model may call functions to get the weather in 3 different locations at the same time, which will result in a message with 3 function calls in the tool_calls array, each with an id. To respond to these function calls, add 3 new messages to the conversation, each containing the result of one function call, with a tool_call_id referencing the id from tool_calls.

Parallel function calling can be disabled by passing parallel_tool_calls: false in the request. The model will only call one function at a time when parallel function calling is disabled.

In this example, we define a single function get_current_weather. The model calls the function multiple times, and after sending the function response back to the model, we let it decide the next step. It responded with a user-facing message which was telling the user the temperature in San Francisco, Tokyo, and Paris. Depending on the query, it may choose to call a function again.

Example invoking multiple function calls in one response

You can find more examples of function calling in the OpenAI Cookbook:

Function calling
Learn from more examples demonstrating function calling

Tokens
Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means functions count against the model's context limit and are billed as input tokens. If running into context limits, we suggest limiting the number of functions or the length of documentation you provide for function parameters.

It is also possible to use fine-tuning to reduce the number of tokens used if you have many functions defined.

JSON Mode
A common way to use Chat Completions is to instruct the model to always return a JSON object that makes sense for your use case, by specifying this in the system message. While this does work in some cases, occasionally the models may generate output that does not parse to valid JSON objects.

To prevent these errors and improve model performance, when using gpt-4o, gpt-4-turbo, gpt-4o-mini, or gpt-3.5-turbo, you can set response_format to { "type": "json_object" } to enable JSON mode. When JSON mode is enabled, the model is constrained to only generate strings that parse into valid JSON object.

Important notes:

When using JSON mode, always instruct the model to produce JSON via some message in the conversation, for example via your system message. If you don't include an explicit instruction to generate JSON, the model may generate an unending stream of whitespace and the request may run continually until it reaches the token limit. To help ensure you don't forget, the API will throw an error if the string "JSON" does not appear somewhere in the context.
The JSON in the message the model returns may be partial (i.e. cut off) if finish_reason is length, which indicates the generation exceeded max_tokens or the conversation exceeded the token limit. To guard against this, check finish_reason before parsing the response.
JSON mode will not guarantee the output matches any specific schema, only that it is valid and parses without errors.
python

python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Who won the world series in 2020?"}
  ]
)
print(response.choices[0].message.content)
In this example, the response includes a JSON object that looks something like the following:

"content": "{\"winner\": \"Los Angeles Dodgers\"}"`
Note that JSON mode is always enabled when the model is generating arguments as part of function calling.

Advanced Usage
OpenAI's text generation models (often called generative pre-trained transformers or large language models) have been trained to understand natural language, code, and images. The models provide text outputs in response to their inputs. The text inputs to these models are also referred to as "prompts". Designing a prompt is essentially how you “program” a large language model model, usually by providing instructions or some examples of how to successfully complete a task.

Reproducible outputs Beta

Chat Completions are non-deterministic by default (which means model outputs may differ from request to request). That being said, we offer some control towards deterministic outputs by giving you access to the seed parameter and the system_fingerprint response field.

To receive (mostly) deterministic outputs across API calls, you can:

Set the seed parameter to any integer of your choice and use the same value across requests you'd like deterministic outputs for.
Ensure all other parameters (like prompt or temperature) are the exact same across requests.
Sometimes, determinism may be impacted due to necessary changes OpenAI makes to model configurations on our end. To help you keep track of these changes, we expose the system_fingerprint field. If this value is different, you may see different outputs due to changes we've made on our systems.

Deterministic outputs
Explore the new seed parameter in the OpenAI cookbook

Managing tokens
Language models read and write text in chunks called tokens. In English, a token can be as short as one character or as long as one word (e.g., a or apple), and in some languages tokens can be even shorter than one character or even longer than one word.

As a rough rule of thumb, 1 token is approximately 4 characters or 0.75 words for English text.

Check out our Tokenizer tool to test specific strings and see how they are translated into tokens.

For example, the string "ChatGPT is great!" is encoded into six tokens: ["Chat", "G", "PT", " is", " great", "!"].

The total number of tokens in an API call affects:

How much your API call costs, as you pay per token
How long your API call takes, as writing more tokens takes more time
Whether your API call works at all, as total tokens must be below the model's maximum limit (4097 tokens for gpt-3.5-turbo)
Both input and output tokens count toward these quantities. For example, if your API call used 10 tokens in the message input and you received 20 tokens in the message output, you would be billed for 30 tokens. Note however that for some models the price per token is different for tokens in the input vs. the output (see the pricing page for more information).

To see how many tokens are used by an API call, check the usage field in the API response (e.g., response['usage']['total_tokens']).

Chat models like gpt-3.5-turbo and gpt-4-turbo-preview use tokens in the same way as the models available in the completions API, but because of their message-based formatting, it's more difficult to count how many tokens will be used by a conversation.

DEEP DIVE
Counting tokens for chat API calls
To see how many tokens are in a text string without making an API call, use OpenAI’s tiktoken Python library. Example code can be found in the OpenAI Cookbook’s guide on how to count tokens with tiktoken.

Each message passed to the API consumes the number of tokens in the content, role, and other fields, plus a few extra for behind-the-scenes formatting. This may change slightly in the future.

If a conversation has too many tokens to fit within a model’s maximum limit (e.g., more than 4097 tokens for gpt-3.5-turbo or more than 128k tokens for gpt-4o), you will have to truncate, omit, or otherwise shrink your text until it fits. Beware that if a message is removed from the messages input, the model will lose all knowledge of it.

Note that very long conversations are more likely to receive incomplete replies. For example, a gpt-3.5-turbo conversation that is 4090 tokens long will have its reply cut off after just 6 tokens.

Parameter details
Frequency and presence penalties
The frequency and presence penalties found in the Chat Completions API and Legacy Completions API can be used to reduce the likelihood of sampling repetitive sequences of tokens.

DEEP DIVE
Penalties behind the scenes
Reasonable values for the penalty coefficients are around 0.1 to 1 if the aim is to just reduce repetitive samples somewhat. If the aim is to strongly suppress repetition, then one can increase the coefficients up to 2, but this can noticeably degrade the quality of samples. Negative values can be used to increase the likelihood of repetition.

Token log probabilities
The logprobs parameter found in the Chat Completions API and Legacy Completions API, when requested, provides the log probabilities of each output token, and a limited number of the most likely tokens at each token position alongside their log probabilities. This can be useful in some cases to assess the confidence of the model in its output, or to examine alternative responses the model might have given.


Chat Completions
Learn how to use OpenAI's Core API endpoint to get responses from language models.

Try GPT-4o
Try out GPT-4o in the playground

Explore GPT-4o with image inputs
Check out the vision guide for image understanding

To use one of these models via the OpenAI API, you’ll send a request to the Chat Completions API containing the inputs and your API key, and receive a response containing the model’s output.

You can experiment with various models in the chat playground. If you’re not sure which model to use then try gpt-4o if you need high intelligence or gpt-4o-mini if you need the fastest speed and lowest cost.

Overview
The Chat Completions API supports text and image inputs, and can output text content (including code and JSON).

It accepts inputs via the messages parameter, which is an array of message objects.

Message roles
Each message object has a role (either system, user, or assistant) and content.

The system message is optional and can be used to set the behavior of the assistant
The user messages provide requests or comments for the assistant to respond to
Assistant messages store previous assistant responses, but can also be written by you to give examples of desired behavior (few-shot examples)
By default, the system message is "You are a helpful assistant". You can define instructions in the user message, but the instructions set in the system message are more effective. You can only set one system message per conversation.

Getting started
Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it’s just as useful for single-turn tasks without any conversation.

An example Chat Completions API call looks like the following:

python

python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)
To learn more, you can view the full API reference documentation for the Chat API.

Including conversation history is important when user instructions refer to prior messages. In the example above, the user's final question of "Where was it played?" only makes sense in the context of the prior messages about the World Series of 2020. Because the models have no memory of past requests, all relevant information must be supplied as part of the conversation history in each request. If a conversation cannot fit within the model’s token limit, it will need to be shortened in some way.

To mimic the effect seen in ChatGPT where the text is returned iteratively, set the stream parameter to true.

Chat Completions response format

An example Chat Completions API response looks as follows:

{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
        "role": "assistant"
      },
      "logprobs": null
    }
  ],
  "created": 1677664795,
  "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
  "model": "gpt-4o-mini",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 17,
    "prompt_tokens": 57,
    "total_tokens": 74
  }
}
The assistant's reply can be extracted with:

python

python
message = completion.choices[0].message.content
Every response will include a finish_reason. The possible values for finish_reason are:

stop: API returned complete message, or a message terminated by one of the stop sequences provided via the stop parameter
length: Incomplete model output due to max_tokens parameter or token limit
function_call: The model decided to call a function
content_filter: Omitted content due to a flag from our content filters
null: API response still in progress or incomplete
Depending on input parameters, the model response may include different information.

Text to speech
Learn how to turn text into lifelike spoken audio

Overview
The Audio API provides a speech endpoint based on our TTS (text-to-speech) model. It comes with 6 built-in voices and can be used to:

Narrate a written blog post
Produce spoken audio in multiple languages
Give real time audio output using streaming
Here is an example of the alloy voice:

Please note that our usage policies require you to provide a clear disclosure to end users that the TTS voice they are hearing is AI-generated and not a human voice.

Quickstart
The speech endpoint takes in three key inputs: the model, the text that should be turned into audio, and the voice to be used for the audio generation. A simple request would look like the following:

Generate spoken audio from input text
python

python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
By default, the endpoint will output a MP3 file of the spoken audio but it can also be configured to output any of our supported formats.

Audio quality
For real-time applications, the standard tts-1 model provides the lowest latency but at a lower quality than the tts-1-hd model. Due to the way the audio is generated, tts-1 is likely to generate content that has more static in certain situations than tts-1-hd. In some cases, the audio may not have noticeable differences depending on your listening device and the individual person.

Voice options
Experiment with different voices (alloy, echo, fable, onyx, nova, and shimmer) to find one that matches your desired tone and audience. The current voices are optimized for English.

Alloy
Echo
Fable
Onyx
Nova
Shimmer
Streaming real time audio
The Speech API provides support for real time audio streaming using chunk transfer encoding. This means that the audio is able to be played before the full file has been generated and made accessible.

from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="Hello world! This is a streaming test.",
)

response.stream_to_file("output.mp3")
Supported output formats
The default response format is "mp3", but other formats like "opus", "aac", "flac", and "pcm" are available.

Opus: For internet streaming and communication, low latency.
AAC: For digital audio compression, preferred by YouTube, Android, iOS.
FLAC: For lossless audio compression, favored by audio enthusiasts for archiving.
WAV: Uncompressed WAV audio, suitable for low-latency applications to avoid decoding overhead.
PCM: Similar to WAV but containing the raw samples in 24kHz (16-bit signed, low-endian), without the header.
Supported languages
The TTS model generally follows the Whisper model in terms of language support. Whisper supports the following languages and performs well despite the current voices being optimized for English:

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

You can generate spoken audio in these languages by providing the input text in the language of your choice.

FAQ
How can I control the emotional range of the generated audio?
There is no direct mechanism to control the emotional output of the audio generated. Certain factors may influence the output audio like capitalization or grammar but our internal tests with these have yielded mixed results.

Can I create a custom copy of my own voice?
No, this is not something we support.

Do I own the outputted audio files?
Yes, like with all outputs from our API, the person who created them owns the output. You are still required to inform end users that they are hearing audio generated by AI and not a real person talking to them.


Speech to text
Learn how to turn audio into text

Introduction
The Audio API provides two speech to text endpoints, transcriptions and translations, based on our state-of-the-art open source large-v2 Whisper model. They can be used to:

Transcribe audio into whatever language the audio is in.
Translate and transcribe the audio into english.
File uploads are currently limited to 25 MB and the following input file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.

Quickstart
Transcriptions
The transcriptions API takes as input the audio file you want to transcribe and the desired output file format for the transcription of the audio. We currently support multiple input and output file formats.

Transcribe audio
python

python
from openai import OpenAI
client = OpenAI()

audio_file= open("/path/to/file/audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)
By default, the response type will be json with the raw text included.

{
  "text": "Imagine the wildest idea that you've ever had, and you're curious about how it might scale to something that's a 100, a 1,000 times bigger.
....
}
The Audio API also allows you to set additional parameters in a request. For example, if you want to set the response_format as text, your request would look like the following:

Additional options
python

python
from openai import OpenAI
client = OpenAI()

audio_file = open("/path/to/file/speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)
print(transcription.text)
The API Reference includes the full list of available parameters.

Translations
The translations API takes as input the audio file in any of the supported languages and transcribes, if necessary, the audio into English. This differs from our /Transcriptions endpoint since the output is not in the original input language and is instead translated to English text.

Translate audio
python

python
from openai import OpenAI
client = OpenAI()

audio_file= open("/path/to/file/german.mp3", "rb")
translation = client.audio.translations.create(
  model="whisper-1", 
  file=audio_file
)
print(translation.text)
In this case, the inputted audio was german and the outputted text looks like:

Hello, my name is Wolfgang and I come from Germany. Where are you heading today?
We only support translation into English at this time.

Supported languages
We currently support the following languages through both the transcriptions and translations endpoint:

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

While the underlying model was trained on 98 languages, we only list the languages that exceeded <50% word error rate (WER) which is an industry standard benchmark for speech to text model accuracy. The model will return results for languages not listed above but the quality will be low.

Timestamps
By default, the Whisper API will output a transcript of the provided audio in text. The timestamp_granularities[] parameter enables a more structured and timestamped json output format, with timestamps at the segment, word level, or both. This enables word-level precision for transcripts and video edits, which allows for the removal of specific frames tied to individual words.

Timestamp options
python

python
from openai import OpenAI
client = OpenAI()

audio_file = open("speech.mp3", "rb")
transcript = client.audio.transcriptions.create(
  file=audio_file,
  model="whisper-1",
  response_format="verbose_json",
  timestamp_granularities=["word"]
)

print(transcript.words)
Longer inputs
By default, the Whisper API only supports files that are less than 25 MB. If you have an audio file that is longer than that, you will need to break it up into chunks of 25 MB's or less or used a compressed audio format. To get the best performance, we suggest that you avoid breaking the audio up mid-sentence as this may cause some context to be lost.

One way to handle this is to use the PyDub open source Python package to split the audio:

from pydub import AudioSegment

song = AudioSegment.from_mp3("good_morning.mp3")

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

first_10_minutes = song[:ten_minutes]

first_10_minutes.export("good_morning_10.mp3", format="mp3")
OpenAI makes no guarantees about the usability or security of 3rd party software like PyDub.

Prompting
You can use a prompt to improve the quality of the transcripts generated by the Whisper API. The model will try to match the style of the prompt, so it will be more likely to use capitalization and punctuation if the prompt does too. However, the current prompting system is much more limited than our other language models and only provides limited control over the generated audio. Here are some examples of how prompting can help in different scenarios:

Prompts can be very helpful for correcting specific words or acronyms that the model may misrecognize in the audio. For example, the following prompt improves the transcription of the words DALL·E and GPT-3, which were previously written as "GDP 3" and "DALI": "The transcript is about OpenAI which makes technology like DALL·E, GPT-3, and ChatGPT with the hope of one day building an AGI system that benefits all of humanity"
To preserve the context of a file that was split into segments, you can prompt the model with the transcript of the preceding segment. This will make the transcript more accurate, as the model will use the relevant information from the previous audio. The model will only consider the final 224 tokens of the prompt and ignore anything earlier. For multilingual inputs, Whisper uses a custom tokenizer. For English only inputs, it uses the standard GPT-2 tokenizer which are both accessible through the open source Whisper Python package.
Sometimes the model might skip punctuation in the transcript. You can avoid this by using a simple prompt that includes punctuation: "Hello, welcome to my lecture."
The model may also leave out common filler words in the audio. If you want to keep the filler words in your transcript, you can use a prompt that contains them: "Umm, let me think like, hmm... Okay, here's what I'm, like, thinking."
Some languages can be written in different ways, such as simplified or traditional Chinese. The model might not always use the writing style that you want for your transcript by default. You can improve this by using a prompt in your preferred writing style.
Improving reliability
As we explored in the prompting section, one of the most common challenges faced when using Whisper is the model often does not recognize uncommon words or acronyms. To address this, we have highlighted different techniques which improve the reliability of Whisper in these cases:

Using the prompt parameter
The first method involves using the optional prompt parameter to pass a dictionary of the correct spellings.

Since it wasn't trained using instruction-following techniques, Whisper operates more like a base GPT model. It's important to keep in mind that Whisper only considers the first 244 tokens of the prompt.

Prompt parameter
python

python
from openai import OpenAI
client = OpenAI()

audio_file = open("/path/to/file/speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text",
  prompt="ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T."
)
print(transcription.text)
While it will increase reliability, this technique is limited to only 244 characters so your list of SKUs would need to be relatively small in order for this to be a scalable solution.

Post-processing with GPT-4
The second method involves a post-processing step using GPT-4 or GPT-3.5-Turbo.

We start by providing instructions for GPT-4 through the system_prompt variable. Similar to what we did with the prompt parameter earlier, we can define our company and product names.

Post-processing
python

python
system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

def generate_corrected_transcript(temperature, system_prompt, audio_file):
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    return completion.choices[0].message.content

corrected_text = generate_corrected_transcript(0, system_prompt, fake_company_filepath)
If you try this on your own audio file, you can see that GPT-4 manages to correct many misspellings in the transcript. Due to its larger context window, this method might be more scalable than using Whisper's prompt parameter and is more reliable since GPT-4 can be instructed and guided in ways that aren't possible with Whisper given the lack of instruction following.


Embeddings
Learn how to turn text into numbers, unlocking use cases like search.

New embedding models

text-embedding-3-small and text-embedding-3-large, our newest and most performant embedding models are now available, with lower costs, higher multilingual performance, and new parameters to control the overall size.
What are embeddings?
OpenAI’s text embeddings measure the relatedness of text strings. Embeddings are commonly used for:

Search (where results are ranked by relevance to a query string)
Clustering (where text strings are grouped by similarity)
Recommendations (where items with related text strings are recommended)
Anomaly detection (where outliers with little relatedness are identified)
Diversity measurement (where similarity distributions are analyzed)
Classification (where text strings are classified by their most similar label)
An embedding is a vector (list) of floating point numbers. The distance between two vectors measures their relatedness. Small distances suggest high relatedness and large distances suggest low relatedness.

Visit our pricing page to learn about Embeddings pricing. Requests are billed based on the number of tokens in the input.

How to get embeddings
To get an embedding, send your text string to the embeddings API endpoint along with the embedding model name (e.g. text-embedding-3-small). The response will contain an embedding (list of floating point numbers), which you can extract, save in a vector database, and use for many different use cases:

Example: Getting embeddings
curl

curl
curl https://api.openai.com/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "input": "Your text string goes here",
    "model": "text-embedding-3-small"
  }'
The response will contain the embedding vector along with some additional metadata.

Example embedding response
json

json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -0.006929283495992422,
        -0.005336422007530928,
        ... (omitted for spacing)
        -4.547132266452536e-05,
        -0.024047505110502243
      ],
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 5,
    "total_tokens": 5
  }
}
By default, the length of the embedding vector will be 1536 for text-embedding-3-small or 3072 for text-embedding-3-large. You can reduce the dimensions of the embedding by passing in the dimensions parameter without the embedding losing its concept-representing properties. We go into more detail on embedding dimensions in the embedding use case section.

Embedding models
OpenAI offers two powerful third-generation embedding model (denoted by -3 in the model ID). You can read the embedding v3 announcement blog post for more details.

Usage is priced per input token, below is an example of pricing pages of text per US dollar (assuming ~800 tokens per page):

MODEL	~ PAGES PER DOLLAR	PERFORMANCE ON MTEB EVAL	MAX INPUT
text-embedding-3-small	62,500	62.3%	8191
text-embedding-3-large	9,615	64.6%	8191
text-embedding-ada-002	12,500	61.0%	8191
Use cases
Here we show some representative use cases. We will use the Amazon fine-food reviews dataset for the following examples.

Obtaining the embeddings
The dataset contains a total of 568,454 food reviews Amazon users left up to October 2012. We will use a subset of 1,000 most recent reviews for illustration purposes. The reviews are in English and tend to be positive or negative. Each review has a ProductId, UserId, Score, review title (Summary) and review body (Text). For example:

PRODUCT ID	USER ID	SCORE	SUMMARY	TEXT
B001E4KFG0	A3SGXH7AUHU8GW	5	Good Quality Dog Food	I have bought several of the Vitality canned...
B00813GRG4	A1D87F6ZCVE5NK	1	Not as Advertised	Product arrived labeled as Jumbo Salted Peanut...
We will combine the review summary and review text into a single combined text. The model will encode this combined text and output a single vector embedding.

Get_embeddings_from_dataset.ipynb

from openai import OpenAI
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('output/embedded_1k_reviews.csv', index=False)
To load the data from a saved file, you can run the following:

import pandas as pd

df = pd.read_csv('output/embedded_1k_reviews.csv')
df['ada_embedding'] = df.ada_embedding.apply(eval).apply(np.array)
Reducing embedding dimensions
Question answering using embeddings-based search
Text search using embeddings
Code search using embeddings
Recommendations using embeddings
Data visualization in 2D
Embedding as a text feature encoder for ML algorithms
Classification using the embedding features
Zero-shot classification
Obtaining user and product embeddings for cold-start recommendation
Clustering
FAQ
How can I tell how many tokens a string has before I embed it?
In Python, you can split a string into tokens with OpenAI's tokenizer tiktoken.

Example code:

import tiktoken

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

num_tokens_from_string("tiktoken is great!", "cl100k_base")
For third-generation embedding models like text-embedding-3-small, use the cl100k_base encoding.

More details and example code are in the OpenAI Cookbook guide how to count tokens with tiktoken.

How can I retrieve K nearest embedding vectors quickly?
For searching over many vectors quickly, we recommend using a vector database. You can find examples of working with vector databases and the OpenAI API in our Cookbook on GitHub.

Which distance function should I use?
We recommend cosine similarity. The choice of distance function typically doesn’t matter much.

OpenAI embeddings are normalized to length 1, which means that:

Cosine similarity can be computed slightly faster using just a dot product
Cosine similarity and Euclidean distance will result in the identical rankings
Can I share my embeddings online?
Yes, customers own their input and output from our models, including in the case of embeddings. You are responsible for ensuring that the content you input to our API does not violate any applicable law or our Terms of Use.

Do V3 embedding models know about recent events?
No, the text-embedding-3-large and text-embedding-3-small models lack knowledge of events that occurred after September 2021. This is generally not as much of a limitation as it would be for text generation models but in certain edge cases it can reduce performance.

Assistants API OverviewBeta

The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and files to respond to user queries. The Assistants API currently supports three types of tools: Code Interpreter, File Search, and Function calling.

You can explore the capabilities of the Assistants API using the Assistants playground or by building a step-by-step integration outlined in our Assistants API quickstart.

How Assistants work

The Assistants API is designed to help developers build powerful AI assistants capable of performing a variety of tasks.

The Assistants API is in beta and we are actively working on adding more functionality. Share your feedback in our Developer Forum!
Assistants can call OpenAI’s models with specific instructions to tune their personality and capabilities.
Assistants can access multiple tools in parallel. These can be both OpenAI-hosted tools — like code_interpreter and file_search — or tools you build / host (via function calling).
Assistants can access persistent Threads. Threads simplify AI application development by storing message history and truncating it when the conversation gets too long for the model’s context length. You create a Thread once, and simply append Messages to it as your users reply.
Assistants can access files in several formats — either as part of their creation or as part of Threads between Assistants and users. When using tools, Assistants can also create files (e.g., images, spreadsheets, etc) and cite files they reference in the Messages they create.
Objects
Assistants object architecture diagram

OBJECT	WHAT IT REPRESENTS
Assistant	Purpose-built AI that uses OpenAI’s models and calls tools
Thread	A conversation session between an Assistant and a user. Threads store Messages and automatically handle truncation to fit content into a model’s context.
Message	A message created by an Assistant or a user. Messages can include text, images, and other files. Messages stored as a list on the Thread.
Run	An invocation of an Assistant on a Thread. The Assistant uses its configuration and the Thread’s Messages to perform tasks by calling models and tools. As part of a Run, the Assistant appends Messages to the Thread.
Run Step	A detailed list of steps the Assistant took as part of a Run. An Assistant can call tools or create Messages during its run. Examining Run Steps allows you to introspect how the Assistant is getting to its final results.

Assistants API Quickstart Beta

A typical integration of the Assistants API has the following flow:

Create an Assistant by defining its custom instructions and picking a model. If helpful, add files and enable tools like Code Interpreter, File Search, and Function calling.
Create a Thread when a user starts a conversation.
Add Messages to the Thread as the user asks questions.
Run the Assistant on the Thread to generate a response by calling the model and the tools.
This starter guide walks through the key steps to create and run an Assistant that uses Code Interpreter. In this example, we're creating an Assistant that is a personal math tutor, with the Code Interpreter tool enabled.

Calls to the Assistants API require that you pass a beta HTTP header. This is handled automatically if you’re using OpenAI’s official Python or Node.js SDKs. OpenAI-Beta: assistants=v2

Step 1: Create an Assistant
An Assistant represents an entity that can be configured to respond to a user's messages using several parameters like model, instructions, and tools.

Create an Assistant
python

python
from openai import OpenAI
client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Math Tutor",
  instructions="You are a personal math tutor. Write and run code to answer math questions.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)
Step 2: Create a Thread
A Thread represents a conversation between a user and one or many Assistants. You can create a Thread when a user (or your AI application) starts a conversation with your Assistant.

Create a Thread
python

python
thread = client.beta.threads.create()
Step 3: Add a Message to the Thread
The contents of the messages your users or applications create are added as Message objects to the Thread. Messages can contain both text and files. There is no limit to the number of Messages you can add to Threads — we smartly truncate any context that does not fit into the model's context window.

Add a Message to the Thread
python

python
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
Step 4: Create a Run
Once all the user Messages have been added to the Thread, you can Run the Thread with any Assistant. Creating a Run uses the model and tools associated with the Assistant to generate a response. These responses are added to the Thread as assistant Messages.

You can use the 'create and stream' helpers in the Python and Node SDKs to create a run and stream the response.

Create and Stream a Run
python

python
from typing_extensions import override
from openai import AssistantEventHandler
 
# First, we create a EventHandler class to define
# how we want to handle the events in the response stream.
 
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)
 
# Then, we use the `stream` SDK helper 
# with the `EventHandler` class to create the Run 
# and stream the response.
 
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account.",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()
See the full list of Assistants streaming events in our API reference here. You can also see a list of SDK event listeners for these events in the Python & Node repository documentation.

Next steps
Continue learning about Assistants Concepts in the Deep Dive
Learn more about Tools
Explore the Assistants playground
Check out our Assistants Quickstart app on github

Assistants API Deep dive Beta

As described in the Assistants Overview, there are several concepts involved in building an app with the Assistants API.

This guide goes deeper into each of these concepts.

If you want to get started coding right away, check out the Assistants API Quickstart.

Creating Assistants
We recommend using OpenAI's latest models with the Assistants API for best results and maximum compatibility with tools.

To get started, creating an Assistant only requires specifying the model to use. But you can further customize the behavior of the Assistant:

Use the instructions parameter to guide the personality of the Assistant and define its goals. Instructions are similar to system messages in the Chat Completions API.
Use the tools parameter to give the Assistant access to up to 128 tools. You can give it access to OpenAI-hosted tools like code_interpreter and file_search, or call a third-party tools via a function calling.
Use the tool_resources parameter to give the tools like code_interpreter and file_search access to files. Files are uploaded using the File upload endpoint and must have the purpose set to assistants to be used with this API.
For example, to create an Assistant that can create data visualization based on a .csv file, first upload a file.

python

python
file = client.files.create(
  file=open("revenue-forecast.csv", "rb"),
  purpose='assistants'
)
Then, create the Assistant with the code_interpreter tool enabled and provide the file as a resource to the tool.

python

python
assistant = client.beta.assistants.create(
  name="Data visualizer",
  description="You are great at creating beautiful data visualizations. You analyze data present in .csv files, understand trends, and come up with data visualizations relevant to those trends. You also share a brief text summary of the trends observed.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
You can attach a maximum of 20 files to code_interpreter and 10,000 files to file_search (using vector_store objects).

Each file can be at most 512 MB in size and have a maximum of 5,000,000 tokens. By default, the size of all the files uploaded by your organization cannot exceed 100 GB, but you can reach out to our support team to increase this limit.

Managing Threads and Messages
Threads and Messages represent a conversation session between an Assistant and a user. There is no limit to the number of Messages you can store in a Thread. Once the size of the Messages exceeds the context window of the model, the Thread will attempt to smartly truncate messages, before fully dropping the ones it considers the least important.

You can create a Thread with an initial list of Messages like this:

python

python
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Create 3 data visualizations based on the trends in this file.",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)
Messages can contain text, images, or file attachment. Message attachments are helper methods that add files to a thread's tool_resources. You can also choose to add files to the thread.tool_resources directly.

Creating image input content
Message content can contain either external image URLs or File IDs uploaded via the File API. Only models with Vision support can accept image input. Supported image content types include png, jpg, gif, and webp. When creating image files, pass purpose="vision" to allow you to later download and display the input content. Currently, there is a 100GB limit per organization and 10GB for user in organization. Please contact us to request a limit increase.

Tools cannot access image content unless specified. To pass image files to Code Interpreter, add the file ID in the message attachments list to allow the tool to read and analyze the input. Image URLs cannot be downloaded in Code Interpreter today.

python

python
file = client.files.create(
  file=open("myimage.png", "rb"),
  purpose="vision"
)
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is the difference between these images?"
        },
        {
          "type": "image_url",
          "image_url": {"url": "https://example.com/image.png"}
        },
        {
          "type": "image_file",
          "image_file": {"file_id": file.id}
        },
      ],
    }
  ]
)
Low or high fidelity image understanding
By controlling the detail parameter, which has three options, low, high, or auto, you have control over how the model processes the image and generates its textual understanding.

low will enable the "low res" mode. The model will receive a low-res 512px x 512px version of the image, and represent the image with a budget of 85 tokens. This allows the API to return faster responses and consume fewer input tokens for use cases that do not require high detail.
high will enable "high res" mode, which first allows the model to see the low res image and then creates detailed crops of input images based on the input image size. Use the pricing calculator to see token counts for various image sizes.
python

python
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is this an image of?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/image.png",
            "detail": "high"
          }
        },
      ],
    }
  ]
)
Context window management
The Assistants API automatically manages the truncation to ensure it stays within the model's maximum context length. You can customize this behavior by specifying the maximum tokens you'd like a run to utilize and/or the maximum number of recent messages you'd like to include in a run.

Max Completion and Max Prompt Tokens
To control the token usage in a single Run, set max_prompt_tokens and max_completion_tokens when creating the Run. These limits apply to the total number of tokens used in all completions throughout the Run's lifecycle.

For example, initiating a Run with max_prompt_tokens set to 500 and max_completion_tokens set to 1000 means the first completion will truncate the thread to 500 tokens and cap the output at 1000 tokens. If only 200 prompt tokens and 300 completion tokens are used in the first completion, the second completion will have available limits of 300 prompt tokens and 700 completion tokens.

If a completion reaches the max_completion_tokens limit, the Run will terminate with a status of incomplete, and details will be provided in the incomplete_details field of the Run object.

When using the File Search tool, we recommend setting the max_prompt_tokens to no less than 20,000. For longer conversations or multiple interactions with File Search, consider increasing this limit to 50,000, or ideally, removing the max_prompt_tokens limits altogether to get the highest quality results.

Truncation Strategy
You may also specify a truncation strategy to control how your thread should be rendered into the model's context window. Using a truncation strategy of type auto will use OpenAI's default truncation strategy. Using a truncation strategy of type last_messages will allow you to specify the number of the most recent messages to include in the context window.

Message annotations
Messages created by Assistants may contain annotations within the content array of the object. Annotations provide information around how you should annotate the text in the Message.

There are two types of Annotations:

file_citation: File citations are created by the file_search tool and define references to a specific file that was uploaded and used by the Assistant to generate the response.
file_path: File path annotations are created by the code_interpreter tool and contain references to the files generated by the tool.
When annotations are present in the Message object, you'll see illegible model-generated substrings in the text that you should replace with the annotations. These strings may look something like 【13†source】 or sandbox:/mnt/data/file.csv. Here’s an example python code snippet that replaces these strings with information present in the annotations.

python

python
# Retrieve the message object
message = client.beta.threads.messages.retrieve(
  thread_id="...",
  message_id="..."
)
# Extract the message content
message_content = message.content[0].text
annotations = message_content.annotations
citations = []
# Iterate over the annotations and add footnotes
for index, annotation in enumerate(annotations):
    # Replace the text with a footnote
    message_content.value = message_content.value.replace(annotation.text, f' [{index}]')
    # Gather citations based on annotation attributes
    if (file_citation := getattr(annotation, 'file_citation', None)):
        cited_file = client.files.retrieve(file_citation.file_id)
        citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
    elif (file_path := getattr(annotation, 'file_path', None)):
        cited_file = client.files.retrieve(file_path.file_id)
        citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
        # Note: File download functionality not implemented above for brevity
# Add footnotes to the end of the message before displaying to user
message_content.value += '\n' + '\n'.join(citations)
Runs and Run Steps
When you have all the context you need from your user in the Thread, you can run the Thread with an Assistant of your choice.

python

python
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id
)
By default, a Run will use the model and tools configuration specified in Assistant object, but you can override most of these when creating the Run for added flexibility:

python

python
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  model="gpt-4o",
  instructions="New instructions that override the Assistant instructions",
  tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
)
Note: tool_resources associated with the Assistant cannot be overridden during Run creation. You must use the modify Assistant endpoint to do this.

Run lifecycle
Run objects can have multiple statuses.

Run lifecycle - diagram showing possible status transitions

STATUS	DEFINITION
queued	When Runs are first created or when you complete the required_action, they are moved to a queued status. They should almost immediately move to in_progress.
in_progress	While in_progress, the Assistant uses the model and tools to perform steps. You can view progress being made by the Run by examining the Run Steps.
completed	The Run successfully completed! You can now view all Messages the Assistant added to the Thread, and all the steps the Run took. You can also continue the conversation by adding more user Messages to the Thread and creating another Run.
requires_action	When using the Function calling tool, the Run will move to a required_action state once the model determines the names and arguments of the functions to be called. You must then run those functions and submit the outputs before the run proceeds. If the outputs are not provided before the expires_at timestamp passes (roughly 10 mins past creation), the run will move to an expired status.
expired	This happens when the function calling outputs were not submitted before expires_at and the run expires. Additionally, if the runs take too long to execute and go beyond the time stated in expires_at, our systems will expire the run.
cancelling	You can attempt to cancel an in_progress run using the Cancel Run endpoint. Once the attempt to cancel succeeds, status of the Run moves to cancelled. Cancellation is attempted but not guaranteed.
cancelled	Run was successfully cancelled.
failed	You can view the reason for the failure by looking at the last_error object in the Run. The timestamp for the failure will be recorded under failed_at.
incomplete	Run ended due to max_prompt_tokens or max_completion_tokens reached. You can view the specific reason by looking at the incomplete_details object in the Run.
Polling for updates
If you are not using streaming, in order to keep the status of your run up to date, you will have to periodically retrieve the Run object. You can check the status of the run each time you retrieve the object to determine what your application should do next.

You can optionally use Polling Helpers in our Node and Python SDKs to help you with this. These helpers will automatically poll the Run object for you and return the Run object when it's in a terminal state.

Thread locks
When a Run is in_progress and not in a terminal state, the Thread is locked. This means that:

New Messages cannot be added to the Thread.
New Runs cannot be created on the Thread.
Run steps
Run steps lifecycle - diagram showing possible status transitions

Run step statuses have the same meaning as Run statuses.

Most of the interesting detail in the Run Step object lives in the step_details field. There can be two types of step details:

message_creation: This Run Step is created when the Assistant creates a Message on the Thread.
tool_calls: This Run Step is created when the Assistant calls a tool. Details around this are covered in the relevant sections of the Tools guide.
Data Access Guidance
Currently, Assistants, Threads, Messages, and Vector Stores created via the API are scoped to the Project they're created in. As such, any person with API key access to that Project is able to read or write Assistants, Threads, Messages, and Runs in the Project.

We strongly recommend the following data access controls:

Implement authorization. Before performing reads or writes on Assistants, Threads, Messages, and Vector Stores, ensure that the end-user is authorized to do so. For example, store in your database the object IDs that the end-user has access to, and check it before fetching the object ID with the API.
Restrict API key access. Carefully consider who in your organization should have API keys and be part of a Project. Periodically audit this list. API keys enable a wide range of operations including reading and modifying sensitive information, such as Messages and Files.
Create separate accounts. Consider creating separate Projects for different applications in order to isolate data across multiple applications.

Assistant Tools Beta

Assistants created using the Assistants API can be equipped with tools that allow them to perform more complex tasks or interact with your application. We provide built-in tools for assistants, but you can also define your own tools to extend their capabilities using Function Calling.

The Assistants API currently supports the following tools:

File Search
Built-in RAG tool to process and search through files

Code Interpreter
Write and run python code, process files and diverse data

Function Calling
Use your own custom functions to interact with your application

File Search Beta

File Search augments the Assistant with knowledge from outside its model, such as proprietary product information or documents provided by your users. OpenAI automatically parses and chunks your documents, creates and stores the embeddings, and use both vector and keyword search to retrieve relevant content to answer user queries.

Quickstart
In this example, we’ll create an assistant that can help answer questions about companies’ financial statements.

Step 1: Create a new Assistant with File Search Enabled
Create a new assistant with file_search enabled in the tools parameter of the Assistant.

python

python
from openai import OpenAI
 
client = OpenAI()
 
assistant = client.beta.assistants.create(
  name="Financial Analyst Assistant",
  instructions="You are an expert financial analyst. Use you knowledge base to answer questions about audited financial statements.",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
)
Once the file_search tool is enabled, the model decides when to retrieve content based on user messages.

Step 2: Upload files and add them to a Vector Store
To access your files, the file_search tool uses the Vector Store object. Upload your files and create a Vector Store to contain them. Once the Vector Store is created, you should poll its status until all files are out of the in_progress state to ensure that all content has finished processing. The SDK provides helpers to uploading and polling in one shot.

python

python
# Create a vector store caled "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")
 
# Ready the files for upload to OpenAI
file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]
file_streams = [open(path, "rb") for path in file_paths]
 
# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)
 
# You can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)
Step 3: Update the assistant to to use the new Vector Store
To make the files accessible to your assistant, update the assistant’s tool_resources with the new vector_store id.

python

python
assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)
Step 4: Create a thread
You can also attach files as Message attachments on your thread. Doing so will create another vector_store associated with the thread, or, if there is already a vector store attached to this thread, attach the new files to the existing thread vector store. When you create a Run on this thread, the file search tool will query both the vector_store from your assistant and the vector_store on the thread.

In this example, the user attached a copy of Apple’s latest 10-K filing.

python

python
# Upload the user provided file to OpenAI
message_file = client.files.create(
  file=open("edgar/aapl-10k.pdf", "rb"), purpose="assistants"
)
 
# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "How many shares of AAPL were outstanding at the end of of October 2023?",
      # Attach the new file to the message.
      "attachments": [
        { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
      ],
    }
  ]
)
 
# The thread now has a vector store with that file in its tool resources.
print(thread.tool_resources.file_search)
Vector stores created using message attachements have a default expiration policy of 7 days after they were last active (defined as the last time the vector store was part of a run). This default exists to help you manage your vector storage costs. You can override these expiration policies at any time. Learn more here.

Step 5: Create a run and check the output
Now, create a Run and observe that the model uses the File Search tool to provide a response to the user’s question.

python

python
from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
 
client = OpenAI()
 
class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    @override
    def on_message_done(self, message) -> None:
        # print a citation to the file searched
        message_content = message.content[0].text
        annotations = message_content.annotations
        citations = []
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f"[{index}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")

        print(message_content.value)
        print("\n".join(citations))


# Then, we use the stream SDK helper
# with the EventHandler class to create the Run
# and stream the response.

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
Your new assistant will query both attached vector stores (one containing goog-10k.pdf and brka-10k.txt, and the other containing aapl-10k.pdf) and return this result from aapl-10k.pdf.

How it works
The file_search tool implements several retrieval best practices out of the box to help you extract the right data from your files and augment the model’s responses. The file_search tool:

Rewrites user queries to optimize them for search.
Breaks down complex user queries into multiple searches it can run in parallel.
Runs both keyword and semantic searches across both assistant and thread vector stores.
Reranks search results to pick the most relevant ones before generating the final response.
By default, the file_search tool uses the following settings but these can be configured to suit your needs:

Chunk size: 800 tokens
Chunk overlap: 400 tokens
Embedding model: text-embedding-3-large at 256 dimensions
Maximum number of chunks added to context: 20 (could be fewer)
Known Limitations

We have a few known limitations we're working on adding support for in the coming months:

Support for deterministic pre-search filtering using custom metadata.
Support for parsing images within documents (including images of charts, graphs, tables etc.)
Support for retrievals over structured file formats (like csv or jsonl).
Better support for summarization — the tool today is optimized for search queries.
Vector stores
Vector Store objects give the File Search tool the ability to search your files. Adding a file to a vector_store automatically parses, chunks, embeds and stores the file in a vector database that's capable of both keyword and semantic search. Each vector_store can hold up to 10,000 files. Vector stores can be attached to both Assistants and Threads. Today, you can attach at most one vector store to an assistant and at most one vector store to a thread.

Creating vector stores and adding files
You can create a vector store and add files to it in a single API call:

python

python
vector_store = client.beta.vector_stores.create(
  name="Product Documentation",
  file_ids=['file_1', 'file_2', 'file_3', 'file_4', 'file_5']
)
Adding files to vector stores is an async operation. To ensure the operation is complete, we recommend that you use the 'create and poll' helpers in our official SDKs. If you're not using the SDKs, you can retrieve the vector_store object and monitor it's file_counts property to see the result of the file ingestion operation.

Files can also be added to a vector store after it's created by creating vector store files.

python

python
file = client.beta.vector_stores.files.create_and_poll(
  vector_store_id="vs_abc123",
  file_id="file-abc123"
)
Alternatively, you can add several files to a vector store by creating batches of up to 500 files.

python

python
batch = client.beta.vector_stores.file_batches.create_and_poll(
  vector_store_id="vs_abc123",
  file_ids=['file_1', 'file_2', 'file_3', 'file_4', 'file_5']
)
Similarly, these files can be removed from a vector store by either:

Deleting the vector store file object or,
By deleting the underlying file object (which removes the file it from all vector_store and code_interpreter configurations across all assistants and threads in your organization)
The maximum file size is 512 MB. Each file should contain no more than 5,000,000 tokens per file (computed automatically when you attach a file).

File Search supports a variety of file formats including .pdf, .md, and .docx. More details on the file extensions (and their corresponding MIME-types) supported can be found in the Supported files section below.

Attaching vector stores
You can attach vector stores to your Assistant or Thread using the tool_resources parameter.

python

python
assistant = client.beta.assistants.create(
  instructions="You are a helpful product support assistant and you answer questions based on the files provided to you.",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
  tool_resources={
    "file_search": {
      "vector_store_ids": ["vs_1"]
    }
  }
)

thread = client.beta.threads.create(
  messages=[ { "role": "user", "content": "How do I cancel my subscription?"} ],
  tool_resources={
    "file_search": {
      "vector_store_ids": ["vs_2"]
    }
  }
)
You can also attach a vector store to Threads or Assistants after they're created by updating them with the right tool_resources.

Ensuring vector store readiness before creating runs
We highly recommend that you ensure all files in a vector_store are fully processed before you create a run. This will ensure that all the data in your vector_store is searchable. You can check for vector_store readiness by using the polling helpers in our SDKs, or by manually polling the vector_store object to ensure the status is completed.

As a fallback, we've built a 60 second maximum wait in the Run object when the thread’s vector store contains files that are still being processed. This is to ensure that any files your users upload in a thread a fully searchable before the run proceeds. This fallback wait does not apply to the assistant's vector store.

Customizing File Search settings
You can customize how the file_search tool chunks your data and how many chunks it returns to the model context.

Chunking configuration

By default, max_chunk_size_tokens is set to 800 and chunk_overlap_tokens is set to 400, meaning every file is indexed by being split up into 800-token chunks, with 400-token overlap between consecutive chunks.

You can adjust this by setting chunking_strategy when adding files to the vector store. There are certain limitations to chunking_strategy:

max_chunk_size_tokens must be between 100 and 4096 inclusive.
chunk_overlap_tokens must be non-negative and should not exceed max_chunk_size_tokens / 2.
Number of chunks

By default, the file_search tool outputs up to 20 chunks for gpt-4* models and up to 5 chunks for gpt-3.5-turbo. You can adjust this by setting file_search.max_num_results in the tool when creating the assistant or the run.

Note that the file_search tool may output fewer than this number for a myriad of reasons:

The total number of chunks is fewer than max_num_results.
The total token size of all the retrieved chunks exceeds the token "budget" assigned to the file_search tool. The file_search tool currently has a token bugdet of:
4,000 tokens for gpt-3.5-turbo
16,000 tokens for gpt-4* models
Managing costs with expiration policies
The file_search tool uses the vector_stores object as its resource and you will be billed based on the size of the vector_store objects created. The size of the vector store object is the sum of all the parsed chunks from your files and their corresponding embeddings.

You first GB is free and beyond that, usage is billed at $0.10/GB/day of vector storage. There are no other costs associated with vector store operations.

In order to help you manage the costs associated with these vector_store objects, we have added support for expiration policies in the vector_store object. You can set these policies when creating or updating the vector_store object.

python

python
vector_store = client.beta.vector_stores.create_and_poll(
  name="Product Documentation",
  file_ids=['file_1', 'file_2', 'file_3', 'file_4', 'file_5'],
  expires_after={
	  "anchor": "last_active_at",
	  "days": 7
  }
)
Thread vector stores have default expiration policies

Vector stores created using thread helpers (like tool_resources.file_search.vector_stores in Threads or message.attachments in Messages) have a default expiration policy of 7 days after they were last active (defined as the last time the vector store was part of a run).

When a vector store expires, runs on that thread will fail. To fix this, you can simply recreate a new vector_store with the same files and reattach it to the thread.

python

python
all_files = list(client.beta.vector_stores.files.list("vs_expired"))

vector_store = client.beta.vector_stores.create(name="rag-store")
client.beta.threads.update(
    "thread_abc123",
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

for file_batch in chunked(all_files, 100):
    client.beta.vector_stores.file_batches.create_and_poll(
        vector_store_id=vector_store.id, file_ids=[file.id for file in file_batch]
    )
Supported files
For text/ MIME types, the encoding must be one of utf-8, utf-16, or ascii.

FILE FORMAT	MIME TYPE
.c	text/x-c
.cs	text/x-csharp
.cpp	text/x-c++
.doc	application/msword
.docx	application/vnd.openxmlformats-officedocument.wordprocessingml.document
.html	text/html
.java	text/x-java
.json	application/json
.md	text/markdown
.pdf	application/pdf
.php	text/x-php
.pptx	application/vnd.openxmlformats-officedocument.presentationml.presentation
.py	text/x-python
.py	text/x-script.python
.rb	text/x-ruby
.tex	text/x-tex
.txt	text/plain
.css	text/css
.js	text/javascript
.sh	application/x-sh
.ts	application/typescript

Code Interpreter Beta

Code Interpreter allows Assistants to write and run Python code in a sandboxed execution environment. This tool can process files with diverse data and formatting, and generate files with data and images of graphs. Code Interpreter allows your Assistant to run code iteratively to solve challenging code and math problems. When your Assistant writes code that fails to run, it can iterate on this code by attempting to run different code until the code execution succeeds.

See a quickstart of how to get started with Code Interpreter here.

How it works
Code Interpreter is charged at $0.03 per session. If your Assistant calls Code Interpreter simultaneously in two different threads (e.g., one thread per end-user), two Code Interpreter sessions are created. Each session is active by default for one hour, which means that you only pay for one session per if users interact with Code Interpreter in the same thread for up to one hour.

Enabling Code Interpreter
Pass code_interpreter in the tools parameter of the Assistant object to enable Code Interpreter:

python

python
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}]
)
The model then decides when to invoke Code Interpreter in a Run based on the nature of the user request. This behavior can be promoted by prompting in the Assistant's instructions (e.g., “write code to solve this problem”).

Passing files to Code Interpreter
Files that are passed at the Assistant level are accessible by all Runs with this Assistant:

python

python
# Upload a file with an "assistants" purpose
file = client.files.create(
  file=open("mydata.csv", "rb"),
  purpose='assistants'
)

# Create an assistant using the file ID
assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-4o",
  tools=[{"type": "code_interpreter"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [file.id]
    }
  }
)
Files can also be passed at the Thread level. These files are only accessible in the specific Thread. Upload the File using the File upload endpoint and then pass the File ID as part of the Message creation request:

python

python
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",
      "attachments": [
        {
          "file_id": file.id,
          "tools": [{"type": "code_interpreter"}]
        }
      ]
    }
  ]
)
Files have a maximum size of 512 MB. Code Interpreter supports a variety of file formats including .csv, .pdf, .json and many more. More details on the file extensions (and their corresponding MIME-types) supported can be found in the Supported files section below.

Reading images and files generated by Code Interpreter
Code Interpreter in the API also outputs files, such as generating image diagrams, CSVs, and PDFs. There are two types of files that are generated:

Images
Data files (e.g. a csv file with data generated by the Assistant)
When Code Interpreter generates an image, you can look up and download this file in the file_id field of the Assistant Message response:

{
	"id": "msg_abc123",
	"object": "thread.message",
	"created_at": 1698964262,
	"thread_id": "thread_abc123",
	"role": "assistant",
	"content": [
    {
      "type": "image_file",
      "image_file": {
        "file_id": "file-abc123"
      }
    }
  ]
  # ...
}
The file content can then be downloaded by passing the file ID to the Files API:

python

python
from openai import OpenAI

client = OpenAI()

image_data = client.files.content("file-abc123")
image_data_bytes = image_data.read()

with open("./my-image.png", "wb") as file:
    file.write(image_data_bytes)
When Code Interpreter references a file path (e.g., ”Download this csv file”), file paths are listed as annotations. You can convert these annotations into links to download the file:

{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1699073585,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "The rows of the CSV file have been shuffled and saved to a new CSV file. You can download the shuffled CSV file from the following link:\n\n[Download Shuffled CSV File](sandbox:/mnt/data/shuffled_file.csv)",
        "annotations": [
          {
            "type": "file_path",
            "text": "sandbox:/mnt/data/shuffled_file.csv",
            "start_index": 167,
            "end_index": 202,
            "file_path": {
              "file_id": "file-abc123"
            }
          }
          ...
Input and output logs of Code Interpreter
By listing the steps of a Run that called Code Interpreter, you can inspect the code input and outputs logs of Code Interpreter:

python

python
run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)
{
  "object": "list",
  "data": [
    {
      "id": "step_abc123",
      "object": "thread.run.step",
      "type": "tool_calls",
      "run_id": "run_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "step_details": {
        "type": "tool_calls",
        "tool_calls": [
          {
            "type": "code",
            "code": {
              "input": "# Calculating 2 + 2\nresult = 2 + 2\nresult",
              "outputs": [
                {
                  "type": "logs",
                  "logs": "4"
                }
						...
 }
Supported files
FILE FORMAT	MIME TYPE
.c	text/x-c
.cs	text/x-csharp
.cpp	text/x-c++
.doc	application/msword
.docx	application/vnd.openxmlformats-officedocument.wordprocessingml.document
.html	text/html
.java	text/x-java
.json	application/json
.md	text/markdown
.pdf	application/pdf
.php	text/x-php
.pptx	application/vnd.openxmlformats-officedocument.presentationml.presentation
.py	text/x-python
.py	text/x-script.python
.rb	text/x-ruby
.tex	text/x-tex
.txt	text/plain
.css	text/css
.js	text/javascript
.sh	application/x-sh
.ts	application/typescript
.csv	application/csv
.jpeg	image/jpeg
.jpg	image/jpeg
.gif	image/gif
.png	image/png
.tar	application/x-tar
.xlsx	application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
.xml	application/xml or "text/xml"
.zip	application/zip

Function calling Beta

Similar to the Chat Completions API, the Assistants API supports function calling. Function calling allows you to describe functions to the Assistants API and have it intelligently return the functions that need to be called along with their arguments.

Quickstart
In this example, we'll create a weather assistant and define two functions, get_current_temperature and get_rain_probability, as tools that the Assistant can call. Depending on the user query, the model will invoke parallel function calling if using our latest models released on or after Nov 6, 2023. In our example that uses parallel function calling, we will ask the Assistant what the weather in San Francisco is like today and the chances of rain. We also show how to output the Assistant’s response with streaming.

Step 1: Define functions
When creating your assistant, you will first define the functions under the tools param of the assistant.

python

python
from openai import OpenAI
client = OpenAI()
 
assistant = client.beta.assistants.create(
  instructions="You are a weather bot. Use the provided functions to answer questions.",
  model="gpt-4o",
  tools=[
    {
      "type": "function",
      "function": {
        "name": "get_current_temperature",
        "description": "Get the current temperature for a specific location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g., San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["Celsius", "Fahrenheit"],
              "description": "The temperature unit to use. Infer this from the user's location."
            }
          },
          "required": ["location", "unit"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_rain_probability",
        "description": "Get the probability of rain for a specific location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g., San Francisco, CA"
            }
          },
          "required": ["location"]
        }
      }
    }
  ]
)
Step 2: Create a Thread and add Messages
Create a Thread when a user starts a conversation and add Messages to the Thread as the user asks questions.

python

python
thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
  thread_id=thread.id,
  role="user",
  content="What's the weather in San Francisco today and the likelihood it'll rain?",
)
Step 3: Initiate a Run
When you initiate a Run on a Thread containing a user Message that triggers one or more functions, the Run will enter a pending status. After it processes, the run will enter a requires_action state which you can verify by checking the Run’s status. This indicates that you need to run tools and submit their outputs to the Assistant to continue Run execution. In our case, we will see two tool_calls, which indicates that the user query resulted in parallel function calling.

Note that a runs expire ten minutes after creation. Be sure to submit your tool outputs before the 10 min mark.

You will see two tool_calls within required_action, which indicates the user query triggered parallel function calling.

json

json
{
  "id": "run_qJL1kI9xxWlfE0z1yfL0fGg9",
  ...
  "status": "requires_action",
  "required_action": {
    "submit_tool_outputs": {
      "tool_calls": [
        {
          "id": "call_FthC9qRpsL5kBpwwyw6c7j4k",
          "function": {
            "arguments": "{"location": "San Francisco, CA"}",
            "name": "get_rain_probability"
          },
          "type": "function"
        },
        {
          "id": "call_RpEDoB8O0FTL9JoKTuCVFOyR",
          "function": {
            "arguments": "{"location": "San Francisco, CA", "unit": "Fahrenheit"}",
            "name": "get_current_temperature"
          },
          "type": "function"
        }
      ]
    },
    ...
    "type": "submit_tool_outputs"
  }
}
Run object truncated here for readability

How you initiate a Run and submit tool_calls will differ depending on whether you are using streaming or not, although in both cases all tool_calls need to be submitted at the same time. You can then complete the Run by submitting the tool outputs from the functions you called. Pass each tool_call_id referenced in the required_action object to match outputs to each function call.

For the streaming case, we create an EventHandler class to handle events in the response stream and submit all tool outputs at once with the “submit tool outputs stream” helper in the Python and Node SDKs.

python

python
from typing_extensions import override
from openai import AssistantEventHandler
 
class EventHandler(AssistantEventHandler):
    @override
    def on_event(self, event):
      # Retrieve events that are denoted with 'requires_action'
      # since these will have our tool_calls
      if event.event == 'thread.run.requires_action':
        run_id = event.data.id  # Retrieve the run ID from the event data
        self.handle_requires_action(event.data, run_id)
 
    def handle_requires_action(self, data, run_id):
      tool_outputs = []
        
      for tool in data.required_action.submit_tool_outputs.tool_calls:
        if tool.function.name == "get_current_temperature":
          tool_outputs.append({"tool_call_id": tool.id, "output": "57"})
        elif tool.function.name == "get_rain_probability":
          tool_outputs.append({"tool_call_id": tool.id, "output": "0.06"})
        
      # Submit all tool_outputs at the same time
      self.submit_tool_outputs(tool_outputs, run_id)
 
    def submit_tool_outputs(self, tool_outputs, run_id):
      # Use the submit_tool_outputs_stream helper
      with client.beta.threads.runs.submit_tool_outputs_stream(
        thread_id=self.current_run.thread_id,
        run_id=self.current_run.id,
        tool_outputs=tool_outputs,
        event_handler=EventHandler(),
      ) as stream:
        for text in stream.text_deltas:
          print(text, end="", flush=True)
        print()
 
 
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id,
  event_handler=EventHandler()
) as stream:
  stream.until_done()

  Migration Guide Beta
We have changed the way that tools and files work in the Assistants API between the v1 and v2 versions of the beta. Both versions of the beta continue to be accessible via the API today, but we recommend migrating to the newest version of our APIs as soon as feasible. We will deprecate v1 of the beta by the end of 2024.

If you do not use tools or files with the Assistants API today, there should be no changes required for you to migrate from the v1 version to the v2 version of the beta. Simply pass the v2 beta version header and/or move to the latest version of our Node and Python SDKs!

What has changed
The v2 version of the Assistants API contains the following changes:

Tool rename: The retrieval tool has been renamed to the file_search tool
Files belong to tools: Files are now associated with tools instead of Assistants and Messages. This means that:
AssistantFile and MessageFile objects no longer exist.
Instead of AssistantFile and MessageFile, files are attached to Assistants and Threads using the new tool_resources object.
The tool_resources for the code interpreter tool are a list of file_ids.
The tool_resources for the file_search tool are a new object called a vector_stores.
Messages now have an attachments, rather than a file_ids parameter. Message attachments are helpers that add the files to a Thread’s tool_resources.
V1 Assistant
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4-turbo",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [{ "type": "code_interpreter" }],
  "file_ids": [],
  "metadata": {}
}
V2 Assistant
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-4-turbo",
  "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
  "tools": [
    {
      "type": "code_interpreter"
    },
    {
      "type": "file_search"
    }
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_abc"]
    },
    "code_interpreter": {
      "file_ids": ["file-123", "file-456"]
    }
  }
}
Assistants have tools and tool_resources instead of file_ids. The retrieval tool is now the file_search tool. The tool_resource for the file_search tool is a vector_store.

V1 Thread
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699012949,
  "metadata": {}
}
V2 Thread
{
  "id": "thread_abc123",
  "object": "thread",
  "created_at": 1699012949,
  "metadata": {},
  "tools": [
    {
      "type": "file_search"
    },
    {
      "type": "code_interpreter"
    }
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_abc"]
    },
    "code_interpreter": {
      "file_ids": ["file-123", "file-456"]
    }
  }
}
Threads can bring their own tool_resources into a conversation.

V1 Message
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1698983503,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "Hi! How can I help you today?",
        "annotations": []
      }
    }
  ],
  "assistant_id": "asst_abc123",
  "run_id": "run_abc123",
  "metadata": {},
  "file_ids": []
}
V2 Message
{
  "id": "msg_abc123",
  "object": "thread.message",
  "created_at": 1698983503,
  "thread_id": "thread_abc123",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": {
        "value": "Hi! How can I help you today?",
        "annotations": []
      }
    }
  ],
  "assistant_id": "asst_abc123",
  "run_id": "run_abc123",
  "metadata": {},
  "attachments": [
    {
      "file_id": "file-123",
      "tools": [
        { "type": "file_search" },
        { "type": "code_interpreter" }
      ]
    }
  ]
}
Messages have attachments instead of file_ids. attachments are helpers that add files to the Thread’s tool_resources.

All v1 endpoints and objects for the Assistants API can be found under the Legacy section of the API reference.

Accessing v1 data in v2
To make your migration simple between our v1 and v2 APIs, we automatically map AssistantFiles and MessageFiles to the appropriate tool_resources based on the tools that are enabled in Assistants or Runs these files are a part of.

V1 VERSION	V2 VERSION
AssistantFiles for code_interpreter	file_ids on Assistant	Files in an Assistant’s tool_resources.code_interpreter
AssistantFiles for retrieval	file_ids on Assistant	Files in a vector_store attached to an Assistant (tool_resources.file_search)
MessageFiles for code_interpreter	file_ids on Message	Files in an Thread’s tool_resources.code_interpreter
MessageFiles for retrieval	file_ids on Message	Files in a vector_store attached to a Thread (tool_resources.file_search)
It's important to note that while file_ids from v1 are mapped to tool_resources in v2, the inverse is not true. Changes you make to tool_resources in v2 will not be reflected as file_ids in v1.

Because Assistant Files and Message Files are already mapped to the appropriate tool_resources in v2, when you’re ready to migrate to v2 you shouldn't have to worry about a data migration. Instead, you only need to:

Update your integration to reflect the new API and objects. You may need to do things like:
Migrate to creating vector_stores and using file_search, if you were using the retrieval tool. Importantly, since these operations are asynchronous, you’ll want to ensure files are successfully ingested by the vector_stores before creating run.
Migrate to adding files to tool_resources.code_interpreter instead of an Assistant or Message’s files, if you were using the code_interpreter tool.
Migrate to using Message attachments instead of file_ids.
Upgrade to the latest version of our SDKs
Changing beta versions
Without SDKs
Both beta versions can be accessed by passing the right API version header in your API requests:

v1: OpenAI-Beta: assistants=v1
v2: OpenAI-Beta: assistants=v2
v2

v2
curl "https://api.openai.com/v1/assistants" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v2" \
  -d '{
    "instructions": "You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    "name": "Math Tutor",
    "tools": [{"type": "code_interpreter"}],
    "model": "gpt-4-turbo"
  }'
With SDKs
Versions of our SDKs that are released after the release of the v2 beta will have the openai.beta namespace point to the v2 version of the API by default. You can still access the v1 version of the API by using an older version of the SDK (1.20.0 or earlier for python, 4.36.0 or earlier for node) or by overriding the version header.

To install an older version of the SDK, you can use the following commands:

Installing older versions of the SDK
python

python
pip install openai==1.20.0
You can also override this header in a newer SDK version, but we don't recommend this approach since the object types in these newer SDK versions will be different from the v1 objects.

Accessing the `v1` API version in new SDKs
python

python
from openai import OpenAI

client = OpenAI(default_headers={"OpenAI-Beta": "assistants=v1"})
Billing
All vector stores created before the release of the v2 API (April 17, 2024) will be free to use until the end of 2024. This implies that any vector stores that were created as a result of us mapping your v1 data to v2, before the v2 launch will be free. After the end of 2024, they’ll be billed at whatever the fees for vector stores are at that point. See our pricing page for the latest pricing information.

Any vector store that is created before the release of the v2 API (April 17, 2024) but not used in a single Run between that release date and the end of 2024 will be deleted. This is to avoid us starting to bill you for something you created during the beta but never used.

Vector stores created after the release of the v2 API will be billed at current rates as specified on the pricing page.

Deleting files
Deleting Assistant Files / Message Files via the v1 API also removes them from the v2 API. However, the inverse is not true - deletions in the v2 version of the API do not propogate to v1. If you created a file on v1 and would like to "fully" delete a file from your account on both v1 and v2 you should:

delete Assistant Files / Message Files you create using v1 APIs using the v1 endpoints, or
delete the underlying file object — this ensures it is fully removed from all objects in all versions of the API.
Playground
The default playground experience has been migrated to use the v2 version of the API (you will still have a read-only view of the v1 version of objects, but will not be able to edit them). Any changes you make to tools and files via the Playground will only be accessible in the v2 version of the API.

In order to make changes to files in the v1 version of the API, you will need to use the API directly.

GPT Actions
GPT Actions are stored in Custom GPTs, which enable users to customize ChatGPT for specific use cases by providing instructions, attaching documents as knowledge, and connecting to 3rd party services.

GPT Actions empower ChatGPT users to interact with external applications via RESTful APIs calls outside of ChatGPT simply by using natural language. They convert natural language text into the json schema required for an API call. GPT Actions are usually either used to do data retrieval to ChatGPT (e.g. query a Data Warehouse) or take action in another application (e.g. file a JIRA ticket).

How GPT Actions work
At their core, GPT Actions leverage Function Calling to execute API calls.

Similar to ChatGPT's Data Analysis capability (which generates Python code and then executes it), they leverage Function Calling to (1) decide which API call is relevant to the user's question and (2) generate the json input necessary for the API call. Then finally, the GPT Action executes the API call using that json input.

Developers can even specify the authentication mechanism of an action, and the Custom GPT will execute the API call using the third party app’s authentication. GPT Actions obfuscates the complexity of the API call to the end user: they simply ask a question in natural language, and ChatGPT provides the output in natural language as well.

The Power of GPT Actions
APIs allow for interoperability to enable your organization to access other applications. However, enabling users to access the right information from 3rd-party APIs can require significant overhead from developers.

GPT Actions provide a viable alternative: developers can now simply describe the schema of an API call, configure authentication, and add in some instructions to the GPT, and ChatGPT provides the bridge between the user's natural language questions and the API layer.

Simplified example
The getting started guide walks through an example using two API calls from weather.gov to generate a forecast:

/points/{latitude},{longitude} inputs lat-long coordinates and outputs forecast office (wfo) and x-y coordinates
/gridpoints/{office}/{gridX},{gridY}/forecast inputs wfo,x,y coordinates and outputs a forecast
Once a developer has encoded the json schema required to populate both of those API calls in a GPT Action, a user can simply ask "What I should pack on a trip to Washington DC this weekend?" The GPT Action will then figure out the lat-long of that location, execute both API calls in order, and respond with a packing list based on the weekend forecast it receives back.

In this example, GPT Actions will supply api.weather.gov with two API inputs:

/points API call:

{
    "latitude": 38.9072,
    "longitude": -77.0369,
}
/forecast API call:

{
    "wfo": "LWX",
    "x": 97,
    "y": 71,
}
Get started on building
Check out the getting started guide for a deeper dive on this weather example and our actions library for pre-built example GPT Actions of the most common 3rd party apps.

Latency optimization
This guide covers the core set of principles you can apply to improve latency across a wide variety of LLM-related use cases. These techniques come from working with a wide range of customers and developers on production applications, so they should apply regardless of what you're building – from a granular workflow to an end-to-end chatbot!

While there's many individual techniques, we'll be grouping them into seven principles meant to represent a high-level taxonomy of approaches for improving latency.

At the end, we'll walk through an example to see how they can be applied.

The seven principles
Process tokens faster.
Generate fewer tokens.
Use fewer input tokens.
Make fewer requests.
Parallelize.
Make your users wait less.
Don't default to an LLM.
You can use the friendly, catchy acronym PGIRPWD to remember these. (Processing, Generation, Input, Requests, Parallelize, Waiting, Don't)

1. Process tokens faster
Inference speed is probably the first thing that comes to mind when addressing latency (but as you'll see soon, it's far from the only one). This refers to the actual rate at which the LLM processes tokens, and is often measured in TPM (tokens per minute) or TPS (tokens per second).

The main factor that influences inference speed is model size – smaller models usually run faster (and cheaper), and when used correctly can even outperform larger models. To maintain high quality performance with smaller models you can explore:

using a longer, more detailed prompt,
adding (more) few-shot examples, or
fine-tuning / distillation.
DEEP DIVE
Compute capacity & inference optimizations
2. Generate fewer tokens
Generating tokens is almost always the highest latency step when using an LLM: as a general heuristic, cutting 50% of your output tokens may cut ~50% your latency. The way you reduce your output size will depend on output type:

If you're generating natural language, simply asking the model to be more concise ("under 20 words" or "be very brief") may help. You can also use few shot examples and/or fine-tuning to teach the model shorter responses.

If you're generating structured output, try to minimize your output syntax where possible: shorten function names, omit named arguments, coalesce parameters, etc.

Finally, while not common, you can also use max_tokens or stop_tokens to end your generation early.

Always remember: an output token cut is a (milli)second earned!

3. Use fewer input tokens
While reducing the number of input tokens does result in lower latency, this is not usually a significant factor – cutting 50% of your prompt may only result in a 1-5% latency improvement. Unless you're working with truly massive context sizes (documents, images), you may want to spend your efforts elsewhere.

That being said, if you are working with massive contexts (or you're set on squeezing every last bit of performance and you've exhausted all other options) you can use the following techniques to reduce your input tokens:

Fine-tuning the model, to replace the need for lengthy instructions / examples.
Filtering context input, like pruning RAG results, cleaning HTML, etc.
Maximize shared prompt prefix, by putting dynamic portions (e.g. RAG results, history, etc) later in the prompt. This makes your request more KV cache-friendly (which most LLM providers use) and means fewer input tokens are processed on each request. (why?)
4. Make fewer requests
Each time you make a request you incur some round-trip latency – this can start to add up.

If you have sequential steps for the LLM to perform, instead of firing off one request per step consider putting them in a single prompt and getting them all in a single response. You'll avoid the additional round-trip latency, and potentially also reduce complexity of processing multiple responses.

An approach to doing this is by collecting your steps in an enumerated list in the combined prompt, and then requesting the model to return the results in named fields in a JSON. This way you can easily parse out and reference each result!

5. Parallelize
Parallelization can be very powerful when performing multiple steps with an LLM.

If the steps are not strictly sequential, you can split them out into parallel calls. Two shirts take just as long to dry as one.

If the steps are strictly sequential, however, you might still be able to leverage speculative execution. This is particularly effective for classification steps where one outcome is more likely than the others (e.g. moderation).

Start step 1 & step 2 simultaneously (e.g. input moderation & story generation)
Verify the result of step 1
If result was not the expected, cancel step 2 (and retry if necessary)
If your guess for step 1 is right, then you essentially got to run it with zero added latency!

6. Make your users wait less
There's a huge difference between waiting and watching progress happen – make sure your users experience the latter. Here are a few techniques:

Streaming: The single most effective approach, as it cuts the waiting time to a second or less. (ChatGPT would feel pretty different if you saw nothing until each response was done.)
Chunking: If your output needs further processing before being shown to the user (moderation, translation) consider processing it in chunks instead of all at once. Do this by streaming to your backend, then sending processed chunks to your frontend.
Show your steps: If you're taking multiple steps or using tools, surface this to the user. The more real progress you can show, the better.
Loading states: Spinners and progress bars go a long way.
Note that while showing your steps & having loading states have a mostly psychological effect, streaming & chunking genuinely do reduce overall latency once you consider the app + user system: the user will finish reading a response sooner.

7. Don't default to an LLM
LLMs are extremely powerful and versatile, and are therefore sometimes used in cases where a faster classical method would be more appropriate. Identifying such cases may allow you to cut your latency significantly. Consider the following examples:

Hard-coding: If your output is highly constrained, you may not need an LLM to generate it. Action confirmations, refusal messages, and requests for standard input are all great candidates to be hard-coded. (You can even use the age-old method of coming up with a few variations for each.)
Pre-computing: If your input is constrained (e.g. category selection) you can generate multiple responses in advance, and just make sure you never show the same one to a user twice.
Leveraging UI: Summarized metrics, reports, or search results are sometimes better conveyed with classical, bespoke UI components rather than LLM-generated text.
Traditional optimization techniques: An LLM application is still an application; binary search, caching, hash maps, and runtime complexity are all still useful in a world of LLMs.
Example
Let's now look at a sample application, identify potential latency optimizations, and propose some solutions!

We'll be analyzing the architecture and prompts of a hypothetical customer service bot inspired by real production applications. The architecture and prompts section sets the stage, and the analysis and optimizations section will walk through the latency optimization process.

You'll notice this example doesn't cover every single principle, much like real-world use cases don't require applying every technique.

Architecture and prompts
The following is the initial architecture for a hypothetical customer service bot. This is what we'll be making changes to.

Assistants object architecture diagram

At a high level, the diagram flow describes the following process:

A user sends a message as part of an ongoing conversation.
The last message is turned into a self-contained query (see examples in prompt).
We determine whether or not additional (retrieved) information is required to respond to that query.
Retrieval is performed, producing search results.
The assistant reasons about the user's query and search results, and produces a response.
The response is sent back to the user.
Below are the prompts used in each part of the diagram. While they are still only hypothetical and simplified, they are written with the same structure and wording that you would find in a production application.

Places where you see placeholders like "[user input here]" represent dynamic portions, that would be replaced by actual data at runtime.

Query contextualization prompt
Retrieval check prompt
Assistant prompt
Analysis and optimizations
Part 1: Looking at retrieval prompts
Looking at the architecture, the first thing that stands out is the consecutive GPT-4 calls - these hint at a potential inefficiency, and can often be replaced by a single call or parallel calls.

Assistants object architecture diagram

In this case, since the check for retrieval requires the contextualized query, let's combine them into a single prompt to make fewer requests.

Assistants object architecture diagram

Combined query contextualization and retrieval check prompt

Actually, adding context and determining whether to retrieve are very straightforward and well defined tasks, so we can likely use a smaller, fine-tuned model instead. Switching to GPT-3.5 will let us process tokens faster.

Assistants object architecture diagram

Part 2: Analyzing the assistant prompt
Let's now direct our attention to the Assistant prompt. There seem to be many distinct steps happening as it fills the JSON fields – this could indicate an opportunity to parallelize.

Assistants object architecture diagram

However, let's pretend we have run some tests and discovered that splitting the reasoning steps in the JSON produces worse responses, so we need to explore different solutions.

Could we use a fine-tuned GPT-3.5 instead of GPT-4? Maybe – but in general, open-ended responses from assistants are best left to GPT-4 so it can better handle a greater range of cases. That being said, looking at the reasoning steps themselves, they may not all require GPT-4 level reasoning to produce. The well defined, limited scope nature makes them and good potential candidates for fine-tuning.

{
"message_is_conversation_continuation": "True", // <-
"number_of_messages_in_conversation_so_far": "1", // <-
"user_sentiment": "Aggravated", // <-
"query_type": "Hardware Issue", // <-
"response_tone": "Validating and solution-oriented", // <-
"response_requirements": "Propose options for repair or replacement.", // <-
"user_requesting_to_talk_to_human": "False", // <-
"enough_information_in_context": "True" // <-
"response": "..." // X -- benefits from GPT-4
}
This opens up the possibility of a trade-off. Do we keep this as a single request entirely generated by GPT-4, or split it into two sequential requests and use GPT-3.5 for all but the final response? We have a case of conflicting principles: the first option lets us make fewer requests, but the second may let us process tokens faster.

As with many optimization tradeoffs, the answer will depend on the details. For example:

The proportion of tokens in the response vs the other fields.
The average latency decrease from processing most fields faster.
The average latency increase from doing two requests instead of one.
The conclusion will vary by case, and the best way to make the determiation is by testing this with production examples. In this case let's pretend the tests indicated it's favorable to split the prompt in two to process tokens faster.

Assistants object architecture diagram

Note: We'll be grouping response and enough_information_in_context together in the second prompt to avoid passing the retrieved context to both new prompts.

Assistants prompt - reasoning
Assistants prompt - response

In fact, now that the reasoning prompt does not depend on the retrieved context we can parallelize and fire it off at the same time as the retrieval prompts.

Assistants object architecture diagram

Part 3: Optimizing the structured output
Let's take another look at the reasoning prompt.

Assistants object architecture diagram

Taking a closer look at the reasoning JSON you may notice the field names themselves are quite long.

{
"message_is_conversation_continuation": "True", // <-
"number_of_messages_in_conversation_so_far": "1", // <-
"user_sentiment": "Aggravated", // <-
"query_type": "Hardware Issue", // <-
"response_tone": "Validating and solution-oriented", // <-
"response_requirements": "Propose options for repair or replacement.", // <-
"user_requesting_to_talk_to_human": "False", // <-
}
By making them shorter and moving explanations to the comments we can generate fewer tokens.

{
"cont": "True", // whether last message is a continuation
"n_msg": "1", // number of messages in the continued conversation
"tone_in": "Aggravated", // sentiment of user query
"type": "Hardware Issue", // type of the user query
"tone_out": "Validating and solution-oriented", // desired tone for response
"reqs": "Propose options for repair or replacement.", // response requirements
"human": "False", // whether user is expressing want to talk to human
}
Assistants object architecture diagram

This small change removed 19 output tokens. While with GPT-3.5 this may only result in a few millisecond improvement, with GPT-4 this could shave off up to a second.

Assistants object architecture diagram

You might imagine, however, how this can have quite a significant impact for larger model outputs.

We could go further and use single chatacters for the JSON fields, or put everything in an array, but this may start to hurt our response quality. The best way to know, once again, is through testing.

Example wrap-up
Let's review the optimizations we implemented for the customer service bot example:

Assistants object architecture diagram

Combined query contextualization and retrieval check steps to make fewer requests.
For the new prompt, switched to a smaller, fine-tuned GPT-3.5 to process tokens faster.
Split the assistant prompt in two, switching to a smaller, fine-tuned GPT-3.5 for the reasoning, again to process tokens faster.
Parallelized the retrieval checks and the reasoning steps.
Shortened reasoning field names and moved comments into the prompt, to generate fewer tokens.
Conclusion
You should now be familiar with the core set of principles you can use to improve latency in your LLM application. As you explore these techniques, always remember to measure where your latency is coming from, and test the impact of each solution your try. Now go make your application fly!





