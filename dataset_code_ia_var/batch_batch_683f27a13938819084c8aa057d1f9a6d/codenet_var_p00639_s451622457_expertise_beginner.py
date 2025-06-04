import sys

def solve():
    while True:
        D_line = sys.stdin.readline()
        D = float(D_line)
        if D == 0:
            break
        line = sys.stdin.readline()
        px, py, vx, vy = map(float, line.split())
        det = px * vy - py * vx
        if det == 0:
            OP = (px ** 2 + py ** 2) ** 0.5
            dot = px * vx + py * vy
            if dot < 0:
                if OP <= D:
                    print(OP)
                else:
                    print('impossible')
            else:
                d = 2 - OP
                if d <= D:
                    print(d)
                else:
                    print('impossible')
        else:
            print('impossible')

solve()