import sys
import collections

def main():
    input = sys.stdin.readline
    M, N, K = map(int, input().split())

    # スイッチのある部屋をセットで管理する（(x,y)でアクセス O(1)）
    switch_rooms = set()
    for _ in range(K):
        x, y = map(int, input().split())
        switch_rooms.add((x, y))

    # 扉の開閉状態は2種類
    # 状態 0: 東西の扉は閉じている、南北の扉は開いている
    # 状態 1: 東西の扉は開いている、南北の扉は閉じている
    #
    # 移動条件
    # - 状態0のときは南北に（y方向、上下）だけ移動可能（±1）
    # - 状態1のときは東西に（x方向、左右）だけ移動可能（±1）
    #
    # また、スイッチがある部屋でスイッチを1分間押すと状態が反転する
    #
    # 始点：(1, 1), 終点：(M, N)
    #
    # 状態遷移を含めた最短時間を求める問題なので
    # 「位置 + 扉の状態(0 or 1)」をノードとしたグラフ上でbfsを行う

    # BFSのキューは(時間, x, y, state)
    # ここで、stateは0か1の2値
    # dist[(x,y,state)] = 最短時間

    from collections import deque

    # BFS用の距離辞書はメモリ大きすぎて使えないのと、
    # M,N最大10^5なので二次元リスト＋状態2も大きすぎる
    # そこで、訪問済み管理はdictまたはセットで行う

    visited = set()
    queue = deque()

    # 始点は(1,1,0)、時間0
    start = (1, 1, 0)
    visited.add(start)
    queue.append((0, 1, 1, 0))

    while queue:
        time, x, y, state = queue.popleft()
        # 目的地に着いたら時間を出力して終了
        if (x, y) == (M, N):
            print(time)
            return

        # 現在の状態で移動可能な方向決定
        # state=0: 南北移動可能 (y±1)
        # state=1: 東西移動可能 (x±1)
        if state == 0:
            # 南北移動可能
            for dy in [-1, 1]:
                ny = y + dy
                if 1 <= ny <= N:
                    nxt = (x, ny, state)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((time + 1, x, ny, state))
        else:
            # 東西移動可能
            for dx in [-1, 1]:
                nx = x + dx
                if 1 <= nx <= M:
                    nxt = (nx, y, state)
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((time + 1, nx, y, state))

        # スイッチを押して状態切り替え（位置は変わらず、時間+1）
        # 位置にスイッチがある場合のみ可能
        if (x, y) in switch_rooms:
            nxt_state = 1 - state
            nxt = (x, y, nxt_state)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((time + 1, x, y, nxt_state))

    # 到達不可
    print(-1)

if __name__ == "__main__":
    main()