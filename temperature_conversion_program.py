# Display a welcome message to the user
print("WELCOME TO THE TEMPERATURE CONVERSION PROGRAM")

# Ask the user which conversion they want to perform
perform = input("Which temperature would you like to convert to: Celsius to Fahrenheit (1), Fahrenheit to Celsius (2), Celsius to Kelvin (3)? : ")
temperature = float(input("Enter temperature: "))

# Get the user's choice as input
if perform == "1":
    temperature = temperature * 9 / 5 + 32
    print("The temperature in Fahrenheit is:", temperature)

elif perform == "2":
    temperature = (temperature - 32) * 5 / 9
    print("The temperature in Celsius is:", temperature)

elif perform == "3":
    temperature = temperature + 273.15
    print("The temperature in Kelvin is:", temperature)

# Use if-elif statements to perform the correct conversion based on user choice
else:
    print("Invalid input")
