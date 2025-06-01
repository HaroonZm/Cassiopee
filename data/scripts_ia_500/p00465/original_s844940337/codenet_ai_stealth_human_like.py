from heapq import heappop as pop, heappush as push

INF = 10**12  # just a big number, kind of arbitrary

def bfs(grid, visited, queue, width, height):
    val, y, x = pop(queue)  # pop the smallest val
    # Check neighbors, add them if not visited
    if y > 0 and not visited[y - 1][x]:
        push(queue, (grid[y - 1][x], y - 1, x))
        visited[y - 1][x] = True
    if y + 1 < height and not visited[y + 1][x]:
        push(queue, (grid[y + 1][x], y + 1, x))
        visited[y + 1][x] = True
    if x > 0 and not visited[y][x - 1]:
        push(queue, (grid[y][x - 1], y, x - 1))
        visited[y][x - 1] = True
    if x + 1 < width and not visited[y][x + 1]:
        push(queue, (grid[y][x + 1], y, x + 1))
        visited[y][x + 1] = True
    return val

def make_dic(grid, width, height, start_x, start_y):
    queue = [(1, start_y, start_x)]  # start val hardcoded as 1? Might want to double check
    visited = [[False]*width for _ in range(height)]
    visited[start_y][start_x] = True
    result = [[0, 0]]  # will store [max_value_so_far, count]
    append_ = result.append  # small micro-optimization maybe unnecessary
    max_val = 0
    acc = 0  # accumulative count of visited nodes or steps?

    while queue:
        val = bfs(grid, visited, queue, width, height)
        acc += 1
        if val > max_val:
            append_([val, acc])
            max_val = val
        else:
            result[-1][1] += 1
    return result

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        w1, h1, x1, y1 = map(int, input().split())
        grid1 = [list(map(int, input().split())) for _ in range(h1)]

        w2, h2, x2, y2 = map(int, input().split())
        grid2 = [list(map(int, input().split())) for _ in range(h2)]

        dic1 = make_dic(grid1, w1, h1, x1 -1, y1 -1)
        dic2 = make_dic(grid2, w2, h2, x2 -1, y2 -1)

        len1 = len(dic1)
        len2 = len(dic2)
        i, j = 0, len2 -1
        ans = INF

        # Trying to find minimum sum of radii such that sum of counts >= R
        while i < len1 and j > 0:
            r1, s1 = dic1[i]
            r2, s2 = dic2[j]

            if s1 + s2 < R:
                i += 1
                continue

            while j > 0 and s1 + s2 >= R:
                j -= 1
                r2, s2 = dic2[j]

            if j == 0 and s1 + s2 >= R:
                candidate = r1 + r2
                if candidate < ans:
                    ans = candidate
                break
            else:
                j += 1
                r2 = dic2[j][0]
                candidate = r1 + r2
                if candidate < ans:
                    ans = candidate
            i += 1

        print(ans)

solve()