from itertools import product, permutations, chain, repeat
from functools import lru_cache
def solve():
    N = 4; DEPTH = 5
    G = [list(map(int, input().split())) for _ in range(N)]
    D = ((-1, 0), (0, -1), (1, 0), (0, 1))
    B = 10

    def flatten(M):
        return tuple(chain.from_iterable(M))

    @lru_cache(maxsize=None)
    def recursive(n, *flatR):
        if flatR == (0,) * (N * N):
            return 0
        if n == 0:
            return B
        best = B
        matrix = [list(flatR[i*N:(i+1)*N]) for i in range(N)]
        for i, j in product(range(N), repeat=2):
            stack = [((i, j, d),) for d in range(4)] if matrix[i][j] == 4 else [()]
            history = [(i, j)]
            temp = [row[:] for row in matrix]
            inc = 1
            temp[i][j] = 0 if temp[i][j] == 4 else temp[i][j]+1
            if matrix[i][j] == 4:
                while stack and any(stack):
                    pending = []
                    for group in stack:
                        for x, y, direction in group:
                            dx, dy = D[direction]
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < N and 0 <= ny < N:
                                temp[nx][ny] += 1
                                if temp[nx][ny] == 5:
                                    temp[nx][ny] = 0
                                    inc += 1
                                    pending.append(tuple((nx, ny, d) for d in range(4)))
                    stack = pending
            best = min(best, recursive(n-1, *flatten(temp)) + 1)
        return best

    ans = recursive(DEPTH, *flatten(G))
    print(ans if ans < B else -1)
solve()