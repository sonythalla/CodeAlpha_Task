import random

def hangman():
    print("Welcome to Hangman! Guess the word before you run out of attempts.\n")
    
    # List of words (you can add more)
    words = ["python", "internship", "codealpha", "developer", "function", "variable"]
    
    # Select a random word
    word = random.choice(words)
    word_letters = list(word)
    guessed_letters = ["_"] * len(word)
    
    attempts = 6  # Number of wrong guesses allowed
    tried_letters = []
    
    while attempts > 0 and "_" in guessed_letters:
        print("Word:", " ".join(guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        
        if guess in tried_letters:
            print("You already tried that letter.\n")
            continue
        
        tried_letters.append(guess)
        
        if guess in word_letters:
            for idx, letter in enumerate(word_letters):
                if letter == guess:
                    guessed_letters[idx] = guess
            print("Good guess!\n")
        else:
            attempts -= 1
            print("Wrong guess!\n")
    
    # Game over
    if "_" not in guessed_letters:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

# Run the Hangman game
hangman()
