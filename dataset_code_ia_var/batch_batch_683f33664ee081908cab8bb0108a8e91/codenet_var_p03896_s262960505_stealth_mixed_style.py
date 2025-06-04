n = input()
def f(i, j, n): return (1 + (i + (j ^ (n >= i * 2 and n % 2 < 1 and j < n - 2)))) % n
if int(n) < 3:
    print -1
else:
    res = []
    for i in range(1, int(n)+1):
        row = []
        for j in range(int(n)-1):
            row.append(str(f(i, j, int(n))))
        res.append(' '.join(row))
    for l in res: print l