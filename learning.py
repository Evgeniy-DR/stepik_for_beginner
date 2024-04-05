# Программа должна вывести одну строку – декодированное сообщение.
# Обратите внимание, что нужно декодировать сообщение,
# а не закодировать.

def cezar(a, b):

    for char in string:
        print(chr((ord(char)-step-ord('a')) % 26 + ord('a')), end='')


step = int(input())
string = input()
cezar(step, string)

