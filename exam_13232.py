


# Ввод строки текста
input_text = input()

# Разделение строки на слова и преобразование каждого слова
result = ' '.join(word[1:] + word[0] + 'ки' for word in input_text.split())

# Вывод результата
print(result)