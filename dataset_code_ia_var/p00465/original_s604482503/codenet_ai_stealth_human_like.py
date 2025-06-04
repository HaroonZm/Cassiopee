from heapq import heappop, heappush
INF = 10 ** 12  # Just a big number

def bfs(grid, visited, heap, width, height):
    v, y, x = heappop(heap)  # get something from the heap

    # neighbor up
    if not visited[y - 1][x]:
        heappush(heap, (grid[y - 2][x - 1], y - 1, x))
        visited[y - 1][x] = True
    # down
    if not visited[y + 1][x]:
        heappush(heap, (grid[y][x - 1], y + 1, x))
        visited[y + 1][x] = True
    # left
    if not visited[y][x - 1]:
        heappush(heap, (grid[y - 1][x - 2], y, x - 1))
        visited[y][x - 1] = True
    # right
    if not visited[y][x + 1]:
        heappush(heap, (grid[y - 1][x], y, x + 1))
        visited[y][x + 1] = True

    return v  # return the value we found

def make_dic(grid, w, h, x, y):
    queue = [(1, y, x)]  # starting with weight 1?
    # Build "visited" matrix with an outer wall
    visited = [[True] + [False for _ in range(w)] + [True] for _ in range(h)]
    visited = [[True] * (w + 2)] + visited + [[True] * (w + 2)]
    visited[y][x] = True
    dic = [[0, 0]]
    Max = 0
    acc = 0
    add_dic = dic.append

    while queue:
        v = bfs(grid, visited, queue, w, h)
        acc += 1
        if v > Max:
            add_dic([v, acc])
            Max = v
        else:
            dic[-1][1] += 1  # increment last count

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
        n1 = len(dic1)
        n2 = len(dic2)
        idx1 = 0
        idx2 = n2 - 1
        ans = INF

        while idx1 < n1 and idx2 > 0:
            val1, cnt1 = dic1[idx1]
            val2, cnt2 = dic2[idx2]
            if cnt1 + cnt2 < R:
                idx1 += 1
                continue
            while idx2 > 0 and cnt1 + cnt2 >= R:
                idx2 -= 1
                val2, cnt2 = dic2[idx2]
            if idx2 == 0 and cnt1 + cnt2 >= R:
                total = val1 + val2
                if ans > total:
                    ans = total
                break
            else:
                idx2 += 1
                total = val1 + dic2[idx2][0]
                if ans > total:
                    ans = total
            idx1 += 1
        print(ans)

# I hope this works, wasn't super careful with edge cases here tbh
solve()