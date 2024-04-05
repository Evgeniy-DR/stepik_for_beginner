
# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False


def get_next_prime(num):
    next_num = num + 1
    while not is_prime(next_num):
        next_num += 1
    return next_num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
