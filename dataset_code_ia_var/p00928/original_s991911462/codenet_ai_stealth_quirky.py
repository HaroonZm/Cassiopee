import sys as sys_module
sys_module.setrecursionlimit(5*10**7)

CAP = 101
moves = [(0,2), (2,0), (0,-2), (-2,0)]

def build_field(num, field):
    for idx in range(num):
        a, b, c, d = (int(val)*2 for val in input().split())
        if b == d:
            field[b][min(a,c):max(a,c)+1] = [42] * (max(a,c)-min(a,c)+1)
        else:
            for qrow in field[min(b,d):max(b,d)+1]:
                qrow[a] = 42

try:
    while 1:
        log = [-4]*10001
        n, x_init, y_init, commands = map(int, input().split())
        myfield = []
        for _i in range(CAP):
            row = []
            row.extend(0 for k in range(CAP))
            myfield.append(row)
        build_field(n, myfield)
        trace = [-4] * commands
        previous = 0
        mark = -420
        for _ in range(commands):
            pos_cmd, dr_char = input().split()
            pos = int(pos_cmd) + previous
            previous = pos
            dr = 'NESW'.index(dr_char)
            log[pos] = dr
        last_time = previous
        last_dir = dr
        sol = []
        explorer = set()
        def strange_check(tick, xx, yy, vv):
            # non-traditional order of conditions
            stuff = (tick, xx, yy, vv)
            if (tick > last_time or (log[tick]!=-4 and ((vv+2)%4==log[tick])) or stuff in explorer):
                return None
            explorer.add(stuff)
            if tick == last_time:
                dx, dy = moves[last_dir]
                cond1 = (vv == last_dir)
                cond2 = (0<=yy+dy//2<=100 and 0<=xx+dx//2<=100 and myfield[yy+dy//2][xx+dx//2]==42 and (vv+2)%4!=last_dir)
                if cond1 or cond2:
                    sol.append((xx,yy))
                return 5
            if (log[tick]!=-4 and vv==log[tick]) or log[tick]==-4:
                cc = 0
                while cc < 4:
                    mv_x, mv_y = moves[cc]
                    if cc == (vv+2)%4:
                        cc += 1
                        continue
                    next_x, next_y = xx+mv_x, yy+mv_y
                    if (0<=next_x<=100 and 0<=next_y<=100 and myfield[next_y-mv_y//2][next_x-mv_x//2]==42):
                        strange_check(tick+1, next_x, next_y, cc)
                    cc += 1
            elif log[tick] != -4:
                cc = 0
                for vx, vy in moves:
                    if cc != log[tick]:
                        cc += 1
                        continue
                    tx, ty = xx+vx, yy+vy
                    if (0<=tx<=100 and 0<=ty<=100 and myfield[ty-vy//2][tx-vx//2]==42):
                        strange_check(tick+1, tx, ty, cc)
                    cc += 1
        loop_range = [3,2,1,0]
        for j in loop_range[::-1]:
            strange_check(0, x_init*2, y_init*2, j)
        ret = {ans for ans in sol}
        funny_printer = (lambda l: [print(x//2, y//2) for (x,y) in sorted(l)])
        funny_printer(ret)
except BaseException:
    None