def croad():
    n, k = input().split()
    n = int(n)
    k = int(k)
    x = input().split()
    for i in range(n):
        x[i] = int(x[i])
    y = []
    for i in range(n - 1):
        y.append(x[i + 1] - x[i])
    y.sort()
    y = y[::-1]
    while k > 1 and len(y) > 0:
        y.pop(0)
        k = k - 1
    total = 0
    for value in y:
        total = total + value
    print(total)

a = int(input())
for i in range(a):
    croad()