

# объявление функции
def convert_to_python_case(text):
    new_text = ''
    if text[0].isupper():
        new_text += text[0].lower()

    for char in text[1:]:
        if char.isupper() and text[0:]:
            new_text += '_' + char.lower()
        else:
            new_text += char
    return new_text


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
