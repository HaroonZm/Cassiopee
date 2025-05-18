s = input()
n = len(s)

ans = 0
for i in range(1, n):
    if i%2 != 0:
        if s[i] == 'g':
            ans += 1
    else:
        if s[i] == 'p':
            ans -= 1
print(ans)