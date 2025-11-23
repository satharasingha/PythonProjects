#collect user preferences
 #length
 #should contain uppercase
 #should contain special
 #should contain digits


#get all available char
##randomly pick char up to the len
#ensure we have at least one of each char type
#ensure length is valid


import random
import string

def generate_password():
    length = int(input("Enter the password length: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").strip().lower()
    include_special = input("Include special characters? (y/n): ").strip().lower()
    include_digits = input("Include digits? (y/n): ").strip().lower()

    if length < 4:
        print("Too short password, need at least 4 characters.")
        return

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase == "y" else ""
    special = string.punctuation if include_special == "y" else ""
    digits = string.digits if include_digits == "y" else ""

    all_characters = lower + upper + special + digits

    # Ensure at least one of each selected type
    required_characters = []
    if include_uppercase == "y":
        required_characters.append(random.choice(upper))
    if include_special == "y":
        required_characters.append(random.choice(special))
    if include_digits == "y":
        required_characters.append(random.choice(digits))

    # Fill the rest with random characters
    remaining_length = length - len(required_characters)
    password = required_characters + random.choices(all_characters, k=remaining_length)

    # Shuffle the result
    random.shuffle(password)

    # Convert list to string
    final_password = "".join(password)
    print("Your generated password is:", final_password)

generate_password()
