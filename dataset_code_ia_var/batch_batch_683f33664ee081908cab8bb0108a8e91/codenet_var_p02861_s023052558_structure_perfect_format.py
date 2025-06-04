n = int(input())
ls = [list(map(int, input().split())) for i in range(n)]
a = 0
for j in range(n):
    for k in range(n):
        if j < k:
            a += ((ls[k][0] - ls[j][0]) ** 2 + (ls[k][1] - ls[j][1]) ** 2) ** 0.5
b = a / (n * (n - 1) / 2)
print(b * (n - 1))