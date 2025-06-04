n, a, b = input().split()
n = int(n)
a = int(a)
b = int(b)
cost = a * n
if cost < b:
    print(cost)
else:
    print(b)