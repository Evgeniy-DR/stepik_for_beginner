# На вход программе подается строка текста в которой буква «h»
# встречается как минимум два раза. Напишите программу,
# которая возвращает исходную строку и переворачивает последовательность символов,
# заключенную между первым и последним вхождением буквы «h».


s = input()

first_h = s.find('h')
last_h = s.rfind('h')
string_to_reverse = s[first_h+1:last_h]
reverse = string_to_reverse[::-1]

# print(first_h, last_h)
print(f'{s[:first_h+1]}{reverse}{s[last_h:]}')
