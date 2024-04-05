

# объявление функции
def print_fio(name, surname, patronymic):
    print(f'{surname[:1].upper()}{name[:1].upper()}{patronymic[:1].upper()}')

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

