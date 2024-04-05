

# объявление функции
def is_password_good(password):
    upper = any(password.isupper() for password in password)
    lower = any(password.islower() for password in password)
    digit = any(password.isdigit() for password in password)
    if len(password) >= 8 and upper and lower and digit:
        return True
    else:
        return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
