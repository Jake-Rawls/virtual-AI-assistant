import speech_recognition as sr
from roku import Roku

roku = Roku('192.168.1.218')

r = sr.Recognizer()

def process_command(command):
    command = command.lower()

    if 'power on' in command:
        roku.poweron()
    elif 'power off' in command:
        roku.poweroff()
    elif 'home' in command:
        roku.home()
    elif 'volume up' in command:
        roku.volume_up()
    elif 'volume down' in command:
        roku.volume_down()
    elif 'mute' in command:
        roku.volume_mute()
    elif 'unmute' in command:
        roku.volume_mute()
    elif 'up' in command:
        roku.up()
    elif 'down' in command:
        roku.down()
    elif 'left' in command:
        roku.left()
    elif 'right' in command:
        roku.right()
    elif 'select' in command:
        roku.select()
    elif 'netflix' in command:
        app = roku['Netflix']
        app.launch()
    elif 'peacock' in command:
        app = roku['593099']
        app.launch()
    elif 'hulu' in command:
        app = roku['2285']
        app.launch()
    elif 'xbox' in command:
        app = roku['tvinput.hdmi1']
        app.launch()
    else:
        print("Command not recognized.")

while True:
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            process_command(command)
        except sr.UnknownValueError:
            pass