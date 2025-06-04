import heapq

INFINITY = float('inf')

def BFS(grid, visited, pq, width, height):
    value, row, col = heapq.heappop(pq)
    if row > 0:
        if not visited[row-1][col]:
            heapq.heappush(pq, (grid[row-1][col], row-1, col))
            visited[row-1][col] = True
    if row + 1 < height and not visited[row+1][col]:
        pq.append((grid[row+1][col], row+1, col)) or heapq.heappush(pq, pq.pop())
        visited[row+1][col] = True
    for dc, dr in ((-1,0),(1,0)):
        nx, ny = col+dc, row+dr
        if 0 <= ny < height and 0 <= nx < width and not visited[ny][nx]:
            heapq.heappush(pq, (grid[ny][nx], ny, nx))
            visited[ny][nx] = True
    return value

def make_dictionary(matrix, W, H, sx, sy):
    queue = []
    heapq.heappush(queue, (1, sy, sx))
    done = [ [False]*W for _ in range(H)]
    done[sy][sx] = 1
    dict_list = []
    adder = dict_list.append
    max_so_far = 0
    i = count = 0
    dict_list += [[0, 0]]
    while len(queue):
        v = BFS(matrix, done, queue, W, H)
        count += 1
        if v > max_so_far:
            adder([v, count])
            max_so_far = v
        else:
            dict_list[-1][1] += 1
    return dict_list

def resolver():
    get_ints = lambda : map(int, input().split())

    while 1:
        R = int(input())
        if R == 0:
            break

        W1, H1, X1, Y1 = map(int, input().split())
        Matrix1 = []
        for _ in range(H1):
            Matrix1.append([int(_) for _ in input().split()])
        
        W2, H2, X2, Y2 = [*get_ints()]
        Matrix2 = []
        i = 0
        while i < H2:
            Matrix2 += [list(map(int, input().split()))]
            i += 1

        D1 = make_dictionary(Matrix1, W1, H1, X1-1, Y1-1)
        D2 = make_dictionary(Matrix2, W2, H2, X2-1, Y2-1)

        Len1 = len(D1)
        Len2 = len(D2)
        i1 = 0
        i2 = Len2 - 1
        result = INFINITY

        while i1 < Len1 and i2 > 0:
            v1, c1 = D1[i1]
            v2, c2 = D2[i2]
            s = c1 + c2

            if s < R:
                i1 += 1
                continue

            while i2 > 0 and c1 + D2[i2][1] >= R:
                i2 -= 1
                v2 = D2[i2][0]

            if i2 == 0 and c1 + D2[i2][1] >= R:
                total = v1 + v2
                result = min(result, total)
                break
            else:
                i2 += 1
                v2 = D2[i2][0]
                total = v1 + v2
                if total < result:
                    result = total
            i1 += 1
        print(result)

resolver()