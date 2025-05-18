n = int(input())
a, b, c = [list(map(int, input().split())) for _ in range(3)]
foodSum = sum(b)
for i in range(n - 1):
    if a[i + 1] - a[i] == 1:
        foodSum += c[a[i] - 1]

print(foodSum)