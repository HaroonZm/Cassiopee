class Ruiseki2D:
    """二次元累積和を構築する"""
    def __init__(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.ru = [[0] * (self.w + 1) for _ in range(self.h + 1)]

        for i in range(self.h):
            for j in range(self.w):
                self.ru[i + 1][j + 1] = self.ru[i + 1][j] + matrix[i][j]
        for i in range(self.h):
            for j in range(self.w):
                self.ru[i + 1][j + 1] += self.ru[i][j + 1]

    def get_sum(self, hl, hr, wl, wr):
        """[hl, hr), [wl, wr) で囲まれた部分の和を求める"""
        return (self.ru[hr][wr] + self.ru[hl][wl]
                - self.ru[hr][wl] - self.ru[hl][wr])

n, m, q = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]
query = [list(map(int, input().split())) for i in range(q)]

matrix = [[0] * (n + 1) for i in range(n + 1)]
for l, r in info:
    matrix[l][r] += 1
ru = Ruiseki2D(matrix)

for l, r in query:
    ans = ru.get_sum(l, r + 1, l, r + 1)
    print(ans)