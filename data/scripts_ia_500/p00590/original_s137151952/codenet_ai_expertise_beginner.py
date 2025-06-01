n = 10000
p = [1] * (n + 1)
p[0] = 0
p[1] = 0

limit = int(n ** 0.5)
for i in range(2, limit + 1):
    if p[i] == 1:
        j = i * i
        while j <= n:
            p[j] = 0
            j += i

while True:
    try:
        n = int(input())
    except:
        break
    count = 0
    for i in range(2, n):
        if p[i] == 1 and p[n - i + 1] == 1:
            count += 1
    print(count)