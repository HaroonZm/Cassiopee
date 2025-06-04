a = input()
ans = 1
d = {}
for i in range(len(a)):
    ch = a[i]
    if ch not in d:
        d[ch] = 0
    d[ch] += 1
    ans = ans + (i + 1 - d[ch])
print(ans)