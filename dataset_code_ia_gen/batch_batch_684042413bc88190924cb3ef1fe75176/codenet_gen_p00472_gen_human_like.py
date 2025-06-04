n, m = map(int, input().split())
dist = [0] * (n)
for i in range(1, n):
    dist[i] = int(input())
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1]
    if i < n:
        prefix[i] += dist[i]
pos = 1
mod = 10**5
total = 0
for _ in range(m):
    a = int(input())
    start = pos
    end = pos + a
    if start <= end:
        distance = prefix[end] - prefix[start]
    else:
        distance = prefix[start] - prefix[end]
    total += distance
    total %= mod
    pos = end
print(total % mod)