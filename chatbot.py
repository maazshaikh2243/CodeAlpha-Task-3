def chatbot_response(user_input):    
    responses = {
        "hi": "Hello! How can I assist you today?",
        "hello": "Hi there! Feel free to ask me anything.",
        "how are you": "I'm just a program, but I'm here to help you!",
        "what is your name": "I am Chatbot 1.0, your virtual assistant.",
        "what is python": "Python is a popular programming language known for its simplicity and versatility.",
        "who created you": "I was created by a programmer, just like how apps are built.",
        "bye": "Goodbye! Have a great day!",
    }

    return responses.get(user_input.lower(), "I'm sorry, I don't have an answer to that. Can you ask something else?")

if __name__ == "__main__":
    print("Chatbot: Hi! I am your chatbot. Ask me anything. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
