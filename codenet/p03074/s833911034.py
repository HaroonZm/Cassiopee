n, k = map(int, input().split())
s = input()
rest = k
i = 0
while i < n:
    if s[i] == '1':
        i += 1
    else:
        if rest == 0:
            break
        rest -= 1
        while i < n and s[i] == '0':
            i += 1
ans = i
j = 0
while i < n:
    while i < n and s[i] == '0':
        i += 1
    while i < n and s[i] == '1':
        i += 1
    while j < n and s[j] == '1':
        j += 1
    while j < n and s[j] == '0':
        j += 1
    ans = max(ans, i - j)
print(ans)