j, y = map(int, input().split())

# 判定用関数：試合の終了判定と勝者判定
def finished(j, y):
    # 相手が3点以下のときに先に5点とれば勝ち
    if (j >= 5 and y <= 3) or (y >= 5 and j <= 3):
        return True
    # 4対4の同点の場合の特別ルール判定は状態遷移時に行うためここでは終了判定しない
    # ただし6点がある場合の処理は終了とする（6-4か4-6のみ）
    if j == 6 or y == 6:
        return True
    return False

# 4対4状態か？
def is_deuce(j, y):
    return j == 4 and y == 4

# 有効な試合状態かどうか？（ルール上あり得るスコアか）
def valid_state(j, y):
    if not (0 <= j <= 6 and 0 <= y <= 6):
        return False
    if j == 6:
        if y != 4:
            return False
    if y == 6:
        if j != 4:
            return False
    if 0 <= j <= 5 and 0 <= y <= 5:
        # 普通の範囲ならOK（deuceは4-4）
        return True
    return True

# 遷移ルールで次の状態に遷移できるか判定。その際Aはジョウが1点、Bはヤエが1点
def next_states(j, y):
    states = []
    # まず終了済みなら遷移なし
    if finished(j, y):
        return states

    if is_deuce(j, y):
        # Deuce後の処理
        # 4-4から1点取った状態は4-5 or 5-4
        # その後の2点連続ルールや1点ずつ取って引き分けの場合は出力済み
        # 連続2点の状態は6-4か4-6（終了状態）
        states.append(('A', j+1, y))
        states.append(('B', j, y+1))
        return states

    # 通常状態の遷移
    # それぞれ1点加算しても5点以上なら終了判定が後で効く
    # ただしj,yは7以上にはならない（問題の制約）
    if j < 6:
        states.append(('A', j+1, y))
    if y < 6:
        states.append(('B', j, y+1))

    return states

# 経路探索（DFS）
results = []

def dfs(path, j, y):
    if j == target_j and y == target_y:
        results.append(''.join(path))
        return
    for c, nj, ny in next_states(j, y):
        # 先に到達点までのスコアを超えないかつ正当な状態のみ進む
        # 例えば途中でジョウ君の点数が目標値より大きくなるのは意味がない
        if nj <= target_j and ny <= target_y and valid_state(nj, ny):
            dfs(path+[c], nj, ny)

target_j, target_y = j, y

dfs([], 0, 0)

results.sort()
for r in results:
    print(r)