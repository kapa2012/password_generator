import string
import secrets
nums = string.digits
letters = string.ascii_letters
chars = string.punctuation
nums_and_letters = string.digits + string.ascii_letters
nums_and_chars = string.digits + string.punctuation
letters_and_chars = string.ascii_letters + string.punctuation
letters_nums_digits = string.digits + string.ascii_letters + string.punctuation
def greeting():
    while True:
        print("HELLO! WELCOME TO PASSWORD GENERATOR!".center(30, '='))
        will_contain_letters = input("Do u want any letters in your password?(y/n)").lower().strip()
        if will_contain_letters != 'y' and will_contain_letters != 'n':
            print("Please enter y/n")
            continue
        will_contain_nums = input("Do u want any numbers in your password?(y/n)").lower().strip()
        will_contain_chars = input("Do u want any characters in your password?(y/n)").lower().strip()
        if will_contain_chars != 'y' and will_contain_chars != 'n':
            print("Please enter y/n")
            continue
        try:
            length = int(input("How long will be your password?\n >"))
        except ValueError:
            print("Enter please a number")
            continue
        if length < 8:
            print("Password that contains less than 8 characters isn`t really safe ngl")
            continue

        if will_contain_letters == "y" and will_contain_nums == "y" and will_contain_chars == "y":
            password = ''.join(secrets.choice(letters_nums_digits)for i in range(length))
            print(password)
        elif will_contain_letters == "y" and will_contain_nums == "y" and will_contain_chars == "n":
            password = ''.join(secrets.choice(nums_and_letters) for i in range(length))
            print(password)
        elif will_contain_letters == "y" and will_contain_nums == "n" and will_contain_chars == "n":
            password = ''.join(secrets.choice(letters) for i in range(length))
            print(password)
        elif will_contain_letters == "n" and will_contain_nums == "y" and will_contain_chars == "n":
            password = ''.join(secrets.choice(nums) for i in range(length))
            print(password)
        elif will_contain_letters == "y" and will_contain_nums == "n" and will_contain_chars == "y":
            password = ''.join(secrets.choice(letters_and_chars) for i in range(length))
            print(password)
        elif will_contain_letters == "n" and will_contain_nums == "n" and will_contain_chars == "y":
            password = ''.join(secrets.choice(chars) for i in range(length))
            print(password)
        elif will_contain_letters == "n" and will_contain_nums == "y" and will_contain_chars == "y":
            password = ''.join(secrets.choice(nums_and_chars) for i in range(length))
            print(password)
        elif will_contain_letters == "n" and will_contain_nums == "n" and will_contain_chars == "n":
            print("Bro... you want empty password?Its not really safe yk...")
    greeting()

