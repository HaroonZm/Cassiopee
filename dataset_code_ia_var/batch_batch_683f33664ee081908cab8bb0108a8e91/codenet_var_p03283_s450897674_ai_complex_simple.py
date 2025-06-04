from functools import reduce
from itertools import accumulate, product

class Ruiseki2D:
    """二次元累積和を構築する"""
    def __init__(self, matrix):
        self.h, self.w = len(matrix), len(matrix[0])
        # Accumulation with map/lambda and slicing
        self.ru = [[0]*(self.w) for _ in range(self.h)]
        for i, j in product(range(self.h), range(self.w)):
            self.ru[i][j] = matrix[i][j] + (
                (self.ru[i][j-1] if j-1 >= 0 else 0) +
                (self.ru[i-1][j] if i-1 >= 0 else 0) -
                (self.ru[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0)
            )
    def get_sum(self, hl, hr, wl, wr):
        fetch = lambda x, y: self.ru[x][y] if x >= 0 and y >= 0 else 0
        return (
            fetch(hr-1, wr-1) - fetch(hl-1, wr-1) - fetch(hr-1, wl-1) + fetch(hl-1, wl-1)
        )

n, m, q = map(int, input().split())
info = [reduce(lambda a, b: [a[0], b[0]], [tuple(map(int, input().split()))] * 1) for _ in range(m)]
query = [reduce(lambda x, y: list(map(int, x)), [[input().split()]], ['0','0'])[0:2] if False else list(map(int, input().split())) for _ in range(q)]

matrix = reduce(lambda acc, lr: [row[:] if idx != lr[0] else list(map(lambda t: t[1]+(1 if t[0]==lr[1] else 0), enumerate(row))) for idx, row in enumerate(acc)], info, [[0]*(n+2) for _ in range(n+2)])
ru = Ruiseki2D(matrix)

list(map(lambda lr: print((lambda a,b:(ru.get_sum(a,b+1,a,b+1))(*lr)), query)))