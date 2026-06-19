chat_history = []

def add_message(role, message):
    chat_history.append({
        "role": role,
        "message": message
    })

def get_history():
    return chat_history