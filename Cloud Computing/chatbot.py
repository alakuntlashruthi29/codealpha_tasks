print("Welcome to the Basic Chatbot!")
print("Type 'bye' to exit the chat.")

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I'm fine, thanks!")

    elif user == "what is your name":
        print("Bot: I am a simple chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")