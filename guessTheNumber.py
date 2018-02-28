# This is number guessing game

import random

secretNumber = random.randint(1, 20)
print("I'm guessing a number between 1 and 20. You're gonna have seven tries to be able to guess it")

# Ask the user for a number

for guessesTaken in range(1, 7):
    print("Take a guess")
    guessedNumber = int(input())

    if guessedNumber < secretNumber:
        print("Your guess is too low.")
    elif guessedNumber > secretNumber:
        print("Your guess is too high.")
    else:
        break    # this condition means correct guess!


if guessedNumber == secretNumber:
    print("Good job! You've guessed correctly in " + str(guessesTaken) + " tries...")
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))