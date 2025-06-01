import sys
import heapq

def solve():
    input = sys.stdin.readline
    N, M, X = map(int, input().split())
    # 部屋の温度情報
    T = [int(input()) for _ in range(N)]

    # グラフの構築（無向グラフ）
    # graph[u] = [(v, cost), ...]
    graph = [[] for _ in range(N)]

    for _ in range(M):
        A, B, D = map(int, input().split())
        A -= 1  # 0-indexedに調整
        B -= 1
        graph[A].append((B, D))
        graph[B].append((A, D))

    # 温度状態の定義
    # 0: 寒すぎ (Cold)
    # 1: 快適 (Comfortable)
    # 2: 暑すぎ (Hot)
    # JOI君は寒すぎの部屋1 (index0) に現在いる

    # 状態を管理するために、次に使う温度遷移を管理
    # JOI君が最後に寒すぎの部屋を出てからX分未満のうちに暑すぎの部屋に入れない
    # および最後に暑すぎの部屋を出てからX分未満のうちに寒すぎの部屋に入れない

    # 快適な部屋（1）は制約なしに入れる

    # 上記を満たすために状態を
    # last_temp: 最後にいた寒・暑部屋の種類（0, 2 もしくは -1でなし（快適））
    # elapsed: 最後に寒すぎor暑すぎな部屋を出てからの経過時間（0〜X）

    # よって状態は (部屋, last_temp, elapsed) の３次元となる

    # 初期状態は部屋0（寒すぎ）、last_temp=0 (寒すぎ), elapsed=0
    # elapsedは経過時間でXまでの範囲、X以上はXで扱う（それ以上は制約無しと同じ）

    INF = 10**15
    dist = [[[INF] * (X + 1) for _ in range(3)] for _ in range(N)]
    # last_temp = 0 or 1 or 2 のうち、
    # 1は快適なのでここでは last_temp を 0,2,3 (3は快適なし状態) に該当させる、
    # 便宜上 last_temp: 0(寒すぎ), 1(快適), 2(暑すぎ)
    # しかし elapsed が意味を持つのはlast_tempが寒(0)か暑(2)のときのみ
    # 快適(1)の時は elapsed = Xとしておけば制約なし扱いにできる
    # 状態を0,1,2で管理し、快適はelapsed=Xとして扱う

    # last_temp に対応する添字を以下とする：
    # 0: 寒すぎ
    # 1: 快適
    # 2: 暑すぎ

    # 初期状態は部屋0、last_temp=0(寒すぎ)、elapsed=0
    dist[0][0][0] = 0
    hq = []
    heapq.heappush(hq, (0, 0, 0, 0)) # (時間, 部屋, last_temp, elapsed)

    while hq:
        time, u, last_temp, elapsed = heapq.heappop(hq)
        if dist[u][last_temp][elapsed] < time:
            continue
        if u == N - 1:
            # ゴールに到達
            print(time)
            return

        current_temp = T[u]

        # 次に行く部屋の温度(next_temp)によって制約と状態更新が異なる
        for v, cost in graph[u]:
            next_temp = T[v]

            # 移動中、部屋に入ったらすぐ出るため、
            # 次の状態の last_temp, elapsed を更新する必要がある

            # elapsedは最後の寒すぎor暑すぎな部屋を出てからの経過時間
            # 最後の温度状態を更新するには次の部屋に入る瞬間の規則を見る

            # 制約判定と状態遷移ルール
            # 快適な部屋の場合（1）
            #   last_temp は変えない、elapsed は経過時間を加算（最大Xでクリップ）
            # 寒すぎまたは暑すぎ部屋の場合（0 or 2）
            #   急な遷移がないかチェック
            #   もし last_temp と next_temp が
            #    0→2 or 2→0 の場合 elapsed >= Xでなければ遷移不可
            #   遷移可能なら、last_temp=next_temp, elapsed=0リセット

            # elapsedにcostを加算（移動時間）

            # ただし elapsed は部屋を出てから次の部屋に入るまでの時間なので、
            # 部屋 u を出て廊下を渡り部屋 v に入るまで cost 分かかる

            if current_temp in (0, 2):
                # last_tempはcurrent_temp
                cur_last = current_temp
                cur_elapsed = elapsed
            else:
                # 快適な部屋は last_temp状態に影響しないのでそのまま
                # elapsed は cur_elapsed+costで加算するのでここで設定
                # ただし last_tempは変わらない
                cur_last = last_temp
                cur_elapsed = elapsed

            next_elapsed = min(cur_elapsed + cost, X)  # 経過時間はXで頭打ち

            # 制約判定
            # last_tempはcur_last、next_tempで判定
            # 下記の急変禁止条件に注意
            if cur_last != 1 and next_temp != 1:
                # last_tempが寒(0)か暑(2)、次も寒(0)か暑(2)
                # 急な温度変化は0→2または2→0のケース
                if cur_last != next_temp:
                    # 急変なので elapsed >= X でなければ移動不可
                    if next_elapsed < X:
                        continue
                    # 移動可能なら elapsed=0にリセットし状態更新
                    # ただし elapsedは部屋を出てからの時間なので
                    # 新しい last_tempは next_temp
                    new_last = next_temp
                    new_elapsed = 0
                else:
                    # 同じ0->0または2->2なら状態は変わらずelapsed加算のみ
                    new_last = cur_last
                    new_elapsed = next_elapsed
            else:
                # 快適部屋を含む遷移は制約なし
                # last_tempはnext_tempが0 or 2なら更新、1なら維持（快適部屋は状態変化なし）
                if next_temp == 0 or next_temp == 2:
                    new_last = next_temp
                    new_elapsed = 0
                else:
                    # 快適部屋
                    new_last = cur_last
                    new_elapsed = next_elapsed

            # 次の状態の距離更新
            # dist[v][new_last][new_elapsed]を更新する
            new_time = time + cost
            if dist[v][new_last][new_elapsed] > new_time:
                dist[v][new_last][new_elapsed] = new_time
                heapq.heappush(hq, (new_time, v, new_last, new_elapsed))


if __name__ == "__main__":
    solve()