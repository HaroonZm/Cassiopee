import math

N = int(input())
b = []
a = list(map(int, input().split()))
x = (min(a) + max(a)) // 2
for i in range(N):
    b.append(abs(x - a[i]))
print("{:.0f}".format(max(b)))