import sys
import math
input=sys.stdin.readline

def can_collect_all(n, hx, hy, dx, dy, crystals):
    # 魔王の位置と勇者の初期位置が同じ場合は既に始まっているので判定しやすい
    # クリスタルをi番目に取るまでにかかる最短時間を計算し、その時点で瘴気が広がった範囲を考慮
    # ユークリッド距離1/日で移動可、瘴気は魔王の位置から1/日ずつ広がり、境界線上の地点は立ち入り不可（クリスタルも取れない）
    
    # 状態：bitmask(選んだクリスタル)+現在位置として、全探索（n <= 20だが全探査は2^n* nで間に合わない）
    # → ここではDPは使わず、貪欲に順番を固定してすべての順列を試すのは無理
    # しかし n <= 20では完全順列調査は不可能
    # → そこで順序を変えずに全探索しながら、最短経路を探すのは困難
    # 対応策として TSP を諦め、問題文からは「勇者は全てのクリスタルを1つずつ手に入れていく」という記述のみで、任意の順序に取って良いと推察
    # → 順列探索は最大20!で不可能
    # → そこで枝刈り付きDFS + 距離と時間での早期打ち切りが有用
    # しかし今回の提出は最適化も考慮しつつも高速化が必要なので、
    # 1) クリスタル20個で全順列は不可能
    # 2) DP TSP (O(n^2 * 2^n)) は約20万で許容範囲だが、計算量厳しい
    # 3) そのためDP TSPで解く
    
    # 距離計算関数
    def dist(a, b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    # 初期位置
    pos = (hx, hy)
    # 瘴気の中心は魔王の位置
    center = (dx, dy)

    # dp[bit][j] := bitで指定されたクリスタル群を集め、最後にj番目のクリスタルを取った場合の最短時間
    dp = [[math.inf]*(n) for _ in range(1<<n)]

    # 初期化：勇者の位置から各クリスタルへ行けるか調べる
    for i,(cx, cy) in enumerate(crystals):
        dist0 = dist(pos, (cx, cy))
        # 勇者が移動にdist0日かかるとして、そこについた時刻t=dist0
        # 瘴気はt日経過で距離tだけ中心から広がっている
        # 勇者は境界線上には入れないので、中心からの距離 >
        # (t=dist0)すなわち moving_point_distance_from_center > dist0 が必要
        d_center = dist(center, (cx, cy))
        if d_center > dist0:
            dp[1<<i][i] = dist0

    for bit in range(1<<n):
        for j in range(n):
            if dp[bit][j] == math.inf:
                continue
            # 現在j番目のクリスタルにいる（時間は dp[bit][j]）
            t_now = dp[bit][j]
            pos_j = crystals[j]
            for k in range(n):
                if bit & (1<<k):
                    continue
                # j→k の距離
                d_jk = dist(pos_j, crystals[k])
                t_arrive = t_now + d_jk
                d_center_k = dist(center, crystals[k])
                # 瘴気の境界線上及びその内部は無理 → d_center_k > t_arrive 必須
                if d_center_k > t_arrive:
                    nxt = bit | (1<<k)
                    if dp[nxt][k] > t_arrive:
                        dp[nxt][k] = t_arrive

    full = (1<<n) - 1
    res = min(dp[full])
    return res != math.inf


while True:
    n,hx,hy,dx,dy=map(int,input().split())
    if n==0 and hx==0 and hy==0 and dx==0 and dy==0:
        break
    crystals=[tuple(map(int,input().split())) for _ in range(n)]
    print("YES" if can_collect_all(n,hx,hy,dx,dy,crystals) else "NO")