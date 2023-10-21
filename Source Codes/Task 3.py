import random
import string

def generate_password(length):
    # Define character sets for different complexity levels
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on desired complexity
    characters = lower_case + upper_case + digits + special_characters

    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))

    return password
try:
    # Prompt the user for the desired password length
    password_length = int(input("Enter the desired password length: "))

    # Check if the specified length is valid
    if password_length <= 0:
        print("Password length should be a positive integer.")
    else:
        # Generate the password
        generated_password = generate_password(password_length)

        # Display the generated password
        print(f"Generated Password: {generated_password}")

except ValueError:
    print("Invalid input. Please enter a valid positive integer for password length.")
 
