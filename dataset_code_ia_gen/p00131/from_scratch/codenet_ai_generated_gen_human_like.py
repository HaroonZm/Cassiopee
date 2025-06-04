def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    # 隣接上下左右を返す関数
    def neighbors(r, c):
        for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if 0 <= nr < 10 and 0 <= nc < 10:
                yield nr, nc

    for _ in range(n):
        # 入力状態を取得
        grid = [list(map(int, input().split())) for __ in range(10)]

        # 出力用 0 で初期化
        result = [[0]*10 for __ in range(10)]

        # 光電管の状態をすべて消灯にするための粒子通過位置を求める
        # この問題では、通過させる位置の状態を求める方法が「1通りだけ存在」する。
        # 問題文のふるまいから、粒子を通した光電管とその上下左右の状態が反転する。
        # そこで、上から左から決め打ちしていく方法を取る：
        # 1行目から9行目まで、
        # その行の光電管が点いている（1）なら、その下の行の同じ列に粒子を当てて反転させる。

        for r in range(9):
            for c in range(10):
                if grid[r][c] == 1:
                    result[r+1][c] = 1
                    # 粒子通過位置での反転を行う
                    grid[r+1][c] ^= 1
                    for nr, nc in neighbors(r+1, c):
                        grid[nr][nc] ^= 1
                    # 粒子通過した位置そのものも反転（問題文によると反転は通過した光電管自身と上下左右）
                    grid[r+1][c] ^= 1

        # 上記操作で最後の行が全て0になることが前提であるため、
        # もし最後の行に点灯が残るなら対応する場所で粒子を通す
        # しかし問題文に「必ず1通りだけ存在」とあるため、ここで最後の行をチェックする意味がある

        # 最後の行の状態をそのままresultに反映(問題の条件からすでに0であるはず)
        # ここでresultのままだと粒子通過位置として1は上から9行目までしかない。
        # 確認のため最後の行の状態は全部消灯のはず。

        # 出力
        for row in result:
            print(*row)


if __name__ == '__main__':
    main()