import math
n = int(input())
nn = n - 1
count = 0
for i in range(1, n):
    count += nn // i
print(count)