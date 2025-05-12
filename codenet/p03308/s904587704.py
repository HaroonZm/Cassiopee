import math

n = int(input())
a = sorted([int(i) for i in input().split()])
print(a[-1] - a[0])