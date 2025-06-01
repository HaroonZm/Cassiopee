from sys import stdin

s = stdin.readline().rstrip()
n = int(stdin.readline())
ls = len(s)

ans = 0
for _ in range(n):
    r = stdin.readline().rstrip()
    lr = len(r)
    if any(all(r[(j + k) % lr] == s[k] for k in range(ls)) for j in range(lr)):
        ans += 1
print(ans)