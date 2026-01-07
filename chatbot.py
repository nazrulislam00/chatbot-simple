def get_response(message):
    message = message.lower()

    if "hello" in message:
        return "Hello! How can I help you?"
    if "name" in message:
        return "I am a simple chatbot."
    if "bye" in message:
        return "Goodbye!"
    return "Sorry, I did not understand."

if __name__ == "__main__":
    print("Chatbot started (type 'bye' to exit)")
    while True:
        user = input("You: ")
        reply = get_response(user)
        print("Bot:", reply)
        if "bye" in user.lower():
            break
