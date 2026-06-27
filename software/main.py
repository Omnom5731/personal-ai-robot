import logger
from voice_input import listen_command
from gtts import gTTS
from pydub import AudioSegment
import os
import ai_response
import re

def clean_text_for_speech(text: str) -> str:
    cleaned = re.sub(r"[*_`#>~^]", "", text)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned

def speak(text):
    print(f"Speaking: {text}")
    try:
        tts = gTTS(text)
        tts.save("reply.mp3")
        AudioSegment.from_mp3("reply.mp3").export("reply.wav", format="wav")
        os.system("aplay -D plughw:3,0 reply.wav")
    except Exception as e:
        print(f"Speech output failed: {e}")

def main():
    print("System initialized. Waiting for wake word...")
    while True:
        command = listen_command().strip()
        if not command:
            continue

        print(f"You said: {command}")
        reply = ai_response.get_ai_reply(command)
        print(f"AI Reply: {reply}")

        logger.log_conversation(command, reply)

        reply = clean_text_for_speech(reply)
        speak(reply)

if __name__ == "__main__":
    main()
