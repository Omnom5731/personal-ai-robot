from gtts import gTTS
from pydub import AudioSegment
import os

def speak(text):
    print(f"Speaking: {text}")
    try:
        tts = gTTS(text)
        tts.save("reply.mp3")
        AudioSegment.from_mp3("reply.mp3").export("reply.wav", format="wav")
        os.system("aplay -D plughw:3,0 reply.wav")
    except Exception as e:
        print(f"Speech output failed: {e}")
