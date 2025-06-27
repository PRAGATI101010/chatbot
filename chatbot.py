def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input:
            print("Chatbot: Hi!")
        elif "how are you" in user_input:
            print("Chatbot: I'm fine, thanks!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()