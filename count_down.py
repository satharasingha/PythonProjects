# Import the time module to use the sleep function
import time

# Ask the user to enter the number of seconds for the countdown
seconds = input("Please enter how many seconds you have: ")

# Convert the input into an integer
seconds = int(seconds)

# Use a while loop to count down from the given number to zero
while seconds > 0:
    # Inside the loop, print the current time remaining
    print(seconds)

    # Pause for one second using time.sleep(1) after each print
    time.sleep(1)

    # Decrease the countdown value by 1 on each loop
    seconds -= 1

# When the countdown reaches zero, print a message like "Time's up!"
print("Time's up!")
