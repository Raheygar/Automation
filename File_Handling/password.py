import re
def check_password_strength(password):
    if len(password) <= 8:
        return "Weak : password must be 8 characters long"
    if not any(char.isupper() for char in password):
        return "Weak : password must have an uppercase letter"
    if not any(char.islower() for char in password):
        return "Weak : password must have a lowercase letter"
print(check_password_strength('Lord Raheygar'))