import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate and print passwords from 1 to 40 characters
for length in range(1, 41):
    print(f"Password of length {length}: {generate_password(length)}")


