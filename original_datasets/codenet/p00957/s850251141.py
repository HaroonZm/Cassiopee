import math
l, k = map(int, input().split())
c = 0
for i in range(1, int((l + 1) / 2) + 1):
    for j in range(i + 1):
        if 2 * i - 1 + j * (k - 1) <= l:
            c += math.factorial(i) / math.factorial(j) / math.factorial(i - j)
        else:
            break
print(int(c))