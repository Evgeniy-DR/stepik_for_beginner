

# объявление функции
def quick_merge(lists):
    merge_lists = []
    for lst in lists:
        merge_lists.extend(lst)
    return sorted(merge_lists)


n = int(input())
lists = []

for i in range(n):
    string_n = [int(c) for c in input().split()]
    lists.append(string_n)

# вызываем функцию
result = quick_merge(lists)
print(*result)
