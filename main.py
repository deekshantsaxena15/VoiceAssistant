import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import webbrowser
from datetime import datetime


# Set up speech recognition
recognizer = sr.Recognizer()

# Set up text-to-speech
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    print("Listening...")

    audio = sd.rec(
        int(5 * 16000),
        samplerate=16000,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    print("Recording completed!")
    print("Converting speech to text...")

    audio_bytes = audio.tobytes()

    audio_data = sr.AudioData(
        audio_bytes,
        16000,
        2
    )

    try:
        text = recognizer.recognize_google(audio_data)

        print("You:", text)

        return text.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you.")
        return ""

    except sr.RequestError:
        speak("Sorry, I could not connect to the speech recognition service.")
        return ""


print("Voice Assistant started!")
speak("Hello, I am your voice assistant. How can I help you?")

command = listen()


if "youtube" in command:
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

elif "google" in command:
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

elif "time" in command:
    current_time = datetime.now().strftime("%I:%M %p")
    speak("The current time is " + current_time)

else:
    speak("Sorry, I don't know how to do that yet.")