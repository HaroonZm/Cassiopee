n = int(input())
s = int(input())
if n == s:
    print(n + 1)
    exit()
for i in range(2, int(n**0.5) + 3):
    nb = n
    b = i
    res = 0
    while nb >= b:
        res += nb % b
        nb //= b
    res += nb
    if res == s:
        print(i)
        exit()
ans = 10**13
for k in range(1, int(n**0.5) + 3):
    if (n-s) % k != 0 or n-s < 0:
        continue
    b = (n-s)//k + 1
    if b == 1:
        continue
    nb = n
    res = 0
    bb = b
    while nb >= bb:
        res += nb % bb
        nb //= bb
    res += nb
    if res == s:
        if b < ans:
            ans = b
if ans != 10**13:
    print(ans)
else:
    print(-1)