n_r = input().split()
n = int(n_r[0])
r = int(n_r[1])

if n < 10:
    diff = 10 - n
    x = 100 * diff
    total = x + r
    print(total)
else:
    print(r)