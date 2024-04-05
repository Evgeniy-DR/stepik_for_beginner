# На вход программе подается строка текста, содержащая
# различные натуральные числа. Из данной строки формируется
# список чисел. Напишите программу, которая меняет местами
# минимальный и максимальный элемент этого списка.

string = input().split(' ')

reverse = string.copy()
string.sort(key=int)
reverse.sort(reverse=True, key=int)

print(*string, sep=' ')
print(*reverse, sep=' ')

