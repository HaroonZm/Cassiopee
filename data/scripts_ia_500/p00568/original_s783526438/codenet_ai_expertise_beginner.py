def main():
    INF = 10**20
    directions = [(0,1), (0,-1), (-1,0), (1,0)]

    h, w = map(int, input().split())
    mp = []
    for _ in range(h):
        row = list(map(int, input().split()))
        mp.append([-1] + row + [-1])
    mp.insert(0, [-1] * (w+2))
    mp.append([-1] * (w+2))

    is_goal = [[False] * (w+2) for _ in range(h+2)]

    from heapq import heappush, heappop
    queue = []
    heappush(queue, (w, h))

    while queue:
        x, y = heappop(queue)
        if is_goal[y][x]:
            continue
        is_goal[y][x] = True

        if mp[y][x] != 0:
            continue

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if mp[ny][nx] == -1 or is_goal[ny][nx]:
                continue
            heappush(queue, (nx, ny))

    costs = []
    for _ in range(w*h):
        costs.append([[INF] * (w+2) for _ in range(h+2)])

    heappush(queue, (0, 0, 1, 1))  # score, distance, x, y
    costs[0][1][1] = 0

    while queue:
        score, dist, x, y = heappop(queue)

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if mp[ny][nx] == -1:
                continue
            if dist >= w*h - 1:
                continue

            wood = mp[ny][nx]
            new_score = score + (dist * wood * 2) + wood

            if costs[dist+1][ny][nx] > new_score:
                costs[dist+1][ny][nx] = new_score
                heappush(queue, (new_score, dist+1, nx, ny))

    answer = INF
    for d in range(w*h):
        for y in range(1, h+1):
            for x in range(1, w+1):
                if is_goal[y][x]:
                    if costs[d][y][x] < answer:
                        answer = costs[d][y][x]

    print(answer)

main()