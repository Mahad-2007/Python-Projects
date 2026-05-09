
import datetime
import random



name = input("Enter your name: ")

present_hour = datetime.datetime.now().hour

if 5 <= present_hour < 12:
    print(f"\nGood Morning, {name}")
elif 12 <= present_hour < 17:
    print(f"\nGood Afternoon, {name}")
elif 17 <= present_hour < 21:
    print(f"\nGood Evening, {name}")
else:
    print(f"\nGood Night, {name}")


print("\nWelcome to Smart AI ChatBot")
print("Type 'bye' anytime to exit.\n")


responses = {

    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Nice to meet you.",
    "hey": "Hey! What's going on?",
    "good morning": "Good morning! Hope you have a wonderful day.",
    "good afternoon": "Good afternoon! How is your day going?",
    "good evening": "Good evening! Hope you're doing great.",
    "salam": "Walikum Salam!",
    "how are you": "I am fine. Thanks for asking!",
    "what is your name": "My name is Smart AI ChatBot.",
    "who made you": "I was created using Python programming.",
    "where are you from": "I belong to the AI world.",
    "nice": "Glad you liked it!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "bye": "Goodbye! Have a great day.",

    "what can you do": "I can chat with you and answer simple questions.",
    "are you real": "No, I am a virtual chatbot.",
    "do you sleep": "No, I work 24/7.",
    "are you human": "No, I am an AI chatbot.",
    "what is python": "Python is a powerful and beginner-friendly programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that learns from data.",
    "what is data science": "Data Science is the process of analyzing and understanding data.",
    "what is pandas": "Pandas is a Python library used for data analysis.",
    "what is numpy": "NumPy is a Python library used for numerical operations.",
    "what is github": "GitHub is a platform used to store and manage code.",
    "what is coding": "Coding means writing instructions for computers.",
    "what is programming": "Programming is the process of creating software using code.",

    "tell me a joke": "Why do programmers hate nature? Because it has too many bugs!",
    "do you like music": "Yes! Music is relaxing.",
    "your favorite color": "I like blue because it looks cool.",
    "your favorite food": "I don't eat food, but pizza looks delicious.",
    "do you play games": "I like talking about games!",
    "can you dance": "Only digitally!",
    "can you sing": "I can sing in binary language.",

    "i am tired": "Take a short break and refresh your mind.",
    "i am sad": "Everything will get better. Stay positive!",
    "motivate me": "Success comes from consistency and hard work.",
    "i want to learn python": "Start with basics like variables, loops, and functions.",
    "how to become programmer": "Practice coding daily and build projects.",
    "how to improve coding": "Solve problems and create projects regularly.",
    "how to focus": "Avoid distractions and study in small sessions.",
    "exam": "Prepare smartly and revise regularly.",
    "career": "Choose a career that matches your passion and skills.",

    "what is laptop": "A laptop is a portable computer.",
    "what is internet": "The internet connects computers around the world.",
    "what is software": "Software is a program that runs on computers.",
    "what is hardware": "Hardware means physical computer components.",
    "what is operating system": "An operating system manages computer resources.",
    "what is windows": "Windows is an operating system developed by Microsoft.",
    "what is linux": "Linux is a powerful open-source operating system.",

    "weather": "I cannot check live weather right now.",
    "time": "Use your system clock to check the current time.",
    "date": "You can check today's date from your device.",
    "your age": "AI chatbots don't have real age.",
    "do you study": "I learn from data and programming.",
    "are you smart": "I try my best to help users.",
    "can you help me": "Of course! Ask me anything.",
    "good job": "Thank you! That means a lot.",
    "awesome": "Glad you think so!",
    "cool": "Nice"
}


def get_response(user_question):

    user_question = user_question.lower()

    for key in responses:
        if key in user_question:
            return responses[key]

    unknown_responses = [
        "Sorry, I don't understand that yet.",
        "Can you ask something else?",
        "Interesting question!",
        "I am still learning new things.",
        "Please try asking differently."
    ]

    return random.choice(unknown_responses)

while True:

    user_input = input("\nYou: ")

    reply = get_response(user_input)

    print("Bot:", reply)

    if "bye" in user_input.lower():
        break