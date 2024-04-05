

# объявление функции
def is_correct_bracket(text):
    stack = []
    for char in text:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
