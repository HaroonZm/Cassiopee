from collections import deque

def solve():
    # 入力の読み込み
    W, H, N = map(int, input().split())
    sx, sy = map(int, input().split())

    # 各導火線の経路を格納
    paths = []
    max_L = 0
    for _ in range(N):
        data = list(map(int, input().split()))
        L = data[0]
        path = [(data[i], data[i+1]) for i in range(1, 2*L, 2)]
        paths.append(path)
        if L > max_L:
            max_L = L

    # 各導火線の火の位置は時刻tでpath[t], ただしt >= L-1なら火は爆弾位置で爆発（爆弾位置に火が到達する瞬間爆発）
    # 火は0秒でpath[0]にある

    # 火が爆弾位置に到達する時間：L-1秒、この時点で爆発するので、それ以降の時刻で火が爆弾位置にいるのを防ぐ必要がある
    # 火の位置が時刻t >= L => 火は存在しない（消火済み、または爆発済み）

    # 移動可能な8方向＋停留まりの移動ベクトル（dx, dy）
    directions = [
        (0, 0),  # 留まる
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]

    # 爆弾の座標セット
    bomb_cells = set(path[-1] for path in paths)

    # グリッド内判定
    def in_grid(x, y):
        return 1 <= x <= W and 1 <= y <= H

    # 時間tに各導火線の火の位置を返す関数
    # 時間t >= L_i-1のとき火は爆発位置にいるので、そこに火は存在し爆発
    # 時間t >= L_iのとき火は存在しない（消火済みまたは爆発済み）
    # それ以外は path[t]
    def fires_positions(t):
        positions = []
        for path in paths:
            L = len(path)
            if t < L - 1:
                positions.append(path[t])
            elif t == L - 1:
                # 火が爆弾位置にいる瞬間とも言えるが爆発するのでここに火がいると爆発確定
                # ※火はこの時刻「爆弾位置」にいるが爆発扱い
                # 実装ではこの瞬間の火を検知したら爆発判定として扱う
                positions.append(path[-1])
            else:
                # 火は消えている（消火済みまたは爆発済み）
                positions.append(None)
        return positions

    # 爆弾爆発判定
    # ある時刻tに火が爆弾位置に到達( == path[-1])したら爆発なのでNG
    # ただし、path途中で爆弾位置に火が来たのではなく「path[-1]」に火が来た時だけ爆発する。
    # パス中の他マスは爆発しない

    # 探索状態は
    # (x, y, bitmask of extinguished fires)
    # bitmaskはN個の導火線の火の消火状態を示す。1ビットが消火済みであることを表す。
    # ただし火が消えた瞬間でも状態は変わるので注意

    # BFSの使うキュー
    # 時刻tを状態に含める必要は無いが、火の位置は時間依存なので訪問済み管理は状態＋時間の概念で行う
    # 時刻は探索の深さになる

    from collections import deque

    # 状態の訪問管理
    # visited[x][y][bitmask][t]は重くなるので、爆弾爆発時間の最大はmax_L-1秒なので
    # 時刻はmax時間20*20*max_L程度？
    # 時刻無限ではなく、火の最大長さがtを制限するため、時刻上限はmax_L + H*W程度とする

    # ただし状態数は大きいので、時刻を訪問管理に入れずに工夫する。
    # 火の位置は時刻依存するので同じ(x,y,bitmask)でも時刻違うと火の位置違う。
    # そこで訪問に時刻も含めるか、またはbitmaskに火が存在する場所を含める方法がある。

    # ここでは時刻を含めてvisitedに入れる実装にする（最大時刻はmax_L + W*H）

    max_time = max_L + W * H + 10

    # visited[(x, y, extinguished_bitmask, t)] = True の代わりに2次元マップに
    # visited[x][y][bitmask][t]はメモリ結構使うため、
    # 代わりに visited[(x,y,bitmask, t)] のsetにする

    visited = set()

    # 移動可能ではないマスは爆弾のマスとグリッド外のみ
    # 導火線の火があるマスはロボットが火を消すことができるが移動は出来るのでOK

    # BFS開始状態
    # 初期時刻0秒、ロボット位置は(sx, sy)、消火済みビットマスク0

    from copy import deepcopy

    q = deque()
    start_state = (sx, sy, 0, 0)  # x, y, extinguished bitmask, time
    visited.add(start_state)
    q.append(start_state)

    while q:
        x, y, extinguished, t = q.popleft()
        # 時刻tに各導火線の火の位置を取得
        fire_pos = fires_positions(t)

        # 爆弾爆発判定: 火が爆弾位置にいるなら爆発
        # 火がすでに消えている導火線はfire_pos[i] is None
        exploded = False
        for i, pos in enumerate(fire_pos):
            if pos is not None:
                # 火が存在
                if pos == paths[i][-1]:
                    # 火が爆弾位置にいる爆発タイミング =>爆発で失敗
                    exploded = True
                    break
        if exploded:
            continue  # 爆発したのでこの状態は無効

        # 火がいるマスで消火可能
        # 現在いるマスに火がいる導火線の火を消火する
        # 消火したら対応するビットを立てる

        new_extinguished = extinguished
        for i, pos in enumerate(fire_pos):
            if pos == (x, y):
                new_extinguished |= (1 << i)

        # すべての火が消えていれば終了
        if new_extinguished == (1 << N) - 1:
            print(t)
            return

        # 時刻の制限
        if t + 1 > max_time:
            # 探索打ち切り安全策（だいたいmax_L+W*H）
            continue

        # 次の状態に遷移
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if not in_grid(nx, ny):
                continue
            # 爆弾のマスは移動禁止
            if (nx, ny) in bomb_cells:
                continue
            # 次の時刻t+1の火の位置
            fire_pos_next = fires_positions(t+1)

            # 次のマスnx, nyに火の火があるか？
            # 火のあるマスは移動可能なのでここはチェック不要（火のマスは通れる）
            # ただし爆弾位置は爆弾マスに含まれる

            # 次の時刻で爆発判定は次ループで行うためここは不要

            next_state = (nx, ny, new_extinguished, t+1)
            if next_state not in visited:
                visited.add(next_state)
                q.append(next_state)

    # 探索終了しても解がないなら-1
    print(-1)


if __name__ == "__main__":
    solve()