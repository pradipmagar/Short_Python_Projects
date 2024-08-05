import re
import random

class AccountRegistration:
    def __init__(self):
        self.username = None
        self.password = None

    def create_account(self):
        print("Welcome to the registration process!")
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")

    def check_password_strength(self):
        # Check password strength based on criteria
        length_error = len(self.password) < 8
        digit_error = re.search(r"\d", self.password) is None
        uppercase_error = re.search(r"[A-Z]", self.password) is None
        lowercase_error = re.search(r"[a-z]", self.password) is None
        special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password) is None

        errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
        error_count = sum(errors)

        if error_count == 0:
            print("Password is strong.")
        else:
            print("Password is weak.")
            print("Errors:")
            if length_error:
                print("- Password should be at least 8 characters long.")
            if digit_error:
                print("- Password should contain at least one digit.")
            if uppercase_error:
                print("- Password should contain at least one uppercase letter.")
            if lowercase_error:
                print("- Password should contain at least one lowercase letter.")
            if special_char_error:
                print("- Password should contain at least one special character.")

    def generate_captcha(self):
        captcha = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        print("Your captcha is:", captcha)
        user_input = input("Please enter the captcha: ")
        if user_input == captcha:
            print("Captcha validated. Registration successful!")
        else:
            print("Captcha validation failed. Registration aborted.")


if __name__ == "__main__":
    registration = AccountRegistration()
    registration.create_account()
    registration.check_password_strength()
    registration.generate_captcha()
