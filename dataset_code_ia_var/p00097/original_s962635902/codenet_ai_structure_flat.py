m = 1001
A = range(9)
d = []
for i in A:
    d.append([0] * m)
for i in range(101):
    j = 8
    while j >= 0:
        if j == 0:
            d[j][i] = 1
        else:
            k = 0
            while k < m - i:
                d[j][k + i] += d[j - 1][k]
                k += 1
        j -= 1
while True:
    n_s = raw_input()
    n, s = map(int, n_s.split())
    if n == 0 and s == 0:
        break
    print d[n - 1][s]