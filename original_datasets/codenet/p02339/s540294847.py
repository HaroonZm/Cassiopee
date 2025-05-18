def way9(ball, box):
    """ball: True / box: False / constraints: 1 or more
    -> ans = S(ball, box)  Sはスターリング数 / 計算量 O(ball * box)
    """
    if ball < box:
        return 0

    # S[i][j] := i個(区別する)をkグループ(区別しない)に分ける場合の数
    S = [[0] * (box + 1) for i in range(ball + 1)] 
    S[0][0] = 1
    for i in range(ball):
        for j in range(box):
            S[i + 1][j + 1] = S[i][j] + S[i][j + 1] * (j + 1)
            S[i + 1][j + 1] %= MOD

    return S[ball][box]

n, k = map(int, input().split())
MOD = 10 ** 9 + 7

print(way9(n, k))