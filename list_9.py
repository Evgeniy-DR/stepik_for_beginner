
n = int(input())
list_numbers = []
list_minus = []
list_zero = []
list_plus = []

# Input elements into the list
for i in range(n):
    k = int(input())
    list_numbers.append(k)

for number in list_numbers:
    if number < 0:
        list_minus.append(number)
    elif number == 0:
        list_zero.append(number)
    else:
        list_plus.append(number)


# Print the lines with all search terms
print(*list_minus, sep='\n')
print(*list_zero, sep='\n')
print(*list_plus, sep='\n')
