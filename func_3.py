
# Напишите функцию draw_triangle(), которая выводит звездный прямоугольный треугольник с катетами, равными
# 10 в соответствии с образцом:

# объявление функции


def draw_triangle(fill, base):
    counter = 0
    range_enter = base//2 + 1
    for i in range(range_enter):
        counter += 1
        print(fill * counter)

    for j in range(range_enter):
        counter -= 1
        print(fill * counter)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
