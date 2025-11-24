select_operator = input("Please select the operator: + - / * : ")

while True:
    user_input1 = int(input("Enter first number: "))
    user_input2 = int(input("Enter second number: "))

    addition = user_input1 + user_input2
    subtraction = user_input1 - user_input2
    multiplication = user_input1 * user_input2
    division = user_input1 / user_input2

    if select_operator == "+":
        print(f"{addition}")

    elif select_operator == "-":
        print(f"{subtraction}")

    elif select_operator == "*":
        print(f"{multiplication}")

    elif select_operator == "/":
        print(f"{division}")

    else:
        print("Invalid operator")

    break
