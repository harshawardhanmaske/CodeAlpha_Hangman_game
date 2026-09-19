import random

words = ["python", "computer", "programming", "developer", "college"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display = ["_"] * len(word)

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong and "_" in display:

    print("\nWord:", " ".join(display))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
