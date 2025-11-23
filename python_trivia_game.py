import random

questions = {
    "What keyword is used to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "bool",
    "What symbol is used to start a comment in Python?": "#",
    "Which function displays output to the screen?": "print",
    "What data type is created when you use quotes around text?": "string",
    "Which keyword is used to create a loop that runs while a condition is true?": "while",
    "What keyword is used to import a module in Python?": "import",
    "What function is used to get input from the user?": "input",
    "What keyword stops a loop early?": "break",
    "Which function returns the number of items in a list?": "len"
}

# Shuffle the questions
question_items = list(questions.items())
random.shuffle(question_items)

score = 0

# Loop through shuffled questions
for question, answer in question_items:
    user_answer = input(question + " ").strip().lower()
    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer was '{answer}'.\n")

# Show final score AFTER the loop
print(f"🎯 Your final score is {score}/{len(questions)}")
