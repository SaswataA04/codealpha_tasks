import random


word_list = ["applepie", "mangojuice", "grapevine", "peach", "lemontree"]


secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print(" Welcome to Hangman!")
print("_ " * len(secret_word))

while incorrect_guesses < max_guesses:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Correct!")
    else:
        incorrect_guesses += 1
        print(f" Incorrect! You have {max_guesses - incorrect_guesses} guesses left.")

    current_status = ""
    for letter in secret_word:
        if letter in guessed_letters:
            current_status += letter + " "
        else:
            current_status += "_ "
    print("\nWord:", current_status.strip())

    if all(letter in guessed_letters for letter in secret_word):
        print("\n Congratulations! You guessed the word:", secret_word)
        break

if incorrect_guesses == max_guesses:
    print("\n Game Over! The word was:", secret_word)
