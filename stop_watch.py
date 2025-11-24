# Start of the Stopwatch Program

# Import the time module to track seconds accurately
import time

# Display a message to the user about how to start and stop the stopwatch
start = input("Please type 1 then your time will start:\n ")

# Wait for the user to press a key (like Enter) to start the timer
if start == "1":
    start = time.time()
    print("Timer started...")

    # Wait for the user to press a key to stop the timer
    end = input("Please type 0 then your time will stop:\n ")
    if end == "0":
        end = time.time()
        print("Timer stopped.")

        # Calculate the difference between the end time and start time
        elapsed = end - start

        # Display the elapsed time in seconds
        print("Elapsed time:", round(elapsed, 2), "seconds")
