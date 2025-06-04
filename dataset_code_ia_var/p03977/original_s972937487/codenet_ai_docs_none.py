n = int(input())
for _ in range(n):
    i, j = (int(k) for k in input().split())
    if i % 2 == 0:
        print(127 * i - j)
    else:
        print(127 * (i - 1) + j)