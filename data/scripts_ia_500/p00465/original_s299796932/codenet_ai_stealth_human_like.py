from heapq import heappop as pop
from heapq import heappush as push

INF = 10**12  # big number used as infinity basically

def bfs(grid, visited, queue, width, height):
    val, y, x = pop(queue)
    # checking neighbors in the order: up, down, left, right
    if not visited[y - 1][x]:
        push(queue, (grid[y - 2][x - 1], y - 1, x))
        visited[y - 1][x] = True

    if not visited[y + 1][x]:
        push(queue, (grid[y][x - 1], y + 1, x))
        visited[y + 1][x] = True

    if not visited[y][x - 1]:
        push(queue, (grid[y - 1][x - 2], y, x - 1))
        visited[y][x - 1] = True

    if not visited[y][x + 1]:
        push(queue, (grid[y - 1][x], y, x + 1))
        visited[y][x + 1] = True

    return val

def make_dic(grid, width, height, start_x, start_y):
    queue = [(1, start_y, start_x)]  # starting from value 1 for some reason

    # creating a visited matrix padded with True so edges are always considered visited
    visited = [[True] * (width + 2)]
    for _ in range(height):
        visited.append([True] + [False] * width + [True])
    visited.append([True] * (width + 2))

    visited[start_y][start_x] = True  # mark start as visited

    dic = [[0,0]]
    append_dic = dic.append
    max_val = 0
    acc = 0

    while queue:
        val = bfs(grid, visited, queue, width, height)
        acc += 1
        if val > max_val:
            append_dic([val, acc])
            max_val = val
        else:
            dic[-1][1] += 1

    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        w1, h1, x1, y1 = map(int, input().split())
        grid1 = [list(map(int, input().split())) for _ in range(h1)]
        
        w2, h2, x2, y2 = map(int, input().split())
        grid2 = [list(map(int, input().split())) for _ in range(h2)]

        dic1 = make_dic(grid1, w1, h1, x1, y1)
        dic2 = make_dic(grid2, w2, h2, x2, y2)

        end1 = len(dic1)
        end2 = len(dic2)
        idx1 = 0
        idx2 = end2 - 1
        ans = INF

        # okay this is some kind of two pointer approach I guess...
        while idx1 < end1 and idx2 > 0:
            r1, sum1 = dic1[idx1]
            r2, sum2 = dic2[idx2]

            if sum1 + sum2 < R:
                idx1 += 1
                continue

            while idx2 > 0 and sum1 + sum2 >= R:
                idx2 -= 1
                r2, sum2 = dic2[idx2]

            if idx2 == 0 and sum1 + sum2 >= R:
                res = r1 + r2
                if res < ans:
                    ans = res
                break
            else:
                idx2 += 1
                r2 = dic2[idx2][0]
                res = r1 + r2
                if res < ans:
                    ans = res

            idx1 += 1

        print(ans)

solve()