# Voice Assistant

A Python-based voice assistant that captures voice input, converts speech to text, processes spoken commands, performs actions, and responds using text-to-speech.

## Features

- Voice input using SoundDevice
- Speech recognition using SpeechRecognition
- Text-to-speech using pyttsx3
- Greeting when the assistant starts
- Opens Google
- Opens YouTube
- Searches Google using voice commands
- Searches YouTube using voice commands
- Tells the current time
- Tells the current date
- Continuous voice command processing
- Handles unrecognized speech gracefully
- Handles speech recognition service errors
- Exit command to stop the assistant

## Technologies Used

- Python
- SpeechRecognition
- SoundDevice
- pyttsx3
- Webbrowser
- Datetime
- urllib.parse

## How It Works

The assistant follows these steps:

1. Records audio from the microphone.
2. Converts the recorded audio into audio data.
3. Sends the audio data to Google's speech recognition service.
4. Converts the recognized speech into text.
5. Processes the spoken command.
6. Performs the requested action.
7. Responds using text-to-speech.

## Example Commands

You can say:

- "Hello"
- "Open YouTube"
- "Open Google"
- "Search Google for Python tutorials"
- "Search YouTube for machine learning"
- "What is the time?"
- "What is today's date?"
- "Exit"

## Installation

Clone the repository:

```bash
git clone https://github.com/deekshantsaxena15/VoiceAssistant.git