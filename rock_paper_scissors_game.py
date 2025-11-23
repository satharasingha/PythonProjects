import random

while True:
    user_input = input("Rock, Paper or Scissors? (r/p/s or q to quit): ").lower()

    if user_input == "q":
        print("Thanks for playing!")
        break

    if user_input not in ['r', 'p', 's']:
        print("Invalid choice, please type r, p, or s.")
        continue

    computer_choice = random.choice(['r', 'p', 's'])

    if user_input == "r":
        if computer_choice == "r":
            print("Computer chose Rock — It's a tie!")
        elif computer_choice == "p":
            print("Computer chose Paper — You lose!")
        else:
            print("Computer chose Scissors — You win!")

    elif user_input == "p":
        if computer_choice == "p":
            print("Computer chose Paper — It's a tie!")
        elif computer_choice == "s":
            print("Computer chose Scissors — You lose!")
        else:
            print("Computer chose Rock — You win!")

    elif user_input == "s":
        if computer_choice == "s":
            print("Computer chose Scissors — It's a tie!")
        elif computer_choice == "r":
            print("Computer chose Rock — You lose!")
        else:
            print("Computer chose Paper — You win!")

    print()  # Blank line for readability
