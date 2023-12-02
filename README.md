# S.U.N.D.A.Y Assistant

AI assistant that run the code that you indicate with your voice.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact Information](#contact-information)
- [FAQs](#faqs)
- [Examples/Demo](#examplesdemo)
- [Roadmap](#roadmap)
- [Security](#security)
- [Dependencies](#dependencies)

## Description

This project is a Ai assistant called Sunday, that help you to run Python functions using only your voice as input, the project use Open Ai Whisper model to translate the waveform audio to text, and then the text combined with the json description of your functions, is given to the Gorilla Model, to return a text with the name of function and their parameters, using this information, Python evaluate the given function in the context of globals and locals, finally if the function exists, Python run it.

## Installation

For the moment the installation procces is very easy:
1. Go to the code button
2. Select if you want to clone the project with Github or Download the ZIP folder.
3. Open the project with your favorite code editor or IDE (In my case I use Visual Studio Code)
4. Import the necessary libraries
5. Run the command 
`gradio main.py` 
or 
`python3 main.py`
6. Enjoy!

## Usage

When start the main file, click the button "Record" to start recording your command, then when you finish, click the "Record" button again and when the program finsih to process the data, will execute your code.

## Features

- AI Assitant
- Record microphone
- Large Language Model
- API Usage
- LangChain

## Documentation

COMING SOON!

## Contributing

COMING SOON!

## Credits

- https://huggingface.co/openai/whisper-small The OpenAI whisper model
- https://huggingface.co/TheBloke/gorilla-openfunctions-v1-GGUF The Gorilla Model
- https://www.gradio.app/ For the Gradio interface
- https://python.langchain.com/

## License

Project under the Apache License 2.0.

## Contact Information

Gmail: thekingmarco03@gmail.com
Instagram: https://www.instagram.com/titancloudofficial/

## FAQs

Make your question and they will be posted here.

## Examples/Demo

COMING SOON!

## Roadmap

The future plans for the Ai Assistant are:

- Remove the need of use a button to record the user voice
- The assistant must be able to recognize when the user call her, and then start to record the voice
- Enlarge the functions and capabilities of the assistant for example, call people, make emails, home automation
- Make the assistant faster to be able to doing the speech recognition and text generation in a few seconds 
- Make the assistant can work anywhere and anytime with a web version 
- Make the assistant can run natively in edge devices

This plan will be updated with new steps, or modify the previous ones.

## Security

Any information regarding security vulnerabilities, please write to the email: thekingmarco03@gmail.com.

## Dependencies

- [OpenAI Whisper Model](https://huggingface.co/openai/whisper-small)
    - Description: The OpenAI whisper model for natural language processing.

- [Gorilla Model](https://huggingface.co/TheBloke/gorilla-openfunctions-v1-GGUF)
    - Description: The Gorilla model for specific tasks.

- [Gradio](https://www.gradio.app/)
    - Description: Gradio is an easy-to-use UI library for machine learning models.

- [Langchain Python Library](https://python.langchain.com/)
    - Description: The Langchain Python library for language-related functionalities.