Voice Assistant

A simple desktop voice assistant built in Python. It listens for a spoken command, converts it to text with Google's speech recognition API, and performs one of a small set of actions: web search (Google/YouTube), opening a site, or telling the current date/time.

Features
Voice input via microphone (sounddevice) and speech-to-text (speech_recognition, Google Web Speech API)
Text-to-speech responses (pyttsx3)
Commands:
"search google for <query>" / "search youtube for <query>"
"open google" / "open youtube"
"what's the date" / "what's the time"
"exit" / "quit" / "stop" / "goodbye" to end the session
Session history log printed at the end of each run
Regex-based query extraction (robust to phrases like "search for cats and dogs on youtube", where a naive word-by-word approach would break)
Requirements
pip install SpeechRecognition sounddevice pyttsx3

You'll also need a working microphone and speakers, and an internet connection (speech recognition calls Google's API over HTTP).

Usage
python voice_assistant.py

Speak a command after "Listening..." appears. Each recording window is 5 seconds by default — this can be changed via VoiceAssistant(listen_seconds=...) in main().

Design notes
VoiceAssistant class: groups the recognizer, TTS engine, config, and command history together instead of relying on module-level globals. Makes it straightforward to unit test extract_query() and handle_command() independently of the microphone.
Query extraction: three regex patterns are tried in order (most specific first) to pull the actual search phrase out of a raw command, rather than stripping fixed keywords like "search", "for", "on" from anywhere in the string — the latter approach corrupts queries that happen to contain those words.
Fixed 5-second recording window: chosen for simplicity. It means short commands have dead air at the end and long ones can get cut off — see "Future improvements" below.
Known limitations / future improvements
Fixed-length recording instead of voice activity detection (VAD). Right now every command listens for exactly listen_seconds, regardless of how long the person actually spoke. A better version would detect silence and stop recording automatically (e.g. using webrtcvad or streaming recognition), which would feel more natural and avoid cutting off longer commands.
No wake word. The assistant is always listening in a loop rather than waiting for a trigger phrase like "Hey Assistant." Adding one (e.g. via porcupine or a simple keyword-spotting pass) would make it usable in the background without constantly recording.
Single recognized command per action. Commands aren't chainable ("search google for cats and then open youtube"), and there's no way to correct a misheard command without repeating it.
Cloud dependency for recognition. recognize_google requires internet access and sends audio to Google's servers. An offline option (e.g. Vosk or whisper.cpp) would remove that dependency and improve privacy.
No persistent memory across runs. The session history resets every time the script restarts; saving it to a file would let the assistant reference past commands.
