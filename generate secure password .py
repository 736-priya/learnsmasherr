import random
import string
def generate_password(length,uppercase = True,lowercase=True,numbers=True,symbols=True):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    if not chars:
        print("Error:At least one character type should be selected.")
        return None
    password = ''.join(random.choice(chars)for _ in range(length))
    return password
def get_criteria():
    print("password criteria:")
    while True:
        try:
            length = int(input("Desired password length:"))
            if length <= 0:
                print("Error:Length should be a positive integer.")
                continue
            break
        except ValueError:
            print("Error:Invalid input.pleasebenter a positive integer.")
    uppercase=input("Include uppercase letters?(Y/N):").upper()=='Y'
    lowercase=input("Include lowercase letters?(Y/N):").lower()=='Y'
    numbers=input("Include numbers?(Y/N):").upper()=='Y'
    symbols=input("Include symbols?(Y/N):").upper()=='Y'
    return length,uppercase,lowercase,numbers,symbols
print("secure password Generator")
print("=========================")

length,uppercase,lowercase,numbers,symbols = get_criteria()
password = generate_password(length,uppercase,lowercase,numbers,symbols)

if password:
    print("Generate password:",password)
