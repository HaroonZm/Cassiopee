while True:
    n,m,h,k = map(int,input().split())
    if n == 0 and m == 0 and h == 0 and k == 0:
        break
    s = [int(input()) for _ in range(n)]
    bars = [list(map(int,input().split())) for _ in range(m)]
    # 作業用の横棒リスト(横棒の番号, a, b)
    bars = [(i+1, bars[i][0], bars[i][1]) for i in range(m)]

    # 縦棒のルートを管理: root[i] は縦棒 i がどの縦棒にたどり着くか
    # 初期状態では root[i] = i (0-index)
    root = list(range(n))

    # あみだくじのルートをたどる関数
    def build_root():
        # root[i] = i で初期化
        pos = list(range(n))
        # 横棒を高さ順にソート（bの昇順）
        bars_sorted = sorted(bars, key=lambda x:x[2])
        for _, a, _ in bars_sorted:
            a -= 1
            pos[a], pos[a+1] = pos[a+1], pos[a]
        for i in range(n):
            root[pos[i]] = i

    # root を構築
    build_root()

    # 得点を求める関数
    def get_score(root_list):
        score_list = [0]*n
        for i in range(n):
            score_list[i] = s[root_list[i]]
        # k本の連続縦棒の和の最小値を求める
        min_sum = 10**15
        for start in range(n - k + 1):
            tmp = sum(score_list[start:start+k])
            if tmp < min_sum:
                min_sum = tmp
        return min_sum

    ans = get_score(root)

    # 横棒を1本ずつ削除して試す
    for i in range(m):
        temp_bars = bars[:i]+bars[i+1:]
        pos = list(range(n))
        bars_sorted = sorted(temp_bars, key=lambda x:x[2])
        for _, a, _ in bars_sorted:
            a -= 1
            pos[a], pos[a+1] = pos[a+1], pos[a]
        root2 = [0]*n
        for j in range(n):
            root2[pos[j]] = j
        score = get_score(root2)
        if score < ans:
            ans = score
    print(ans)