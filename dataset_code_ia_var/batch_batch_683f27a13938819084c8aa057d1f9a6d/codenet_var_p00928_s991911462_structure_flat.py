import sys
sys.setrecursionlimit(50000000)
max_c = 101
vec = [(0,2),(2,0),(0,-2),(-2,0)]
try:
    while True:
        log = [-1 for i in range(10001)]
        n, x0, y0, t = map(int, input().split())
        field = []
        for i in range(max_c):
            field.append([])
            for j in range(max_c):
                field[i].append(0)
        i = 0
        while i < n:
            lst = input().split()
            a = int(lst[0])*2
            b = int(lst[1])*2
            c = int(lst[2])*2
            d = int(lst[3])*2
            if b == d:
                mi = min(a, c)
                ma = max(a, c)
                for k in range(mi, ma+1):
                    field[b][k] = 1
            else:
                mi = min(b, d)
                ma = max(b, d)
                for kk in range(mi, ma+1):
                    field[kk][a] = 1
            i += 1
        a = -1
        b = -1
        pt = 0
        i = 0
        while i < t:
            lst = input().split()
            a1 = int(lst[0]) + pt
            d1 = lst[1]
            pt = a1
            b1 = 'NESW'.find(d1)
            log[a1] = b1
            i += 1
        end_t = pt
        end_v = b1
        ans = []
        memo = set({})
        stack = []
        i = 0
        while i < 4:
            stack.append( (0, x0*2, y0*2, i) )
            i += 1
        while stack:
            inf = stack.pop()
            t, x, y, v = inf
            if t > end_t or (log[t] != -1 and not ((v+2)%4 != log[t])) or ((t,x,y,v) in memo):
                continue
            memo.add( (t,x,y,v) )
            if t == end_t:
                ex, ey = vec[end_v]
                if v == end_v:
                    ans.append( (x,y) )
                elif 0 <= y+ey//2 <= 100 and 0 <= x+ex//2 <= 100 and field[y+ey//2][x+ex//2] == 1 and (v+2)%4 != end_v:
                    ans.append( (x,y) )
                continue
            if (log[t] != -1 and v == log[t]) or log[t] == -1:
                i2 = 0
                for ymm in vec:
                    if i2 == (v+2)%4:
                        i2 += 1
                        continue
                    mx = ymm[0]
                    my = ymm[1]
                    nx = x + mx
                    ny = y + my
                    if 0 <= nx <= 100 and 0 <= ny <= 100 and field[ny-my//2][nx-mx//2] == 1:
                        stack.append( (t+1, nx, ny, i2) )
                    i2 += 1
            elif log[t] != -1:
                i2 = 0
                for ymm in vec:
                    if i2 != log[t]:
                        i2 += 1
                        continue
                    mx = ymm[0]
                    my = ymm[1]
                    nx = x + mx
                    ny = y + my
                    if 0 <= nx <= 100 and 0 <= ny <= 100 and field[ny-my//2][nx-mx//2] == 1:
                        stack.append( (t+1, nx, ny, i2) )
                    i2 += 1
        s = set()
        for q in ans:
            s.add(q)
        for q in sorted(s):
            print(q[0]//2, q[1]//2)
except:
    pass