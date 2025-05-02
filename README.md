import random
import string
import math
import pyperclip
import nltk
import os

# Set a custom NLTK data path to store the word list
os.environ["NLTK_DATA"] = "M:\\nltk_data"
from nltk.corpus import words

# Ensure the word list is downloaded and loaded
nltk.download("words", download_dir="M:\\nltk_data")
word_list = words.words()

# ANSI escape codes for color formatting in the terminal output
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def calculate_entropy(password):
    """
    Estimates the strength of a password based on entropy calculation.

    Entropy represents the randomness and complexity of a password. 
    Higher entropy means stronger password security.

    :param password: The password or passphrase to evaluate.
    :return: Entropy value of the password.
    """
    character_set_size = len(set(password))  # Count of unique characters in the password
    entropy = math.log2(character_set_size ** len(password))  # Entropy formula
    return entropy

def generate_password(length):
    """
    Generates a random password with the specified length.

    :param length: Number of characters in the password.
    :return: Generated password and its entropy value.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entropy = calculate_entropy(password)
    return password, entropy

def generate_passphrase(num_words=4):
    """
    Generates a passphrase using random words for better memorability.

    :param num_words: Number of words to include in the passphrase.
    :return: Generated passphrase and its entropy value.
    """
    passphrase = '-'.join(random.choice(word_list) for _ in range(num_words))
    entropy = calculate_entropy(passphrase)
    return passphrase, entropy

# Ask user for password type (random password or passphrase)
choice = input("Generate (P)assword or (W)ord-based Passphrase? ").strip().lower()
length_or_words = int(input("Enter the number of characters/words: "))

# Generate the chosen type of password
if choice == 'p':
    password, entropy = generate_password(length_or_words)
elif choice == 'w':
    password, entropy = generate_passphrase(length_or_words)
else:
    print("Invalid choice. Please restart.")
    exit()

# Determine color coding based on entropy value
color = RED if entropy < 40 else GREEN
print(f"{color}Generated: {password} (Entropy: {entropy:.2f}){RESET}")

# Copy generated password to clipboard for convenience
pyperclip.copy(password)
print("Password copied to clipboard!")

