p = [1] * 1000001
p[0] = 0
p[1] = 0
i = 2
while i < 500000:
    j = 2
    while j <= 1000000 // i:
        p[i * j] = 0
        j += 1
    i += 1

while 1:
    n = int(input())
    if n == 0:
        break
    s = 0
    i = 1
    while i <= n // 2:
        if p[i] == 1 and p[n - i] == 1:
            s += 1
        i += 1
    print(s)