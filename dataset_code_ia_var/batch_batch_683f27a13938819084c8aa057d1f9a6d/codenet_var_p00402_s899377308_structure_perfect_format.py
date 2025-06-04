n = int(input())
x = list(map(int, input().split()))
a = max(x) + min(x)
b = a // 2
print(max(x) - b)