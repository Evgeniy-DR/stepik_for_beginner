

digit = [int(just_digit) ** 2 for just_digit in input().split() if int(just_digit) % 2 == 0 and (int(just_digit) ** 2) % 10 != 4]

print(*digit, sep=' ')
