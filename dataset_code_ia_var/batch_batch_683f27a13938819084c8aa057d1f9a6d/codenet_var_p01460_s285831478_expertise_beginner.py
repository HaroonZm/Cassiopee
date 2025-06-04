import sys

def main():
    input = sys.stdin.readline
    N, Q, A, B, C, D, E, F, G = map(int, input().split())
    d = 0
    rx = 0
    ry = 0
    X = list(range(N))
    Y = list(range(N))
    memory = {}

    def rotate(d, x, y):
        if d == 0:
            return x, y
        elif d == 1:
            return y, N - 1 - x
        elif d == 2:
            return N - 1 - x, N - 1 - y
        else:
            return N - 1 - y, x

    for _ in range(Q):
        cmd = input().split()
        c = cmd[0]
        if c[0] == "R":
            if c[1] == "L":
                d = (d - 1) % 4
            elif c[1] == "R":
                d = (d + 1) % 4
            elif c[1] == "H":
                if d % 2 == 1:
                    rx ^= 1
                else:
                    ry ^= 1
            else:  # "RV"
                if d % 2 == 1:
                    ry ^= 1
                else:
                    rx ^= 1
        elif c[0] == "S":
            a = int(cmd[1]) - 1
            b = int(cmd[2]) - 1
            if c[1] == "R":
                if d % 2 == 1:
                    if rx != (d // 2):
                        a, b = N - 1 - a, N - 1 - b
                    X[a], X[b] = X[b], X[a]
                else:
                    if ry != (d // 2):
                        a, b = N - 1 - a, N - 1 - b
                    Y[a], Y[b] = Y[b], Y[a]
            else:  # "SC"
                if d % 2 == 1:
                    if ((d // 2) == 0) != ry:
                        a, b = N - 1 - a, N - 1 - b
                    Y[a], Y[b] = Y[b], Y[a]
                else:
                    if ((d // 2) != 0) != rx:
                        a, b = N - 1 - a, N - 1 - b
                    X[a], X[b] = X[b], X[a]
        elif c[0] == "C":
            y1 = int(cmd[1]) - 1
            x1 = int(cmd[2]) - 1
            y2 = int(cmd[3]) - 1
            x2 = int(cmd[4]) - 1
            x1, y1 = rotate(d, x1, y1)
            x2, y2 = rotate(d, x2, y2)
            if rx:
                x1 = N - 1 - x1
                x2 = N - 1 - x2
            if ry:
                y1 = N - 1 - y1
                y2 = N - 1 - y2
            key1 = (X[x1], Y[y1])
            key2 = (X[x2], Y[y2])
            if key1 not in memory:
                xinn, yinn = key1
                memory[key2] = (yinn * A + xinn * B + A + B) % C
            else:
                memory[key2] = memory[key1]
        else:  # "WR"
            y = int(cmd[1]) - 1
            x = int(cmd[2]) - 1
            v = int(cmd[3])
            x, y = rotate(d, x, y)
            if rx:
                x = N - 1 - x
            if ry:
                y = N - 1 - y
            key = (X[x], Y[y])
            memory[key] = v

    MOD = 10 ** 9 + 7
    h = 314159265
    for y in range(D - 1, E):
        for x in range(F - 1, G):
            x0, y0 = rotate(d, x, y)
            if rx:
                x0 = N - 1 - x0
            if ry:
                y0 = N - 1 - y0
            x0 = X[x0]
            y0 = Y[y0]
            key = (x0, y0)
            if key in memory:
                v = memory[key]
            else:
                v = ((y0 + 1) * A + (x0 + 1) * B) % C
            h = (31 * h + v) % MOD
    print(h)

main()