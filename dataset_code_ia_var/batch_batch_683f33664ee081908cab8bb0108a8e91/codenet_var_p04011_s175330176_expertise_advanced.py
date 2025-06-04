n = int(input())
k = int(input())
x = int(input())
y = int(input())

count_x, count_y = min(n, k), max(n - k, 0)
ans = count_x * x + count_y * y

print(ans)