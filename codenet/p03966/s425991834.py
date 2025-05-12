n = int(input())
a, b = 1, 1
for i in range(n):
  x, y = list(map(int, input().split()))
  n = max(-(-a//x), -(-b//y))
  a, b = n*x, n*y
print(a+b)