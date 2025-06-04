import math

f = 100000
n = int(input())

for i in range(n):
    f = f * 1.05
    f = math.ceil(f / 1000) * 1000
    f = int(f)

print(f)