def is_valid_password(password):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_even(n):
        return n % 2 == 0

    # Разбиваем пароль на три части
    parts = password.split(':')

    # Проверяем условия для каждой части пароля
    if len(parts) == 3:
        a, b, c = map(int, parts)
        if is_palindrome(a) and is_prime(b) and is_even(c):
            return True

    return False


# Test cases
print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))
