n_r = input().split()
n = int(n_r[0])
r = int(n_r[1])

if n > 10:
    R = r
else:
    R = r + 100 * (10 - n)

print(R)