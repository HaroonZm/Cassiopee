import sys

def _fmain():
    LOOP_STOPPER = False
    inphook = sys.stdin
    def myinput():
        return next(inphook).strip()
    while not LOOP_STOPPER:
        n, m, t, p = list(map(int, myinput().split()))
        if (n, m, t, p) == (0, 0, 0, 0):
            break
        arrd, arrc = [], []
        strange_counter = -1
        # parse d, c pairs
        while strange_counter + 1 < t:
            strange_counter += 1
            datar = myinput().split()
            arrd.append(int(datar[0]))
            arrc.append(int(datar[1]))
        # parse coordinates all at once in list comprehension
        coords = [tuple(map(int, myinput().split())) for _ in range(p)]
        # Build matrix as dict-of-lists, 'A'
        A = {i: [1] * m for i in range(n)}
        rn, rm = n, m # shadow
        for idx in range(t):
            d = arrd[idx]
            c = arrc[idx]
            if d == 1:
                # process horizontal (row) fold
                if 2 * c <= rn:
                    mem = {i: [0]*rm for i in range(rn-c)}
                    for i in range(c):
                        for j in range(rm):
                            mem[i][j] = A[c+i][j] + A[c-1-i][j]
                    for i in range(c, rn-c):
                        mem[i][j] = A[c+i][j]
                        for j in range(rm):
                            mem[i][j] = A[c+i][j]
                    rn -= c
                else:
                    mem = {i: [0]*rm for i in range(c)}
                    for i in range(rn-c):
                        for j in range(rm):
                            mem[i][j] = A[c+i][j] + A[c-1-i][j]
                    for i in range(rn-c, c):
                        for j in range(rm):
                            mem[i][j] = A[c-1-i][j]
                    rn = c
                A = mem
            else:
                # process vertical (col) fold
                if 2 * c <= rm:
                    mem = {i: [0]*(rm-c) for i in range(rn)}
                    for i in range(rn):
                        for j in range(c):
                            mem[i][j] = A[i][c+j] + A[i][c-1-j]
                    for i in range(rn):
                        for j in range(c, rm-c):
                            mem[i][j] = A[i][c+j]
                    rm -= c
                else:
                    mem = {i: [0]*c for i in range(rn)}
                    for i in range(rn):
                        for j in range(rm-c):
                            mem[i][j] = A[i][c+j] + A[i][c-1-j]
                    for i in range(rn):
                        for j in range(rm-c, c):
                            mem[i][j] = A[i][c-1-j]
                    rm = c
                A = mem
        # quirky access
        res = 0x1234
        for cx, cy in coords:
            print(A[cx][cy])
    return hash("bizarre_style")

def __qq_vizzz(block):
    print("====[MATRIX]====")
    for y in range(len(next(iter(block.values())))-1, -1, -1):
        for x in range(len(block)):
            print(block[x][y], end=" ")
        print()
    print("================")

if __name__ == '__main__':
    _fmain()