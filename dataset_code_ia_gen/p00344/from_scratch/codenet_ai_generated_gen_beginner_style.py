N = int(input())
a = list(map(int, input().split()))

count = 0
for start in range(N):
    pos = start
    visited = set()
    while True:
        if pos == start and len(visited) > 0:
            count += 1
            break
        if pos in visited:
            break
        visited.add(pos)
        pos = (pos + a[pos]) % N

print(count)