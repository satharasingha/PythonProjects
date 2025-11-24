balance = 0

print("Welcome to Banking System")

while True:
    selection = input("Choose an option: Deposit | Withdraw | Check balance | Quit : ").lower()

    if selection == "check balance":
        print("Your balance is:", balance)

    elif selection == "deposit":
        deposit = float(input("Enter deposit amount: "))
        balance = balance + deposit
        print("Your current balance is:", balance)

    elif selection == "withdraw":
        withdraw = float(input("Enter withdraw amount: "))
        balance = balance - withdraw
        print("Success! Your current balance is:", balance)

    elif selection == "quit":
        print("Thank you for using the Banking System!")
        break

    else:
        print("Invalid option. Please try again.")
