from heapq import heappush, heappop

h, w = map(int, input().split())

def get_area():
    mp = ["#" * (w + 2)]
    for _ in range(h):
        mp.append("#" + input() + "#")
    mp.append("#" * (w + 2))
    return mp

areas = [get_area()]
times = {}
n = int(input())
for i in range(n):
    times[int(input())] = i + 1
    areas.append(get_area())

for y in range(1, h + 1):
    for x in range(1, w + 1):
        if areas[0][y][x] == "S":
            sx, sy = x, y
        if areas[0][y][x] == "G":
            gx, gy = x, y

que = []
heappush(que, (0, 0, sx, sy, 0))
dic = {}
dic[(0, sx, sy)] = 0
vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
checked = [[False] * (w + 2) for _ in range(h + 2)]
while que:
    score, time, x, y, area_num = heappop(que)
    if (x, y) == (gx, gy):
        print(score)
        break
    time += 1
    if time in times:
        area_num += 1

    area = areas[area_num]
    for dx, dy in vec:
        nx, ny = x + dx, y + dy
        if area[ny][nx] == "#" :continue
        if (time, nx, ny) not in dic:
            if area_num != n:
                dic[(time, nx, ny)] = score + 1
                heappush(que, (score + 1, time, nx, ny, area_num))
            elif not checked[ny][nx]:
                dic[(time, nx, ny)] = score + 1
                checked[ny][nx] = True
                heappush(que, (score + 1, time, nx, ny, area_num))
    if area[y][x] != "#" and not checked[y][x] and ((time, x, y) not in dic or dic[(time, x, y)] > score):
        dic[(time, x, y)] = score
        heappush(que, (score, time, x, y, area_num))
        if area_num == n:checked[y][x] = True
else:
    print(-1)