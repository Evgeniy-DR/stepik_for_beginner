# # put your python code here
# from math import *
# a=float(input())
# b=float(input())
# c=float(input())
#
# d=pow(b, 2)-4*a*c
# if d>0:
#     x1=(-b+sqrt(d))/(2*a)
#     x2=(-b-sqrt(d))/(2*a)
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif d==0:
#     x1=-(b/(2*a))
#     print(x1)
# else:
#     print('Нет корней')

import math


# объявление функции
def solve(a, b, c):
    d = pow(b, 2) - 4 * a * c
    if d > 0:
        x_1 = (-b+math.sqrt(d))/(2*a)
        x_2 = (-b-math.sqrt(d))/(2*a)
        return (min(x_1, x_2)), (max(x_1, x_2))
    elif d == 0:
        x_1 = -(b/(2*a))
        x_2 = x_1
        return x_1, x_2


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)

