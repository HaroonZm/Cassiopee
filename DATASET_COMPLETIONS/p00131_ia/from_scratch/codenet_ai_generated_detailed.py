def main():
    import sys

    input = sys.stdin.readline

    # サイズは固定の 10x10
    N = 10

    # 近傍の相対座標（上下左右と自身）
    neighbors = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    # 線形代数のGF(2)上の連立方程式を解く関数
    # 行列Aとベクトルbを与えてAx=bを解く (mod 2)
    # 返すのは解xのリスト
    def gauss_elimination_GF2(A, b):
        # A は MxN (ここは NxN の正方行列を想定)
        M = len(A)
        N = len(A[0])
        # 拡大行列を作成
        mat = [A[i][:] + [b[i]] for i in range(M)]

        rank = 0
        for col in range(N):
            pivot = -1
            for row in range(rank, M):
                if mat[row][col] == 1:
                    pivot = row
                    break
            if pivot == -1:
                continue
            # pivot行とrank行を入れ替え
            mat[rank], mat[pivot] = mat[pivot], mat[rank]
            # pivot行を使って他の行のcol成分を消去
            for row in range(M):
                if row != rank and mat[row][col] == 1:
                    for c in range(col, N + 1):
                        mat[row][c] ^= mat[rank][c]
            rank += 1

        # 後退代入（すでに簡約化されている）
        x = [0] * N
        for row in reversed(range(rank)):
            # ピボット列を探す
            pivot_col = -1
            for col in range(N):
                if mat[row][col] == 1:
                    pivot_col = col
                    break
            if pivot_col == -1:
                # この行はすべて0なので矛盾チェック
                if mat[row][N] != 0:
                    # 解なしだが問題文に必ず解があるので無視
                    return None
                continue
            x[pivot_col] = mat[row][N]
        return x

    T = int(input())
    for _ in range(T):
        # 入力読み込み (10x10の状態)
        initial = []
        for _r in range(N):
            row = list(map(int, input().split()))
            initial.append(row)

        # 線形代数の問題に書き換え
        # 光電管を1次元のインデックスに変換する便宜関数
        def idx(r, c):
            return r * N + c

        size = N * N

        # 行列Aを作る。A[i][j] は、粒子をj番目の位置に通過させたときi番目の光電管に影響があるか（1=影響あり）
        A = [[0] * size for _ in range(size)]

        for r in range(N):
            for c in range(N):
                i = idx(r, c)
                # jが粒子を通過させる位置
                for dr, dc in neighbors:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < N and 0 <= nc < N:
                        j = idx(nr, nc)
                        A[i][j] = 1  # j の操作は i に影響

        # bベクトルは初期状態。すべて0にしたいので b = 初期状態（点灯は1）
        b = []
        for r in range(N):
            for c in range(N):
                b.append(initial[r][c])

        # Ax = b をGF2で解く: x は粒子通過位置
        x = gauss_elimination_GF2(A, b)

        # 結果を出力形式に変換
        result = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                result[r][c] = x[idx(r, c)]

        for r in range(N):
            print(*result[r])


if __name__ == "__main__":
    main()