n_r = input().split()
n = int(n_r[0])
r = int(n_r[1])

if n >= 10:
    print(r)
else:
    result = r + 100 * (10 - n)
    print(result)