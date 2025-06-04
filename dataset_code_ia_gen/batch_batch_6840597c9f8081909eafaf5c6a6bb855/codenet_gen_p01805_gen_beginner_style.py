import sys
sys.setrecursionlimit(10**7)

def can_escape(H, W, R, C, horz, vert):
    from collections import deque

    # 盤面の状態は2パターン（壁の有無反転前と反転後）の2状態で管理
    # 状態は (行, 列, 反転状態) で表現する
    # 反転状態 0: 初期状態, 1: 反転状態

    # 壁のチェック関数
    def has_wall(r, c, nr, nc, flipped):
        # 移動方向決定
        dr = nr - r
        dc = nc - c
        # flipped=0なら壁の値そのまま、flipped=1なら壁の値を反転する
        if dr == -1 and dc == 0:
            # 上へ移動 => horz[r][c] をみる (r行c列のマスの上の壁)
            w = horz[r][c]
        elif dr == 1 and dc == 0:
            # 下へ移動 => horz[r+1][c] 上の壁を使うのは horz[r+1][c] (r+1行目のc列目のマスの上側の壁はr行目の下側の壁)
            w = horz[r+1][c]
        elif dr == 0 and dc == -1:
            # 左へ移動 => vert[r][c]
            w = vert[r][c]
        elif dr == 0 and dc == 1:
            # 右へ移動 => vert[r][c+1]
            w = vert[r][c+1]
        else:
            # その他は動かない
            return True
        if flipped == 1:
            w = 1 - w
        return w == 1

    # 脱出可能か判定 BFSで状態を探索
    # Aliceの手番はコマを移動させる（必須）
    # Bobの手番は壁の反転かスルーの2択

    # 始めの状態: Aliceの手番、コマ位置(R,C)、反転状態0
    # 状態: (r, c, flipped, turn) turn:0=Alice,1=Bob
    # ただしAliceの手番で移動できなければNo

    from collections import deque
    visited = [[ [False]*2 for _ in range(W+2) ] for __ in range(H+2)] # visited[r][c][flipped]
    # 盤面の外周と外側は壁状態で固定しておく: 実際には外側は位置として存在しないので空白行列で問題ない

    # 盤面は1-index始まり、0やH+1の行・列は盤の外
    # 独自に壁のチェックで外側への脱出判定も行う

    # BFSキュー: (r, c, flipped, turn)
    from collections import deque
    q = deque()
    q.append( (R, C, 0, 0) ) # Aliceの手番から
    # visitedにただしAliceの手番の状態だけ記録してよい
    # Bobのターンは壁の状態が変わるだけでコマ位置は動かないので
    # 頂点状態の重複はr,c,flippedだけ管理

    # 状態管理を turn も使わずに BFS
    # 実際はAliceの手番のコマ位置と壁状態だけ管理、それでBobの手番の操作を考える
    # 理解を単純にして、状態は(r,c,flipped),上下左右の移動を考えBobの操作は反転orしない2択

    # BFS用の状態は(r,c,flipped)

    from collections import deque
    visited = [[False]*(W+2) for _ in range((H+2)*2)] # 2×(H+2)行分をflattenしないと面倒
    # 代わりに普通に3D visited
    visited = [ [ [False]*2 for _ in range(W+2)] for __ in range(H+2) ]

    q = deque()
    q.append( (R, C, 0) )
    visited[R][C][0] = True

    # 移動方向
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        r,c,flipped = q.popleft()

        # Aliceの手番状態(r,c,flipped)
        # 脱出判定
        # コマの現在位置(r,c)が盤面の外側に接している辺で壁がなく外に出れるかを判定
        # つまり隣接するマスが盤外で，間の壁がない方向があるか

        for dr,dc in directions:
            nr = r + dr
            nc = c + dc
            # 盤外に出るか
            if nr < 1 or nr > H or nc < 1 or nc > W:
                # 移動できるか壁をチェック，壁がなければ脱出可能
                if not has_wall(r,c,nr,nc,flipped):
                    return True

        # Aliceの移動可能なマスを列挙
        next_moves = []
        for dr,dc in directions:
            nr = r + dr
            nc = c + dc
            if 1 <= nr <= H and 1 <= nc <= W:
                if not has_wall(r,c,nr,nc,flipped):
                    next_moves.append( (nr,nc) )
        if len(next_moves) == 0:
            # Aliceが身動きできないなら脱出できない
            continue

        # Bobの手番: 壁の反転 or 反転しない の2択
        # BobはAliceがどちらでも脱出できなくする最悪のケースを目指すので
        # Aliceはどちらの壁状態でも自由に移動できる必要がある

        # BFSにおいては、Aliceの次手番はボブの壁反転後の状態からスタート

        # Bobは壁状態を反転する( flipped ^ 1 )か、そのまま(flipped)の2状態が生成される

        # Aliceの次手番の状態は,r', c' in next_moves, flipped' in {flipped, flipped^1}の組み合わせ

        # ただしBobは自分にとって有利(脱出を妨害する)ように動くため
        # Aliceが一方の壁状態でしか移動できない場合はBobがその状態に導けば脱出は妨げられる
        # だから安全策としては2つの壁状態全てでAliceの位置遷移を探索

        # よってBFSで両方の壁状態でAliceが辿れる状態を管理する

        for flipped_next in (flipped, flipped ^ 1):
            for (nr,nc) in next_moves:
                if not visited[nr][nc][flipped_next]:
                    visited[nr][nc][flipped_next] = True
                    q.append( (nr,nc,flipped_next) 

                    )

    return False

while True:
    line = sys.stdin.readline()
    if not line:
        break
    H, W, R, C = map(int,line.split())
    if H == 0 and W == 0 and R == 0 and C == 0:
        break

    horz = []
    vert = []

    # horzはH+1行、各行W個、0-originではなく1-originも使う
    # 入力はH+1行 horz

    # input lineの前の半角空白消す
    for _ in range(H+1):
        horz.append(list(map(int, sys.stdin.readline().split())))

    for _ in range(H):
        vert.append(list(map(int, sys.stdin.readline().split())))

    # 入力はこれで終わり
    # データセットの問題の通りに処理

    # 盤面の壁の情報は horz[row][col], vert[row][col]
    # horzは(0..H,0..W-1)
    # vertは(0..H-1,0..W)

    if can_escape(H,W,R,C,horz,vert):
        print("Yes")
    else:
        print("No")