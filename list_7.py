# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.

n = int(input())
list_enter = []
list_no_double = []
search = ''

for i in range(n):
    k = input()
    list_enter.append(k)
    list_enter.lower()
search = input()
search.lower()

if search in list_enter:
    list_no_double.append(search)

print(*list_no_double, sep='\n', end=' ')
# print('\n')
# print(*list_function, sep='\n')
