# На вход программе подается строка текста, содержащая
# различные натуральные числа. Из данной строки формируется
# список чисел. Напишите программу, которая меняет местами
# минимальный и максимальный элемент этого списка.

input_string = input()
parts_string = input_string.split('#')
enter = int(parts_string[1])

# enter = int(input('#'))
result_string = []

for i in range(enter):
    enter_string = input()
    parts = enter_string.split('#')
    work_string = parts[0].rstrip()
    result_string.append(work_string)

print(*result_string, sep='\n')
