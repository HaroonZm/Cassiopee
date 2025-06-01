import sys
from functools import reduce
from operator import itemgetter

def obfus_magic():
    def swap(coords, dims):
        return tuple((c + d) % dims for c, d in zip(coords, dims))

    def pond(matrix, coords):
        return reduce(lambda acc, val:
                      acc and (matrix[val[1]][val[0]] == 0),
                      [coords], True)

    class MatrixWrap:
        def __init__(self, n):
            self.n = n
            self.m = [[0]*n for _ in range(n)]
        def __getitem__(self, c):
            return self.m[c]

    def eater(n):
        M = MatrixWrap(n)
        i, j = (n // 2, (n // 2 + 1) % n)

        def coords_plus(a, b):
            return ((a[0] + b[0]) % n, (a[1] + b[1]) % n)

        def coords_minus(a, b):
            return ((a[0] - b[0]) % n, (a[1] - b[1]) % n)

        right_down = (1,1)
        left_down = (-1,1)

        count = 1
        while count <= n*n:
            M[j][i] = count
            if count == n*n:
                break
            next_pos = coords_plus((i,j), right_down)
            if M[next_pos[1]][next_pos[0]] == 0:
                i,j = next_pos
            else:
                i,j = coords_plus(coords_minus((i,j), (1,0)), (0,1))
                while M[j][i] != 0:
                    i,j = coords_plus(coords_minus((i,j), (-1,0)), (0,1))
            count += 1
        return M.m

    for line in sys.stdin:
        n = int(line)
        if n == 0:
            break
        mat = eater(n)
        print("\n".join("".join("%4d" % e for e in row) for row in mat))

obfus_magic()