while True:
    max_num = int(input())
    if max_num == 0:
        break
    n = int(input())
    d = []
    for _ in range(n):
        d.append(int(input()))
    # すごろくのマスの数は n+2 (ふりだし=0, あがり=n+1)
    size = n + 2

    # 移動先を計算する関数
    def move(pos, roll):
        nxt = pos + roll
        if nxt >= n + 1:
            return n + 1
        # 指示があれば指示に従う
        if nxt == 0 or nxt == n + 1:
            return nxt
        diff = d[nxt - 1]
        if diff == 0:
            return nxt
        move2 = nxt + diff
        # 指示によって進んだ先の指示は無視
        if move2 > n + 1:
            move2 = n + 1
        if move2 < 0:
            move2 = 0
        return move2

    from collections import deque

    visited = [False] * size
    reachable = [False] * size
    reachable[0] = True
    queue = deque()
    queue.append(0)

    # 各マスから出るところの遷移先をメモる
    transitions = [[] for _ in range(size)]
    for pos in range(size):
        if pos == n + 1:
            continue
        for roll in range(1, max_num + 1):
            nxt = move(pos, roll)
            transitions[pos].append(nxt)

    # 「あがり」(n+1)にたどり着けるか調べるために
    # 「あがり」にたどり着ける状態を探す
    # 状態を伝播させるため幅優先探索で全てのreachableを探す
    visited = [False] * size
    visited[0] = True
    queue = deque()
    queue.append(0)
    while queue:
        pos = queue.popleft()
        for nxt in transitions[pos]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

    # 到達可能なノードだけでグラフを作って閉路があるか調べる
    # 閉路があれば「あがり」にたどりつけないことになる
    # トポロジカルソートを試みる
    indeg = [0] * size
    for pos in range(size):
        if not visited[pos]:
            continue
        for nxt in transitions[pos]:
            if visited[nxt]:
                indeg[nxt] += 1

    # トポロジカルソート
    q = deque()
    for i in range(size):
        if visited[i] and indeg[i] == 0:
            q.append(i)

    count = 0
    while q:
        pos = q.popleft()
        count += 1
        for nxt in transitions[pos]:
            if visited[nxt]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

    # 到達可能なノード数とトポソートに使ったノード数が一致しなければ閉路あり
    total_reachable = sum(visited)
    if visited[n+1] and count == total_reachable:
        print("OK")
    else:
        print("NG")