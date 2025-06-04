import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    N = int(input())
    p = [0] + [int(input()) for _ in range(N)]

    # next_pos[i]は、i番のマスから効果を適用した後に必ず着地するマス番号
    # p[i]の効果により複数ステップ移動がある場合も、ループせず最終的に止まるマスを計算する
    next_pos = [0] * (N + 1)

    # ループが発生しないようにi番のマスの効果適用先を計算する
    # dfsで効果の連鎖を辿りながら決定する
    visited = [0] * (N + 1)  # 0=未訪問,1=訪問中,2=訪問済み
    def dfs(i):
        if visited[i] == 1:
            # 効果に無限ループがあれば、サイコロを振る数の最小値は無限
            # 問題で「無限ループになる場合もあるが、入力はゴール可能と仮定されている」ためここには来ないはず
            # もし来たら例外として離脱
            raise ValueError("Infinite loop detected in effect chain")
        if visited[i] == 2:
            return next_pos[i]
        visited[i] = 1
        dest = i + p[i]
        # p[i]=0ならdest=i
        # p[i]により指示された移動先が範囲外はありえない（問題の条件）
        # destが効果の適用の起点になりうるので再帰
        next_pos[i] = dfs(dest) if p[i] != 0 else i
        visited[i] = 2
        return next_pos[i]

    for i in range(1, N + 1):
        if visited[i] == 0:
            dfs(i)

    # BFSで最短ステップを求める
    # state: 現在のマス番号（効果適用後の最終着地マス）
    # スタートは1マス目の効果適用後のマス
    start = next_pos[1]

    dist = [-1] * (N + 1)
    dist[start] = 0
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        # サイコロの目は1から6まで自由に選べる（確率湾曲で操作可能）
        for dice in range(1, 7):
            nxt = cur + dice
            if nxt >= N:
                # ゴールに着いたとみなす
                # 現在までのサイコロ数+1が最小回数の候補
                print(dist[cur] + 1)
                return
            # 効果適用後の最終着地マスへ
            after_effect = next_pos[nxt]
            if dist[after_effect] == -1:
                dist[after_effect] = dist[cur] + 1
                queue.append(after_effect)

if __name__ == "__main__":
    solve()