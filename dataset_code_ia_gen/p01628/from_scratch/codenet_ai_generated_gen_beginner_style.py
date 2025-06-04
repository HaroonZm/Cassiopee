N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]

# 横棒の端点が接するかどうかを判定する関数
def can_stack(h1, h2):
    # 同じ高さに出来るのは、端点が重ならない場合のみ
    # 端点は両端の縦棒番号(ai と ai+1)
    # 重なるとは、端点同士が同じ縦棒番号を持つこと
    # h1とh2はそれぞれ横棒の縦棒番号
    # 端点は {h1, h1+1} と {h2, h2+1}
    set1 = {h1, h1+1}
    set2 = {h2, h2+1}
    # 接するとは、端点が同じ縦棒番号を持つこと
    # ここでは「接していない」が条件なので、接していたら重ねられない
    return set1.isdisjoint(set2)

# M本の横棒をグループ分けする問題。
# 同じ高さは横棒の集合グループ。
# グループ内はどの二つの横棒もcan_stack(True)でなければならない。

# まずM本の横棒を順に高さに割り当てていく。
# その高さは1から最大Mまで。

# 条件2：圧縮後のあみだくじを辿った結果と一致していること。
# これは、圧縮後も順序関係が変わらないことを保証する簡単な条件と解釈して良さそう。
# なので同じ順序で横棒が上から下にあること（高さが小さい順）が必要。
# ただし、また、同じ高さにまとめることができるのは端点が重ならない横棒のみ。

# 簡単に言うと、隣接する横棒を同じ高さにまとめられるかはcan_stackで確認。
# 横棒は上から順に並ぶので、例えば、グループにまとめるとき隣接しない横棒は同じ高さに置けない。

# この問題は、M個の横棒を高さというグループに分けて、
# 各グループの横棒は端点が重ならない集合で、
# グループ間は元の順序通りに並べる問題となる。

# ここでは単純に、1 <= height <= Mとして、M本の横棒を高さ割り当てするときの全探索をする。

ans = M  # 最悪は高さ圧縮できず、Mとなる。

# 横棒同士の端点の衝突テーブルを作る
conflict = [[False]*M for _ in range(M)]
for i in range(M):
    for j in range(M):
        if i == j:
            conflict[i][j] = False
        else:
            # 横棒の縦棒位置
            h1 = a[i]
            h2 = a[j]
            # 端点共有してたらTrue（衝突あり）
            conflict[i][j] = not can_stack(h1, h2)

# 使うのは全探索
# assignment[i] = 横棒iの高さ (1〜M)
def check(assignment):
    # 各高さグループに属する横棒を取り出して端点がぶつかっていないか確認
    groups = {}
    for i, h in enumerate(assignment):
        if h not in groups:
            groups[h] = []
        groups[h].append(i)
    for g in groups.values():
        for i1 in range(len(g)):
            for i2 in range(i1+1, len(g)):
                if conflict[g[i1]][g[i2]]:
                    return False
    # 高さの順に横棒は並んでいる必要がある
    # assignment[i] < assignment[j]であれば、i番目横棒はj番目横棒より上にある
    # 解は必ず元の順序を保てば良いのでこれは元の順番の昇順となる
    # 因みにassignmentが高さであるため、i<j なら assignment[i] ≤ assignment[j]は必要。
    for i in range(M-1):
        if assignment[i] > assignment[i+1]:
            return False
    return True

def dfs(i, assignment):
    global ans
    if i == M:
        height_num = len(set(assignment))
        if height_num < ans:
            if check(assignment):
                ans = height_num
        return
    for h in range(1, ans):
        assignment.append(h)
        # 部分的にcheckの簡易判定（今のところ端点のみで早期除外）
        # 直前の棒を新しい高さに置いたときの衝突はないかだけチェック
        ok = True
        last = assignment[-1]
        for j in range(i):
            if assignment[j] == last and conflict[j][i]:
                ok = False
                break
        if ok:
            dfs(i+1, assignment)
        assignment.pop()

dfs(0, [])
print(ans)