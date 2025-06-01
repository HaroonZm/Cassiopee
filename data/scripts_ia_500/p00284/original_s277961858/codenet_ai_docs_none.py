import sys

SIZE = 32
POW = [1]*SIZE
for i in range(1, SIZE):
    POW[i] = POW[i-1]*2

N = int(input())

for _ in range(N):
    start, goal = map(int, input().split())
    ans = 0
    current = start
    while current != goal:
        rank = 0
        for i in range(SIZE-1, 0, -1):
            if abs(current) % POW[i] == 0 and current + POW[i] <= goal:
                rank = i
                break
        current += POW[rank]
        ans += 1
    print(ans)