

def is_valid_password(password):
    work_string = password.split(':')
    if len(work_string) > 3:
        return False
    if not work_string.isdigit():
        return False



# объявление функции
def is_palindrome(text):
    small_and_not_spaces = text.lower().replace(' ', '')
    and_not_any_symbols = ''.join(t for t in small_and_not_spaces if t.isalpha())
    print(and_not_any_symbols)
    for i in range(1, len(and_not_any_symbols) + 1):
        if and_not_any_symbols[::-i] == and_not_any_symbols[::i]:
            return True
        else:
            return False


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
