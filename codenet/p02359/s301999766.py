from collections import deque

N, T = map(int, input().split())
queue = deque()

for i in range(N):
    l, r = map(int, input().split())
    queue.extend([(l, 1), (r, -1)])
queue = sorted(queue)

ans = p = 0

for t, s in queue:
    if s == 1:
        p += 1
        ans = max(ans, p)
    else:
        p -= 1
    
print(max(ans, p))