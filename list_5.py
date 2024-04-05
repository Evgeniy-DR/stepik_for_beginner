# На вход программе подается натуральное число
# n и n строк, а затем число
# k. Напишите программу, которая выводит
# k-ую букву из введенных строк на одной строке без пробелов.


n = int(input())
string = []
dell_not_divided = []
new_string = ''

for i in range(n):
    enter_string = input()
    string.append(enter_string)
    print(string)

k = int(input())

for i in range(len(string)):
    m = string[i]
    if k <= len(m):
        new_letter = m[k - 1]
        new_string += new_letter

print(new_string)
