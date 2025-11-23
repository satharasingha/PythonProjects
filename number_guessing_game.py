import random

number = random.randint(1, 10)

while True:
    try:
        guesses = int(input("Guess the number between 1 and 10: "))

        if guesses < number:
            print("Too low")

        elif guesses > number:
            print("Too high")

        else:
            print("You won!")
            break

    except ValueError:
        print("Enter a valid number")

print("Your guess was:", guesses)
