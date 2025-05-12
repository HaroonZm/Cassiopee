import math
n, d = map(int, input().split())
place_list = []
count = 0
for i in range(n):
    a, b = map(int, input().split())
    if math.sqrt(a*a + b*b) <= d:
        count += 1
print(count)