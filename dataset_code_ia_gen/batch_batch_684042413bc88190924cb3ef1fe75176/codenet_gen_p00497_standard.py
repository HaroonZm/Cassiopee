import sys
input = sys.stdin.readline

N, M = map(int, input().split())
covered = [0]*(N+2)
events = [[] for _ in range(N+2)]

for _ in range(M):
    a, b, x = map(int, input().split())
    for i in range(x+1):
        start = b + i
        end = b + x + 1
        events[a+i].append((start, end))

count = 0
for row in range(1, N+1):
    line = [0]*(row+2)
    for s, e in events[row]:
        line[s] += 1
        if e <= row:
            line[e] -= 1
    c = 0
    for i in range(1, row+1):
        c += line[i]
        if c > 0:
            count += 1
print(count)