import random
import string

def generate_password(length=8):
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    # Define the character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one of each type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the remaining length with random characters from all pools
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)

# Example usage without interactive input
def main():
    try:
        length = 12  # Default password length (can be modified as needed)
        print("Generated password:", generate_password(length))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
