n = int(input())
x = list(map(int, input().split()))
max_x = max(x)
min_x = min(x)
a = max_x + min_x
b = a // 2
print(max_x - b)