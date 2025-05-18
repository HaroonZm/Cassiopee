n, m = map(int, input().split())

roads = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    roads[a-1] += 1
    roads[b-1] += 1

for road in roads:
    print(road)