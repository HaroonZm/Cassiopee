import sys
import threading

def main():
    sys.setrecursionlimit(10**7)
    n = int(sys.stdin.readline())
    W = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    E = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    F = [sys.stdin.readline().rstrip() for _ in range(n)]

    # 現在の状態と目的状態との差分のコストを計算する
    # 目的状態は行、列それぞれに丸印が1つだけ存在する配置（すなわち置く位置を1つずつ選ぶ）
    #
    # 問題は：各行に1つ、各列に1つの丸を配置する場所（完全マッチング）を選び、初期状態の丸を消すコストと
    # 書き足すコストの総和を最小化すること。
    #
    # コスト行列を以下のように定義する。
    # i-th 行、j-th 列のマスに丸を最終的に置く場合、そのコストは
    # もし初期状態で丸ありなら消す必要はないが、もし丸が無ければ書き込みコストがかかる。
    #
    # 一方で、丸が初期状態で置いてあるマスは、
    # それが選ばれずに丸を置かない場合は消すコストがかかり、
    # 選ぶ場合は消さず書かずコスト0
    #
    # したがってマッチングのコストを調整し、最小重みの完全マッチングを求める。

    # ここで「最終状態に丸を置くマス」はi行の列jを決める
    # コスト行列cost[i][j]を以下で考える
    # cost[i][j] = (初期状態の丸がなければW_ij（書き込みコスト）、あれば0)
    # そして、初期状態の丸があるマスで選ばれなかった場合の消去コストは別に加える必要がある。
    #
    # 従って全ての初期状態の丸の消去コストの和を初期値として、それから選ばれたマスの丸がある位置は
    # そこから消去コストを差し引く、選ばれたマスの丸が無ければ書き込みコストを加える形に変形する。

    total_erase_cost = 0
    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o':
                total_erase_cost += E[i][j]

    cost = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o':
                # 既に丸ありなので、選ばれれば消去コストがかからない分を差し引く
                cost[i][j] = total_erase_cost - E[i][j]
            else:
                # 丸なしなので、選べば書き込みコストがかかる
                cost[i][j] = total_erase_cost + W[i][j]

    # ここでcost行列は大きいがこれは全体コストtotal_erase_costをベースに
    # 選択を考慮した値
    # このコストの最小完全マッチングを求めると、マッチングの合計コストは minimized_cost_in_cost_matrix
    #
    # 最小コスト = minimized_cost_in_cost_matrix - total_erase_cost * n 
    # と計算されるため、
    # 実際に動作させる際は負の値も出るがそこは調整しながら。

    # 最小重み完全マッチングをHungarianアルゴリズムで解くコードを以下に実装

    # http://e-maxx.ru/algo/assignment_hungary
    INF = 10**9
    U = [0]*(n+1)
    V = [0]*(n+1)
    p = [0]*(n+1)
    way = [0]*(n+1)

    for i in range(1, n+1):
        p[0] = i
        j0 = 0
        minv = [INF]*(n+1)
        used = [False]*(n+1)
        while True:
            used[j0] = True
            i0 = p[j0]
            j1 = 0
            delta = INF
            for j in range(1, n+1):
                if not used[j]:
                    cur = cost[i0-1][j-1] - U[i0] - V[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
            for j in range(n+1):
                if used[j]:
                    U[p[j]] += delta
                    V[j] -= delta
                else:
                    minv[j] -= delta
            j0 = j1
            if p[j0] == 0:
                break
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    ans = [-1]*n
    for j in range(1, n+1):
        if p[j] != 0:
            ans[p[j]-1] = j-1

    # 最小コスト計算
    # p と V の更新過程から最小コストは -V[0]
    minimized_cost_in_cost_matrix = -V[0]
    mincost = minimized_cost_in_cost_matrix - total_erase_cost * n

    # mincostが負の場合は0にする（理論上は負にならないはずだが安全策）
    if mincost < 0:
        mincost = 0

    # 操作を決定する
    # 操作は、初期状態と最終状態の差分に基づく
    # 最終状態は ans により、行iに丸を置く列が ans[i]

    operations = []
    final_pos = [[False]*n for _ in range(n)]
    for i in range(n):
        final_pos[i][ans[i]] = True

    # 初期状態で丸があってfinal_posがFalseなら消す
    for i in range(n):
        for j in range(n):
            if F[i][j] == 'o' and not final_pos[i][j]:
                operations.append((i+1, j+1, 'erase'))

    # 初期状態で丸がなくfinal_posがTrueなら書く
    for i in range(n):
        for j in range(n):
            if F[i][j] == '.' and final_pos[i][j]:
                operations.append((i+1, j+1, 'write'))

    # 操作コストを確認
    calc_cost = 0
    for r,c,op in operations:
        if op == 'erase':
            calc_cost += E[r-1][c-1]
        else:
            calc_cost += W[r-1][c-1]

    # 出力
    # mincostと一致しない場合はmincostをcalc_costにしておく（理論上一致するはず）
    if calc_cost != mincost:
        mincost = calc_cost

    print(mincost)
    print(len(operations))
    for op in operations:
        print(op[0], op[1], op[2])

threading.Thread(target=main).start()