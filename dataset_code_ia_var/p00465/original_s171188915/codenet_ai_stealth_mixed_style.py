from heapq import heappush, heappop
import sys

inf = 10 ** 12

def expand(queue, grid, visited, W, H):
    val, row, col = heappop(queue)
    # imperative-style exploration
    for dy, dx in ((0,1),(1,0),(0,-1),(-1,0)):
        ny, nx = row+dy, col+dx
        if 0<=ny<H and 0<=nx<W:
            if not visited[ny][nx]:
                heappush(queue, (grid[ny][nx], ny, nx))
                visited[ny][nx] = True
    return val

def build_dict(array, W, H, sx, sy):
    Q = [(1, sy, sx)]
    seen = [[False]*W for _ in range(H)]
    seen[sy][sx] = True
    ret = [[0,0]]
    add = ret.append
    biggest = 0
    cnt = 0
    while len(Q):
        res = expand(Q, array, seen, W, H)
        cnt += 1
        if res > biggest:
            biggest = res
            add([res, cnt])
        else:
            ret[-1][1] += 1
    return ret

def core():
    input_ = sys.stdin.readline
    while 1:
        try:
            R = int(input())
        except:
            break
        if R == 0:
            break
        w1,h1,x1,y1 = map(int, input().split())
        y1-=1; x1-=1
        a1 = [list(map(int, input().split())) for _ in range(h1)]
        w2,h2,x2,y2 = map(int, input().split())
        y2-=1; x2-=1
        a2 = [list(map(int, input().split())) for _ in range(h2)]
        D1 = build_dict(a1,w1,h1,x1,y1)
        D2 = build_dict(a2,w2,h2,x2,y2)
        n1 = len(D1)
        n2 = len(D2)
        idx1 = 0
        idx2 = n2-1
        answer = inf
        # functional style for main loop
        while idx1 < n1 and idx2 > 0:
            val1, s1 = D1[idx1]
            val2, s2 = D2[idx2]
            if s1 + s2 < R:
                idx1 += 1
                continue
            while idx2>0 and s1+s2>=R:
                idx2 -= 1
                val2, s2 = D2[idx2]
            # procedural branch
            if idx2==0 and s1+s2>=R:
                total = val1+val2
                if total < answer: answer = total
                break
            else:
                if idx2 < n2-1:
                    idx2+=1
                val2 = D2[idx2][0]
                total = val1 + val2
                answer = total if total < answer else answer
            idx1 += 1
        print(answer)
core()