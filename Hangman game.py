import random

# List of 5 predefined words
word_list = ["apple", "tiger", "chair", "bread", "robot"]

# Choose a random word from the list
secret_word = random.choice(word_list)

# Displayed word (with underscores)
display_word = ["_"] * len(secret_word)

# Track guessed letters and number of incorrect guesses
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses. Let's begin!\n")

# Game loop
while incorrect_guesses < max_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical character.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Incorrect guess.\n")
        incorrect_guesses += 1

# Game result
if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you've run out of guesses. The word was:", secret_word)
