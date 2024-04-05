

# объявление функции
def print_digit_sum(num):
    summ = 0
    for digit in str(num):
        summ += int(digit)
    print(summ)

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)