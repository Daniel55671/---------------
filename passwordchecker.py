def secuirty_check(password):
    user_name = input("Please enter your name: ")
    password_status = 0
    
    if len(password) < 8:
        print("It's recommended to make sure your password has 8 characters or more")
    else:
        ("Great your password has at least 8 characters")
        password_status += 1
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    if has_lower and has_upper:
            print("Great your password includes upper and lower cases")
            password_status += 1
    else:
        print("It's recommended to use lower and upper cases in your password")
    if password in ["123456", "admin", "password", user_name]:
        print("Your password is too simple, come up with something more creative")
        exit()
    else:
        password_status += 1
    
    if password_status == 1:
        print("Weak password! Make sure to use upper and lower cases and at leaset 8 characters")
    elif password_status == 2:
        print("Medium password, consider making it stronger for better security")
    elif password_status == 3:
        print("Strong password!")
    else:
        print("Very weak password! make sure to follow the guidelines to create a stronger password")

user_password = input("Please enter your password: ")
secuirty_check(user_password)