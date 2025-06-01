from heapq import heappop as pop_heap
from heapq import heappush as push_heap
INF = 10**12  # just a big number, maybe too big but eh

def bfs(grid, visited, queue, width, height):
    val, row, col = pop_heap(queue)  # get smallest item (value, y, x)
    # try to push neighbors if not visited yet
    if row > 0 and not visited[row-1][col]:
        push_heap(queue, (grid[row-1][col], row-1, col))
        visited[row-1][col] = True
    if row + 1 < height and not visited[row+1][col]:
        push_heap(queue, (grid[row+1][col], row+1, col))
        visited[row+1][col] = True
    if col > 0 and not visited[row][col-1]:
        push_heap(queue, (grid[row][col-1], row, col-1))
        visited[row][col-1] = True
    if col + 1 < width and not visited[row][col+1]:
        push_heap(queue, (grid[row][col+1], row, col+1))
        visited[row][col+1] = True
    return val

def make_dic(grid, w, h, start_x, start_y):
    queue = [(1, start_y, start_x)]  # start with value 1?? hmm
    visited = [[False]*w for _ in range(h)]
    visited[start_y][start_x] = True
    dic = [[0, 0]]
    append_to_dic = dic.append
    max_val = 0
    acc = 0

    while queue:
        val = bfs(grid, visited, queue, w, h)
        acc += 1
        if val > max_val:
            append_to_dic([val, acc])
            max_val = val
        else:
            dic[-1][1] += 1  # counts how many times same max val occurs
    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        w1, h1, x1, y1 = map(int, input().split())
        x1 -= 1
        y1 -= 1
        grid1 = [list(map(int, input().split())) for _ in range(h1)]

        w2, h2, x2, y2 = map(int, input().split())
        x2 -= 1
        y2 -= 1
        grid2 = [list(map(int, input().split())) for _ in range(h2)]

        dic1 = make_dic(grid1, w1, h1, x1, y1)
        dic2 = make_dic(grid2, w2, h2, x2, y2)

        end1 = len(dic1)
        end2 = len(dic2)
        ind1 = 0
        ind2 = end2 - 1
        answer = INF

        while ind1 < end1 and ind2 > 0:
            r1, sum1 = dic1[ind1]
            r2, sum2 = dic2[ind2]

            if sum1 + sum2 < R:
                ind1 += 1
                continue

            while ind2 > 0 and sum1 + sum2 >= R:
                ind2 -= 1
                r2, sum2 = dic2[ind2]

            if ind2 == 0 and sum1 + sum2 >= R:
                res = r1 + r2
                if res < answer:
                    answer = res
                break
            else:
                if ind2 < end2 - 1:
                    ind2 += 1
                r2 = dic2[ind2][0]
                res = r1 + r2
                if res < answer:
                    answer = res

            ind1 += 1

        print(answer)

solve()