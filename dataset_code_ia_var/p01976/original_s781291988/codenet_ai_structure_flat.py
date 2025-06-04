import sys, heapq
n = int(sys.stdin.readline())
a = [int(e) for e in sys.stdin.readline().split()]
r = []
x = []
y = []
i = 1
while i <= n:
    heapq.heappush(x, a[i - 1])
    heapq.heappush(y, a[n - i])
    while x and y and x[0] == y[0]:
        heapq.heappop(x)
        heapq.heappop(y)
    if not x and not y:
        r.append(i)
    i += 1
s = ''
j = 0
while j < len(r):
    s += str(r[j])
    if j != len(r) - 1:
        s += ' '
    j += 1
print(s)