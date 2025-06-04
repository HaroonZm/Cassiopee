import heapq

class Point:
    def __init__(self, total, use, place):
        self.total = total
        self.use = use
        self.place = place

    def __lt__(self, other):
        if self.total == other.total:
            return self.use > other.use
        return self.total < other.total

w, h, n = map(int, input().split())

if w == 1 and h == 1:
    print(0)
    exit()

lights = []
for _ in range(n):
    x, y = map(int, input().split())
    lights.append([x, y])

queue = []
mins = []
for i in range(len(lights)):
    dis = lights[i][0] + lights[i][1] - 2
    item = Point(dis, dis, i)
    heapq.heappush(queue, item)
    mins.append(item)

ans = 100000
while queue:
    current = heapq.heappop(queue)
    x, y = lights[current.place]
    temp = current.total + max(0, abs(w - x) + abs(h - y) - current.use)
    if temp < ans:
        ans = temp
    for i in range(len(lights)):
        nx, ny = lights[i]
        dis = abs(x - nx) + abs(y - ny) - 1
        use = max(0, dis - current.use)
        total = current.total + use
        new_point = Point(total, use, i)
        if mins[i].total > new_point.total or (mins[i].total == new_point.total and mins[i].use < new_point.use):
            mins[i] = new_point
            heapq.heappush(queue, new_point)

print(ans)