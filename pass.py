password = input("Enter your password : ")
for char in password: 
    if len(password) <= 8:
        print("Please enter a passowrd with more than 8 characters ")
        password = input("Please enter the password again : ")
    if not any(char.islower()):
        return "Weak password. Password must have an uppercase character"

    if not any(char.isupper()):
        print("Please atleast enter one character in upper case ")
        password = input("Enter your password : ")
    if not any(char.isnumeric()):
        print("Please atleast enter one numeric character  ")
        password = input("Enter your password : ")
