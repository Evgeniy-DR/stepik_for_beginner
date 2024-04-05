
# На вход программе подается натуральное число
# n. Напишите программу, которая создает список, состоящий из делителей введенного числа.


n = int(input())
string = []
dell_not_divided = []


for i in range(n):
    enter_string = int(input())
    string.append(enter_string)

summ = [string[i] + string[i + 1] for i in range(len(string) - 1)]


print(summ)

