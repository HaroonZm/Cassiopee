def main():
    # Lire les dimensions et le nombre de chemins
    w, h, n = map(int, input().split())
    sx, sy = map(int, input().split())
    sx -= 1
    sy -= 1

    limits = []
    paths = []
    bombs = set()
    for _ in range(n):
        line = list(map(int, input().split()))
        limit = line[0]
        coords = line[1:]
        path = []
        for i in range(limit):
            x = coords[i * 2] - 1
            y = coords[i * 2 + 1] - 1
            path.append((x, y))
        bombs.add(path[-1])
        limits.append(limit)
        paths.append(path)

    rest = []
    for i in range(n):
        if (sx, sy) != paths[i][0]:
            rest.append(i)

    from collections import deque
    que = deque()
    que.append((sx, sy, rest, 0))
    visited = {}
    visited[(sx, sy, tuple(rest), 0)] = True

    directions = [
        (1, 0), (1, -1), (0, -1), (-1, -1),
        (-1, 0), (-1, 1), (0, 1), (1, 1), (0, 0)
    ]

    found = False
    while que:
        x, y, rest, time = que.popleft()
        if len(rest) == 0:
            print(time)
            found = True
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # Vérifier si hors limites ou sur une bombe
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue
            if (nx, ny) in bombs:
                continue

            new_time = time + 1
            removes = []
            bad_move = False
            for i in rest:
                if new_time >= limits[i]:
                    bad_move = True
                    break
                if paths[i][new_time] == (nx, ny):
                    removes.append(i)
            if bad_move:
                continue

            new_rest = []
            for i in rest:
                if i not in removes:
                    new_rest.append(i)

            state = (nx, ny, tuple(new_rest), new_time)
            if state not in visited:
                visited[state] = True
                que.append((nx, ny, new_rest, new_time))

    if not found:
        print(-1)

main()