n, m = map(int, input().split())
distances = [0]
for _ in range(n-1):
    distances.append(int(input()))
a = [int(input()) for _ in range(m)]

pos = 1
total = 0
for move in a:
    start = pos
    end = pos + move
    if start < end:
        d = sum(distances[start:end])
    else:
        d = sum(distances[end:start])
    total += d
    pos = end

print(total % 100000)