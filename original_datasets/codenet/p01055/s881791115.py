from collections import deque

def main():
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
        line = line[1:]
        path = []
        for i in range(limit):
            x = line[i * 2] - 1
            y = line[i * 2 + 1] - 1
            path.append((x, y))
        bombs.add(path[-1])
        limits.append(limit)
        paths.append(path)

    rest = [i for i in range(n) if (sx, sy) != paths[i][0]]
    que = deque()
    que.append((sx, sy, rest, 0))
    dic = {}
    dic[(sx, sy, tuple(rest), 0)] = True
    vec = ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (0, 0))
    while que:
        x, y, rest, time = que.popleft()
        if not rest:
            print(time)
            break

        for dx, dy in vec:
            nx, ny = x + dx, y + dy
            if (nx, ny) in bombs or (not 0 <= nx < w) or (not 0 <= ny < h):continue
            new_time = time + 1
            removes = []
            cont_flag = False
            for i in rest:
                if new_time >= limits[i]:
                    cont_flag = True
                    break
                if paths[i][new_time] == (nx, ny):
                    removes.append(i)
            if cont_flag:continue
            new_rest = [i for i in rest if i not in removes]
            if (nx, ny, tuple(new_rest), new_time) not in dic:
                dic[(nx, ny, tuple(new_rest), new_time)] = True
                que.append((nx, ny, new_rest, new_time))
    else:
        print(-1)

main()