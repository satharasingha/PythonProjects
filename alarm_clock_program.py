# Import the time module to track the current time
import time
import datetime
import winsound  # For playing a sound on Windows

# Ask the user to enter the alarm time (for example, in HH:MM:SS format)
alarm_time = input("Please enter alarm time (HH:MM:SS): ")

# Confirm the alarm time to the user
print("Alarm set for:", alarm_time)

# Use a while loop to constantly check the current time
while True:
    # Inside the loop, get the current system time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Compare the current time with the user’s alarm time
    if current_time == alarm_time:
        print("Wake up! ⏰")
        # Play an alarm sound
        winsound.Beep(1000, 1000)  # (frequency, duration)
        break  # After alarm rings, break out of the loop

    # Wait one second before checking again
    time.sleep(1)
