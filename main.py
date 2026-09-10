import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import webbrowser
from datetime import datetime
from urllib.parse import quote


# Set up speech recognition
recognizer = sr.Recognizer()
recognizer.operation_timeout = 10

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
        speak("Sorry, I could not understand you. Please try again.")
        return ""

    except sr.RequestError:
        speak("Sorry, the speech recognition service is unavailable.")
        return ""

    except Exception as error:
        print("Error:", error)
        speak("Something went wrong while processing your voice.")
        return ""


def search_google(query):
    url = "https://www.google.com/search?q=" + quote(query)
    webbrowser.open(url)


def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + quote(query)
    webbrowser.open(url)


def extract_search_query(command):
    query = command

    words_to_remove = [
        "can you",
        "could you",
        "please",
        "i want you to",
        "i want to",
        "search",
        "find",
        "look up",
        "look for",
        "search for",
        "google",
        "youtube",
        "on",
        "for"
    ]

    for word in words_to_remove:
        query = query.replace(word, " ")

    query = " ".join(query.split())

    return query.strip()


def handle_command(command):

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")
        return True

    # Exit assistant
    if any(word in command for word in [
        "exit",
        "quit",
        "stop",
        "goodbye"
    ]):
        speak("Goodbye!")
        return False

    # Google search
    if "google" in command and any(word in command for word in [
        "search",
        "find",
        "look up",
        "look for"
    ]):
        query = extract_search_query(command)

        if query:
            speak("Searching Google for " + query)
            search_google(query)
        else:
            speak("What would you like me to search for?")

        return True

    # YouTube search
    if "youtube" in command and any(word in command for word in [
        "search",
        "find",
        "look up",
        "look for"
    ]):
        query = extract_search_query(command)

        if query:
            speak("Searching YouTube for " + query)
        else:
            speak("What would you like me to search for?")

        return True

    # Open YouTube
    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        return True

    # Open Google
    if "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return True

    # Tell the date
    if "date" in command or "today" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + current_date)
        return True

    # Tell the time
    if "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)
        return True

    # Unknown command
    if command:
        speak("Sorry, I don't know how to do that yet.")

    return True


print("Voice Assistant started!")

speak("Hello, I am your voice assistant. How can I help you?")


while True:
    command = listen()

    if not handle_command(command):
        break