from heapq import heappop as pop
from heapq import heappush as push
INF = 10**12  # just a big number for "infinity"

def bfs(lst, used, que, w, h):
    v, y, x = pop(que)

    # check up
    if not used[y - 1][x]:
        push(que, (lst[y - 2][x - 1], y - 1, x))
        used[y - 1][x] = True

    # check down
    if not used[y + 1][x]:
        push(que, (lst[y][x - 1], y + 1, x))
        used[y + 1][x] = True

    # check left
    if not used[y][x - 1]:
        push(que, (lst[y - 1][x - 2], y, x - 1))
        used[y][x - 1] = True

    # check right
    if not used[y][x + 1]:
        push(que, (lst[y - 1][x], y, x + 1))
        used[y][x + 1] = True

    return v

def make_dic(lst, w, h, x, y):
    # used +1/+1 padding with True to avoid boundary checks
    used = [[True] + [False]*w + [True] for _ in range(h)]
    used.insert(0, [True]*(w+2))
    used.append([True]*(w+2))
    que = [(1, y, x)]  # start with value 1 at (y,x)
    used[y][x] = True
    dic = [[0, 0]]  # will hold pairs of (value, count)
    app = dic.append
    Max = 0
    acc = 0  # accumulator for steps or something like that

    while que:
        v = bfs(lst, used, que, w, h)
        acc += 1
        if v > Max:
            app([v, acc])
            Max = v
        else:
            dic[-1][1] += 1
    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        w1, h1, x1, y1 = map(int, input().split())
        lst1 = [list(map(int, input().split())) for _ in range(h1)]

        w2, h2, x2, y2 = map(int, input().split())
        lst2 = [list(map(int, input().split())) for _ in range(h2)]

        dic1 = make_dic(lst1, w1, h1, x1, y1)
        dic2 = make_dic(lst2, w2, h2, x2, y2)

        end1 = len(dic1)
        end2 = len(dic2)
        ind1 = 0
        ind2 = end2 - 1
        ans = INF

        # match pairs trying to reach sum >= R
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
                rs = r1 + r2
                if rs < ans:
                    ans = rs
                break
            else:
                ind2 += 1
                r2 = dic2[ind2][0]
                rs = r1 + r2
                if rs < ans:
                    ans = rs

            ind1 += 1
        print(ans)

# finally run it
solve()