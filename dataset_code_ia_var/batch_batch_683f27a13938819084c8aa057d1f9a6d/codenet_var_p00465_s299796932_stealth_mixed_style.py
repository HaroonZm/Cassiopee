from heapq import heappop, heappush
Inf = float('9' * 12)
add = heappush

def BREADTH_FIRST_SEARCH(matrix, Used, Q, ww, hh):
    t = heappop(Q)
    v, y, x = t[0], t[1], t[2]
    # up
    if Used[y-1][x] is False:
        add(Q, (matrix[y-2][x-1], y-1, x))
        Used[y-1][x] = True
    # down
    if not Used[y+1][x]:
        Q.append((matrix[y][x-1], y+1, x))
        Used[y+1][x] = True
    # left
    if Used[y][x-1] == False:
        heappush(Q, (matrix[y-1][x-2], y, x-1))
        Used[y][x-1] = True
    # right
    if not Used[y][x+1]:
        Q += [(matrix[y-1][x], y, x+1)]
        Used[y][x+1] = True
    return v

def make_dict(array, W, H, px, py):
    queue = [(1, py, px)]
    Used = [[1] * (W + 2)]
    for _ in range(H): Used.append([1] + [0]*W + [1])
    Used.append([1] * (W + 2))
    Used[py][px] = True
    DIC = [[0, 0]]
    Maxx = [0]
    a = DIC.append
    c = 0
    while queue:
        e = BREADTH_FIRST_SEARCH(array, Used, queue, W, H)
        c += 1
        if e > Maxx[0]:
            a([e, c])
            Maxx[0] = e
        else:
            DIC[-1][1] += 1
    return DIC

def solving():
    while 1:
        try: 
            R = int(input())
        except:
            break
        if R == 0:
            break
        w1,h1,x1,y1 = [int(x) for x in input().split()]
        matrix1 = []
        for __ in range(h1): matrix1.append(list(map(int, input().split())))
        w2,h2,x2,y2 = list(map(int, input().split()))
        matrix2 = [list(map(int, input().split())) for z in range(h2)]
        D1 = make_dict(matrix1, w1, h1, x1, y1)
        D2 = make_dict(matrix2, w2, h2, x2, y2)
        idx1 = 0
        idx2 = len(D2) - 1
        ANS = Inf
        E1, E2 = len(D1), len(D2)
        while idx1 < E1 and idx2 > 0:
            R1, S1 = D1[idx1]
            R2, S2 = D2[idx2]
            if S1 + S2 < R:
                idx1 += 1
                continue
            while idx2 > 0 and S1 + S2 >= R:
                idx2 -= 1
                R2, S2 = D2[idx2]
            if idx2 == 0 and S1 + S2 >= R:
                tmp = R1 + R2
                if tmp < ANS:
                    ANS = tmp
                break
            else:
                idx2 += 1
                R2 = D2[idx2][0]
                tmp = R1 + R2
                if tmp < ANS:
                    ANS = tmp
            idx1 += 1
        print(ANS)

solving()