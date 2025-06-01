N, M = map(int, input().split())
from collections import deque

table = [deque() for _ in range(N)]

for _ in range(M):
    command, num = map(int, input().split())
    if command == 0:
        print(table[num - 1].popleft())
    else:
        minId = min(range(N), key=lambda i: len(table[i]))
        table[minId].append(num)