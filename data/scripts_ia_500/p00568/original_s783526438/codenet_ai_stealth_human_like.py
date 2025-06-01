from heapq import heappush, heappop

def main():
    INF = 10**20
    directions = [(0,1), (0,-1), (-1,0), (1,0)]  # Up, Down, Left, Right - standard moves I guess

    h, w = map(int, input().split())
    # Padding the map with -1 around the borders to avoid boundary checks everywhere
    mp = [[-1]*(w+2)]
    for _ in range(h):
        row = list(map(int, input().split()))
        mp.append([-1] + row + [-1])
    mp.append([-1]*(w+2))

    is_goal = [[False]*(w+2) for _ in range(h+2)]

    # This queue will hold nodes to explore for the "goal" detection
    que = []
    heappush(que, (w, h))  # Starting from bottom right? Seems odd, but okay

    while que:
        x, y = heappop(que)
        is_goal[y][x] = True
        if mp[y][x] != 0:
            continue  # Only expand from empty spots

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if mp[ny][nx] == -1 or is_goal[ny][nx]:
                continue
            heappush(que, (nx, ny))

    # costs[distance][y][x] = minimal score to get to (x,y) in distance steps
    costs = [[[INF]*(w+2) for _ in range(h+2)] for _ in range(w*h)]
    que = []
    heappush(que, (0, 0, 1, 1))  # score=0, dist=0, start at (1,1)
    costs[0][1][1] = 0

    while que:
        score, dist, x, y = heappop(que)
        # This line could slow things if better paths already found
        # but no early prune implemented, might be a slight inefficiency here

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            wood = mp[ny][nx]
            if wood == -1:
                continue

            if dist >= w*h - 1:
                continue  # avoid overflow

            new_score = score + dist*wood*2 + wood
            if costs[dist+1][ny][nx] > new_score:
                costs[dist+1][ny][nx] = new_score
                heappush(que, (new_score, dist+1, nx, ny))

    # Find minimum score among all reachable goal cells, considering all distances
    ans = INF
    for d in range(w*h):
        for y in range(1, h+1):
            for x in range(1, w+1):
                if is_goal[y][x]:
                    ans = min(ans, costs[d][y][x])

    print(ans)

main()