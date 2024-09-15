import random
import string

# Function to generate a password of the given length
def generate_password(length):
    # Define possible characters to use in the password
    # ascii_letters: A-Z and a-z
    # digits: 0-9
    # punctuation: Special characters like !@#$%^&*() etc.
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting 'length' number of characters
    password = ''.join(random.choice(characters) for i in range(length))

    # Return the generated password
    return password

# Prompt the user to input the desired length of the password
password_length = int(input("Enter the desired password length: "))

# Generate the password using the specified length
password = generate_password(password_length)

# Print the generated password to the console
print(f"Generated Password: {password}")
