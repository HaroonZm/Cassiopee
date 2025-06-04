from heapq import heappop, heappush

INF = 10**12  # big number, probably overkill but why not

def bfs(lst, used, pq, w, h):
    # gets min from queue and tries to push neighbors
    v, y, x = heappop(pq)
    if y > 0 and not used[y-1][x]:
        heappush(pq, (lst[y-1][x], y-1, x))
        used[y-1][x] = True
    if y+1 < h and not used[y+1][x]:
        heappush(pq, (lst[y+1][x], y+1, x))
        used[y+1][x] = True
    if x > 0 and not used[y][x-1]:
        heappush(pq, (lst[y][x-1], y, x-1))
        used[y][x-1] = True
    if x+1 < w and not used[y][x+1]:
        heappush(pq, (lst[y][x+1], y, x+1))
        used[y][x+1] = True
    # not 100% sure why return v but seems important
    return v

def make_dic(arr, w, h, sx, sy):
    # builds some kind of list (dictionary? not really...) per min-heap expand
    Q = [(1, sy, sx)]   # starting from (sy, sx)
    used = []
    for i in range(h):
        used.append([False]*w)
    used[sy][sx] = True
    dic = [[0, 0]]
    # shortcut for append, somewhat unnecessary but that's life
    app = dic.append
    maxv = 0
    total = 0
    while Q:
        v = bfs(arr, used, Q, w, h)
        total += 1
        if v > maxv:
            app([v, total])
            maxv = v
        else:
            dic[-1][1] += 1
    return dic

def solve():
    while True:
        R = int(input())
        if R == 0:
            break

        # get 1st field
        w1, h1, x1, y1 = map(int, input().split())
        map1 = []
        for _ in range(h1): map1.append(list(map(int, input().split())))

        # get 2nd field
        w2, h2, x2, y2 = map(int, input().split())
        map2 = []
        for _ in range(h2): map2.append(list(map(int, input().split())))

        dic1 = make_dic(map1, w1, h1, x1-1, y1-1)
        dic2 = make_dic(map2, w2, h2, x2-1, y2-1)

        e1 = len(dic1)
        e2 = len(dic2)
        idx1 = 0
        idx2 = e2-1
        answer = INF

        while idx1 < e1 and idx2 > 0:
            r1, cnt1 = dic1[idx1]
            r2, cnt2 = dic2[idx2]

            if cnt1 + cnt2 < R:
                # not enough, try more from dic1
                idx1 += 1
                continue

            while idx2 > 0 and cnt1 + cnt2 >= R:
                idx2 -= 1
                r2, cnt2 = dic2[idx2]
            if idx2 == 0 and cnt1 + cnt2 >= R:
                s = r1 + r2
                if s < answer:
                    answer = s
                break
            else:
                if idx2 < e2-1:
                    idx2 += 1  # why? bc we went too far? (could maybe explain)
                r2 = dic2[idx2][0]
                s = r1 + r2
                if s < answer:
                    answer = s

            idx1 += 1
        print(answer)
solve()