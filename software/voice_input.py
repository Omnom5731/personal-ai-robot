import speech_recognition as sr
import subprocess
import time

def listen_command():
    recognizer = sr.Recognizer()
    mic_index = 2  # Update this based on your mic index

    print("System initialized. Waiting for wake word...")

    while True:
        print("Listening for wake word...")
        audio_data = record_audio(duration=5)
        text = recognize_speech(audio_data)

        if text and "robot" in text.lower():
            print("Wake word detected!")
            respond_to_wake_word()
            print("Listening for command...")
            command_audio = record_audio(duration=6)
            command_text = recognize_speech(command_audio)
            if command_text:
                print(f"Recognized: {command_text}")
                return command_text
            else:
                print("No command detected, waiting again...")
        else:
            print("Wake word not detected, retrying...")
            time.sleep(1)

def record_audio(duration=5):
    filename = "temp.wav"
    cmd = ["arecord", "-D", "plughw:2,0", "-f", "cd", "-t", "wav", "-d", str(duration), filename]
    subprocess.run(cmd, check=True)
    return filename

def recognize_speech(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""

def respond_to_wake_word():
    print("Speaking: Yes? How can I help you?")
    os.system("aplay -D plughw:3,0 /usr/share/sounds/alsa/Front_Center.wav")
