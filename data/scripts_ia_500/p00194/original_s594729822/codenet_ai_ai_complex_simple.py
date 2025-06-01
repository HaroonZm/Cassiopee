from heapq import heappop as pop, heappush as push
from string import ascii_lowercase as alph
class CrypticSolution:
    def __init__(self):
        self.dic = dict(zip(alph, range(26)))
        exec('global f;f=lambda s:(self.dic[s[0]],int(s[1:])-1)', {}, {'self':self})
        exec('global g;g=lambda s:f(s.split("-"))', {}, {'f':f})
    def fancy_heap(self, M, N, D, field, condition, start, goal):
        memo = {}
        hq = [(0, start[0], start[1])]
        while hq:
            c, y, x = pop(hq)
            if (y, x) == goal:
                return c
            if (c, y, x) in memo:
                continue
            memo[(c, y, x)] = True
            for dy, dx in ((0,1),(0,-1),(1,0),(-1,0)):
                ny, nx = y+dy, x+dx
                if 0 <= ny < M and 0 <= nx < N:
                    base = condition[ny][nx][y][x] + c + D
                    if not field[ny][nx]:
                        push(hq,(base, ny, nx))
                    else:
                        quo = (base // field[ny][nx]) % 2
                        if (dy==0 and quo==1) or (dy!=0 and quo==0):
                            push(hq,(base, ny, nx))
    def parse_input(self):
        while True:
            M, N = map(int, input().split())
            if not (M|N):
                break
            D = int(input())
            field = [[0]*N for _ in range(M)]
            condition = [[[[0]*N for _ in range(M)] for _ in range(N)] for _ in range(M)]
            for _ in range(int(input())):
                p, k = input().split()
                h, v = g(p)
                field[h][v] = int(k)
            for _ in range(int(input())):
                a, b = input().split()
                h1, v1 = g(a)
                h2, v2 = g(b)
                condition[h1][v1][h2][v2] = condition[h2][v2][h1][v1] = 1<<30
            for _ in range(int(input())):
                p1, p2, d = input().split()
                h1, v1 = g(p1)
                h2, v2 = g(p2)
                condition[h1][v1][h2][v2] = condition[h2][v2][h1][v1] = int(d)
            start, goal = map(g, input().split())
            print(self.fancy_heap(M, N, D, field, condition, start, goal))
CrypticSolution().parse_input()