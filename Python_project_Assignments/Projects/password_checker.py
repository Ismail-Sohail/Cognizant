def check_password(password):
    has_upper = has_lower = has_digit = has_special = False
    special_characters = "@#$%^&*()_+!"

    if len(password) < 8:
        print("Your password must be at least 8 characters long.")
        return

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        print("Your password must contain at least one uppercase letter.")
    if not has_lower:
        print("Your password must contain at least one lowercase letter.")
    if not has_digit:
        print("Your password must contain at least one digit.")
    if not has_special:
        print("Your password must contain at least one special character (@, #, $, etc.).")

    if has_upper and has_lower and has_digit and has_special:
        print("Your password is strong! 💪")

if __name__ == '__main__':
    password = input("Enter your password: ")
    check_password(password)
