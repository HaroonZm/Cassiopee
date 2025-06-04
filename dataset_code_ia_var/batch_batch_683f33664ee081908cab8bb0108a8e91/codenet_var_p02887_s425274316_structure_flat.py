n = int(input())
s = input()
result = 1
i = 1
while i < n:
    if s[i] != s[i-1]:
        result += 1
    i += 1
print(result)