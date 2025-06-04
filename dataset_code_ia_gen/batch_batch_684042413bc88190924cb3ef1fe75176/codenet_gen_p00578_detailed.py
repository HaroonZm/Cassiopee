import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    # 各区画の高さをキーに、その区画番号を値としてまとめる辞書を作成
    height_to_indices = {}
    for i, h in enumerate(A, start=1):
        if h not in height_to_indices:
            height_to_indices[h] = []
        height_to_indices[h].append(i)
    
    # 高さを昇順にソートすることで、海面の高さが徐々に上昇した時の状況を順番に処理できる
    unique_heights = sorted(height_to_indices.keys())
    
    # Union-Find（Disjoint Set Union）で島を管理する
    parent = [-1] * (N+2)  # 1-basedインデックスに合わせ、端の0とN+1はガードとして使用
    
    def find(x):
        while parent[x] >= 0:
            x = parent[x]
        return x
    
    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        if parent[x] > parent[y]:
            x, y = y, x
        parent[x] += parent[y]
        parent[y] = x
        return True
    
    # 陸地状態を管理する配列（加速度的に島を増やしていくため）
    is_land = [False] * (N+2)  # 端にダミーを設置
    
    island_count = 0  # 現在の島の数
    max_islands = 0   # 島の最大数
    
    # 初期状態（海面高さ0未満の区画は陸地）
    # 高さ0以上の区画はまだ沈んでいる状態と考える（海）
    # しかし問題文では海面は現在0なので、A_i > 0の区画が現在陸地
    # ただしA_i == 0の区画は海面高さ0以上で沈むので海と考える
    
    # 初期状態では高さ > 0 の区画のみ陸地
    for i, h in enumerate(A, start=1):
        if h > 0:
            is_land[i] = True
    
    # 初期の島の数を計算
    # 陸地が連続する区間を島とする
    prev = False
    for i in range(1, N+1):
        if is_land[i]:
            if not prev:
                island_count += 1
            prev = True
        else:
            prev = False
    
    max_islands = island_count
    
    # 高さ0からスタートして海面を徐々に上昇させると考える
    # 海面の高さがh以上になると、高さhの区画は沈む（陸地ではなくなる）
    # よって高さの小さい区画から順に沈み、陸地を陸地でなくしていく
    # 島の数の変化を反映するために、実際には初めに高さ>0の区画のみが陸地なので、
    # 海面が0から上昇し高さhの区画が沈むイベントを高さの昇順に処理する。
    # しかし上の初期設定では高さ>0を陸地としているので、
    # 高さhの区画が沈む＝陸地じゃなくなる＝島数が変化する。

    # 整合性を取るために逆のアプローチを採る:
    # 海面が0のとき高さ>0の区画が陸地
    # 海面がhになったとき高さ<hの区画は沈む
    # よって高さの昇順にイベントを処理し、陸地の区画を追加していく方法にするため
    # repurpose:
    # 海面の高さ0未満 = no陸地(ない) -> 何もない状態からスタートする
    # 海面の高さを下げていく(逆方向の見方)と島の数増加を捉えやすい
    # したがって、問題で求めるのは、
    # 海面の高さ0～最大A_iの範囲で島の数の最大値
    # ということは高さの昇順に区画を陸地に追加しながら島の数を追跡する方法がある。

    # よって海面の高さがh未満の区画が陸地である状況を考える。
    # 初期はh=0で高さ<0の区画が陸地 (存在しない)
    # 最小高さから順に区画を陸地に変える
    # 各段階で島の数を計算し最大値を取る。

    parent = [-1] * (N+2)
    is_land = [False] * (N+2)
    island_count = 0
    max_islands = 0

    for h in unique_heights:
        # 高さhの区画を陸地にする
        for idx in height_to_indices[h]:
            is_land[idx] = True
            island_count += 1  # 新しい島候補
            # 前後の連結を確認し島の統合をする
            if is_land[idx - 1]:
                if union(idx, idx - 1):
                    island_count -= 1
            if is_land[idx + 1]:
                if union(idx, idx + 1):
                    island_count -= 1
        if island_count > max_islands:
            max_islands = island_count
    
    print(max_islands)

if __name__ == "__main__":
    main()