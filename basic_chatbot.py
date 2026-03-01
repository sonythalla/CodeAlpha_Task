def codealpha_chatbot():
    print("Hello! I am CodeAlpha Internship Bot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == "quit":
            print("Bot: Goodbye! Best of luck with your Python journey at CodeAlpha!")
            break
        
        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! Welcome to CodeAlpha Python Internship support.")
        
        elif "tasks" in user_input or "assignments" in user_input:
            print("Bot: During the internship, you'll work on Python tasks like building small projects, automation scripts, and data manipulation exercises.")
        
        elif "skills" in user_input:
            print("Bot: Make sure you are familiar with Python basics, loops, functions, file handling, and simple data structures.")
        
        elif "duration" in user_input:
            print("Bot: The CodeAlpha Python internship usually lasts 1-3 months depending on your performance and project completion.")
        
        elif "tips" in user_input:
            print("Bot: Focus on writing clean code, understanding logic, and completing small projects. Practice Python coding daily!")
        
        elif "example project" in user_input:
            print("Bot: Example projects include a Hangman game, stock portfolio tracker, or automation scripts for file management.")
        
        else:
            print("Bot: I can help with internship-related queries. Ask me about tasks, skills, duration, tips, or example projects.")

# Run the chatbot
codealpha_chatbot()
