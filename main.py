import speech_recognition as sr
import pyttsx3
import roku

# Replace with your Roku's IP address
roku_ip = "192.168.1.136"
roku_client = roku.Roku(roku_ip)

# Set up the speech recognition engine
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()


# Function to speak the given text
def speak(command):
    engine.say(command)
    engine.runAndWait()


# Define the voice commands
commands = {
    "turn on": roku_client.power_on,
    "turn off": roku_client.power_off,
    "volume up": roku_client.volume_up,
    "volume down": roku_client.volume_down,
    "mute": roku_client.volume_mute,
    "open Netflix": lambda: roku_client.launch_app("Netflix"),
    "open Hulu": lambda: roku_client.launch_app("Hulu"),
    "play": roku_client.play,
    "pause": roku_client.pause,
    "rewind": roku_client.rewind,
    "fast forward": roku_client.fast_forward,
}


# Continuously listen for voice commands
def recognize_and_speak():
    while True:

        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

            try:
                # Recognize the speech using Google Speech Recognition
                command = r.recognize_google(audio).lower()
                print(f"You said: {command}")

                # Execute the corresponding command
                if command in commands:
                    speak(command)

                else:
                    print("Sorry, I didn't understand that.")

            except sr.UnknownValueError:
                print("Sorry, I didn't understand that.")


# Start live speech recognition and speech output
if __name__ == '__main__':
    recognize_and_speak()
