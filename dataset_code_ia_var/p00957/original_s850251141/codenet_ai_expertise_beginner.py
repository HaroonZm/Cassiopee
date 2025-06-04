import math

l, k = input().split()
l = int(l)
k = int(k)
c = 0

for i in range(1, (l + 1) // 2 + 1):
    for j in range(0, i + 1):
        if 2 * i - 1 + j * (k - 1) <= l:
            comb = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            c += comb
        else:
            break

print(c)