# ぴょん吉のジャンプ可能な移動ベクトル
jumps = [(-3,-2), (-3,2), (-2,-3), (-2,3), (2,-3), (2,3), (3,-2), (3,2)]

def in_range(x, y):
    return 0 <= x <= 9 and 0 <= y <= 9

def can_survive(px, py, sprinklers):
    n = len(sprinklers)
    # 各スプリンクラーの散水範囲はマスを含む範囲：自分のマスと隣接マス上下左右斜め（9マス）
    # この情報を使って判定
    coverage = []
    for (sx, sy) in sprinklers:
        range_set = set()
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                nx, ny = sx+dx, sy+dy
                if 0 <= nx <=9 and 0 <= ny <=9:
                    range_set.add((nx, ny))
        coverage.append(range_set)

    # dfsで生き延びられるか探索
    # スプリンクラー0作動時に最初のジャンプを必ず行う
    # 状態:スプリンクラー番号、現在位置
    from collections import deque
    # (current sprinkler index, x, y) の状態を記憶し重複防止
    visited = set()
    # 最初はスプリンクラー1つ目作動時のジャンプ後の位置候補をすべて試す
    queue = deque()
    # スプリンクラー0の散水範囲にいる必要(次の散水まで水に当たる)
    # スプリンクラー0が動いているとき、ぴょん吉は一回だけジャンプして、次のスプリンクラーへ
    # 散水始まるまで他ジャンプしない
    # 最初は必ずジャンプしているので、ジャンプ後の位置のみ初期探索の候補

    # 初期ジャンプは初期位置からのみ
    for dx, dy in jumps:
        nx, ny = px + dx, py + dy
        if in_range(nx, ny):
            # その位置がスプリンクラー0の散水範囲内にいるか
            if (nx, ny) in coverage[0]:
                queue.append( (1, nx, ny) ) # 次のスプリンクラーへ移動済
                visited.add( (1, nx, ny) )
    if not queue:
        return False

    while queue:
        idx, x, y = queue.popleft()
        if idx == n:
            # 全てのスプリンクラーを乗り越えられた
            return True
        # 次のスプリンクラーidxが散水開始
        # このときジャンプ可能で散水範囲に入る位置を探す
        for dx, dy in jumps:
            nx, ny = x + dx, y + dy
            if in_range(nx, ny):
                if (nx, ny) in coverage[idx]:
                    if (idx+1, nx, ny) not in visited:
                        visited.add((idx+1, nx, ny))
                        queue.append((idx+1, nx, ny))
    return False

while True:
    line = input().strip()
    if line == '0 0':
        break
    px, py = map(int, line.split())
    n = int(input())
    coords = list(map(int, input().split()))
    sprinklers = []
    for i in range(n):
        sprinklers.append( (coords[2*i], coords[2*i+1]) )
    if can_survive(px, py, sprinklers):
        print("OK")
    else:
        print("NA")