import heapq
class point:
    def __init__(self, total, use, place):
        self.total = total
        self.use = use
        self.place = place

    def __lt__(self, other):
        return self.total < other.total or (self.total == other.total and self.use > self.use)

w, h, n = map(int, input().split())
if w == h == 1:
    print(0)
    exit()
lights = [list(map(int, input().split())) for _ in range(n)]
que = []
mins = []
for i, j in enumerate(lights):
    dis = j[0] + j[1] - 2
    heapq.heappush(que, point(dis, dis, i))
    mins.append(point(dis, dis, i))
ans = 100000
while que:
    top = heapq.heappop(que)
    ans = min(ans, top.total + max(0, abs(w - lights[top.place][0]) + abs(h - lights[top.place][1]) - top.use))
    for i in range(len(lights)):
        dis = abs(lights[top.place][0] - lights[i][0]) + abs(lights[top.place][1] - lights[i][1]) - 1
        use = max(0, dis - top.use)
        total = top.total + use
        new = point(total, use, i)
        if mins[i] > new:
            mins[i] = new
            heapq.heappush(que, new)
print(ans)