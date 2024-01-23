import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def display_password(password):
    print("Generated Password:", password)

def password_generator():
    length = get_password_length()
    password = generate_password(length)
    display_password(password)

# Run the password generator
password_generator()