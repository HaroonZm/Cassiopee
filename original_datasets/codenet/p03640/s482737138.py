from collections import deque
h , w = map(int,input().split())
n = int(input())
a = list(map(int,input().split()))
p = 1
d = deque()
for i in range(n):
    for j in range(a[i]):
        if len(d) == w:
            print(*d)
            d = deque()
            p *= -1
        if p == 1:
            d.append(i+1)
        elif p == -1:
            d.appendleft(i+1)
if len(d) != 0:
    print(*d)