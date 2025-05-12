#ABC066-C
from collections import deque
n = int(input())
a = list(map(int,input().split()))

d = deque()

for i in range(n):
    if i % 2 == 0:
        d.append(a[i])
    else:
        d.appendleft(a[i])

result = list(d)
if n % 2 == 1:
    result = reversed(list(d))
print(*result)