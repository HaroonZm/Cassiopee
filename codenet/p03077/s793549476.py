import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

min_num = min(a, b, c, d, e)
print(math.ceil(n/min_num) + 4)