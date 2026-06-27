import os
from dotenv import load_dotenv
from google import genai

load_dotenv("/home/pi/robot/.env")

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set. Add it to .env or export it.")

client = genai.Client(api_key=API_KEY)

CONVERSATION_HISTORY = []
MAX_MEMORY = 5

def build_context(prompt: str) -> str:
    memory_text = ""
    for user, bot in CONVERSATION_HISTORY[-MAX_MEMORY:]:
        memory_text += f"User: {user}\nRobot: {bot}\n"
    memory_text += f"User: {prompt}\nRobot:"
    return memory_text

def get_ai_reply(prompt: str) -> str:
    global CONVERSATION_HISTORY
    try:
        context = (
            "You are a helpful, conversational voice assistant robot named Robot. "
            "Keep your replies concise and natural.\n\n"
            + build_context(prompt)
        )
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=context
        )
        reply = response.text.strip()
        CONVERSATION_HISTORY.append((prompt, reply))
        if len(CONVERSATION_HISTORY) > MAX_MEMORY:
            CONVERSATION_HISTORY.pop(0)
        return reply
    except Exception as e:
        print(f"⚠️ AI request failed: {e}")
        return "Sorry, I’m having trouble connecting to the AI service right now."
