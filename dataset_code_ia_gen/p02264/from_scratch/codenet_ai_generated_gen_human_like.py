from collections import deque
import sys

input = sys.stdin.readline

n, q = map(int, input().split())
queue = deque()
for _ in range(n):
    name, time = input().split()
    queue.append([name, int(time)])

current_time = 0
results = []

while queue:
    name, time = queue.popleft()
    if time <= q:
        current_time += time
        results.append((name, current_time))
    else:
        current_time += q
        queue.append([name, time - q])

for name, finish_time in results:
    print(name, finish_time)