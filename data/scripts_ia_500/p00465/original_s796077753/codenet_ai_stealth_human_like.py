from heapq import heappop as pop_heap
from heapq import heappush as push_heap
INF = 10**12  # just a big number, for comparisons

def bfs(grid, visited, queue, width, height):
    value, row, col = pop_heap(queue)
    # check up
    if row > 0 and not visited[row - 1][col]:
        push_heap(queue, (grid[row - 1][col], row - 1, col))
        visited[row - 1][col] = True
    # check down
    if row + 1 < height and not visited[row + 1][col]:
        push_heap(queue, (grid[row + 1][col], row + 1, col))
        visited[row + 1][col] = True
    # check left
    if col > 0 and not visited[row][col - 1]:
        push_heap(queue, (grid[row][col - 1], row, col - 1))
        visited[row][col - 1] = True
    # check right
    if col + 1 < width and not visited[row][col + 1]:
        push_heap(queue, (grid[row][col + 1], row, col + 1))
        visited[row][col + 1] = True
    return value

def make_dic(grid, width, height, start_x, start_y):
    queue = [(1, start_y, start_x)]  # weird that it starts with 1 value?
    visited = [[False] * width for _ in range(height)]
    visited[start_y][start_x] = True
    result = [[0, 0]]
    append_res = result.append  # speed trick? meh.
    max_val = 0
    count = 0

    while queue:
        val = bfs(grid, visited, queue, width, height)
        count += 1
        if val > max_val:
            append_res([val, count])
            max_val = val
        else:
            result[-1][1] += 1  # increment the count of last max_val
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

        dic1 = make_dic(grid1, w1, h1, x1 - 1, y1 - 1)
        dic2 = make_dic(grid2, w2, h2, x2 - 1, y2 - 1)

        len1 = len(dic1)
        len2 = len(dic2)
        idx1 = 0
        idx2 = len2 - 1
        answer = INF

        while idx1 < len1 and idx2 > 0:
            r1, sum1 = dic1[idx1]
            r2, sum2 = dic2[idx2]

            if sum1 + sum2 < R:
                idx1 += 1
                continue

            while idx2 > 0 and sum1 + sum2 >= R:
                idx2 -= 1
                r2, sum2 = dic2[idx2]

            if idx2 == 0 and sum1 + sum2 >= R:
                temp_res = r1 + r2
                if temp_res < answer:
                    answer = temp_res
                break
            else:
                if idx2 < len2 - 1:
                    idx2 += 1
                r2 = dic2[idx2][0]
                temp_res = r1 + r2
                if temp_res < answer:
                    answer = temp_res

            idx1 += 1
        print(answer)

solve()