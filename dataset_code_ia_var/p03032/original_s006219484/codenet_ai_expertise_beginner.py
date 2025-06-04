n, k = map(int, input().split())
v = list(map(int, input().split()))

answer = 0

for a in range(0, n+1):
    for b in range(0, n+1):
        if a + b > n:
            continue
        max_take = a + b
        if max_take > k:
            continue
        items = []
        for i in range(a):
            items.append(v[i])
        for i in range(b):
            items.append(v[-(i+1)])
        items.sort()
        d = k - (a + b)
        now = items[:]
        for j in range(min(d, len(now))):
            if now[j] < 0:
                now[j] = 0
        total = sum(now)
        if total > answer:
            answer = total

print(answer)