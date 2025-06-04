from collections import deque

def neighbors(x, y, m, n):
    # 横に m、縦に n
    res = []
    # 奇数行と偶数行で六角形のつながりが変わる
    # 偶数行 (yが偶数)
    if y % 2 == 0:
        deltas = [(-1,0), (1,0), (0,-1), (1,-1), (0,1), (1,1)]
    else:
        # 奇数行 (yが奇数)
        deltas = [(-1,0), (1,0), (-1,-1), (0,-1), (-1,1), (0,1)]
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 1 <= nx <= m and 1 <= ny <= n:
            res.append((nx, ny))
    return res

def bfs(sources, m, n):
    # 複数の開始点からの距離を同時に計算する
    dist = [[-1]*(n+1) for _ in range(m+1)]
    queue = deque()
    for i, (x, y) in enumerate(sources, 1):
        dist[x][y] = 0
        queue.append((x, y, i))
    owner = [[0]*(n+1) for _ in range(m+1)]
    owner_ties = [[False]*(n+1) for _ in range(m+1)]
    # owner: 一番近いコンビニ番号、owner_ties: 同距離のものが複数あるか

    while queue:
        x, y, cno = queue.popleft()
        for nx, ny in neighbors(x, y, m, n):
            nd = dist[x][y] + 1
            if dist[nx][ny] == -1:
                dist[nx][ny] = nd
                owner[nx][ny] = cno
                queue.append((nx, ny, cno))
            else:
                if dist[nx][ny] == nd and owner[nx][ny] != cno:
                    owner_ties[nx][ny] = True
    return owner, owner_ties

def solve():
    while True:
        mn = input().split()
        if len(mn) != 2:
            continue
        m, n = map(int, mn)
        if m == 0 and n == 0:
            break
        s = int(input())
        established = [tuple(map(int, input().split())) for _ in range(s)]
        t = int(input())
        candidates = [tuple(map(int, input().split())) for _ in range(t)]

        # 既設のコンビニと候補地を含めて一度まとめて距離計算しておく
        # 既設は番号1..s
        # 候補は番号 s+1 .. s+t

        # まず既設コンビニだけで領域分け
        owner, ties = bfs(established, m, n)

        # 各候補地でのカバー数を求めるため、新たに候補地を追加して計算すると計算量が増えるので、問題文の考え方に沿って計算方法を考える
        # ここでは候補地を1つ加えた場合で、既設のコンビニと合わせて領域判定を行い、それによりカバーされるブロック数を出す

        max_cover = 0
        for pidx, (px, py) in enumerate(candidates, 1):
            # 新しい店舗は番号 s+1
            stores = established + [(px, py)]
            owner2, ties2 = bfs(stores, m, n)
            cover_counts = [0]*(s+1)  # 既設が s 個, 新店は s 番目としてカウントしないのでs+1要素、cover_counts[s]は新店舗カウント用
            for x in range(1, m+1):
                for y in range(1, n+1):
                    if ties2[x][y]:
                        continue
                    c = owner2[x][y]
                    if c == s+1:
                        cover_counts[s] += 1
            if cover_counts[s] > max_cover:
                max_cover = cover_counts[s]
        print(max_cover)

if __name__ == "__main__":
    solve()