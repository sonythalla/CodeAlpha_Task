import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "codealpha"]

# Randomly choose a word
word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("_ " * len(word))

while attempts > 0:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")

    # Show the current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word correctly!")
        break
else:
    print(f"\nGame Over! The word was '{word}'.")
