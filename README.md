# CodeAlpha-Task-3
Chatbot 1.0
This is a simple chatbot program written in Python. It provides predefined responses to user inputs using a dictionary-based approach. The chatbot is an interactive tool for learning the basics of Python programming and chatbot logic.

Features:
User Interaction: The chatbot interacts with users via simple text-based inputs and outputs.
Predefined Responses: It has a set of pre-programmed responses for common inputs such as greetings and basic questions.
Fallback Mechanism: If the user input doesn't match any predefined response, the chatbot provides a default message.
Exit Option: Users can exit the chatbot interaction by typing "bye."

How It Works:
Main Loop: The program runs in a loop, allowing continuous interaction until the user types "bye."
Input Handling: User input is read, converted to lowercase, and matched with predefined keys in the responses dictionary.
Response Generation: If the input matches a key in the dictionary, the corresponding response is returned. If no match is found, a default fallback response is given.

Installation:
Make sure you have Python installed on your computer (version 3.x is recommended).
Download or clone this repository to your local machine.

Usage:
Navigate to the directory where the script is located.
Run the script using the following command:
python chatbot.py
Interact with the chatbot by typing your questions or messages. For example:
You: hi
Chatbot: Hello! How can I assist you today?
To exit the chatbot, type bye.

Example Questions:
Here are some questions you can try with the chatbot:
hi
how are you
what is your name
what is python
who created you
Customization
You can expand the chatbot by adding more responses to the responses dictionary in the chatbot_response function. For example:

Learning Objective:
This project is designed for students who want to learn:
Basic Python programming concepts.
How to use dictionaries for mapping inputs to outputs.
How to create simple interactive programs.

Limitations:
The chatbot only supports predefined responses. It doesn't learn or adapt.
Input must match the predefined phrases to trigger a specific response.

Contribution:
Feel free to contribute by improving the code, adding more features, or suggesting ideas! 😊
