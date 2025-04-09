import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter required password length: \n"))
            if length > 0:
                return length
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def main():
    print("--- Password Generator ---")
    length = get_password_length()
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
