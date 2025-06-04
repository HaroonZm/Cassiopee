N,M=map(int,input().split())
a=[int(input()) for _ in range(M)]

# 横棒の端点同士が接しない = 同じ高さにある横棒同士のa_iの差は最低2必要
# また、圧縮後は元のあみだくじと辿り方が一致することから
# あみだくじの辿り方は横棒の並び順を保ったまま、横棒をグループ化し（高さ圧縮）
# 各グループ内の横棒のa_i同士が2以上離れている必要がある

# グループ化問題に帰着され、グループ内のa_iが2以上離れている
# つまり、同じグループ内に隣接する数字(差が1)を含まないようにする最小グループ数を求める

# 差が1のa_i同士が同じグループにならないようにグループを作る
# M<=8なので全探索可能

def can_assign(group,a_i):
    for x in group:
        if abs(x - a_i) == 1:
            return False
    return True

res = M
def dfs(k,groups):
    global res
    if k == M:
        res = min(res,len(groups))
        return
    x = a[k]
    for i,g in enumerate(groups):
        if can_assign(g,x):
            g.append(x)
            dfs(k+1,groups)
            g.pop()
    # 新しいグループに入れる
    groups.append([x])
    dfs(k+1,groups)
    groups.pop()

dfs(0,[])
print(res)