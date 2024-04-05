
s = input().split()
counters = 0

for i in range(0, len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            counters += 1


print(counters)
