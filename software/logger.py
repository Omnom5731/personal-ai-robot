def log_conversation(user_input, ai_reply):
    with open("conversation_log.txt", "a") as f:
        f.write(f"User: {user_input}\nAI: {ai_reply}\n---\n")
