import sys
import heapq

def solve():
    input = sys.stdin.readline
    while True:
        m, n, k, d = map(int, input().split())
        if m == 0 and n == 0 and k == 0 and d == 0:
            break
        cake_cals = list(map(int, input().split()))
        # ノードのラベルを番号にマッピング
        # H:0, D:1, C1..Cm:2..m+1, L1..Ln:m+2..m+n+1
        idx_map = {}
        idx_map['H'] = 0
        idx_map['D'] = 1
        for i in range(m):
            idx_map[f'C{i+1}'] = 2 + i
        for i in range(n):
            idx_map[f'L{i+1}'] = 2 + m + i
        node_count = 2 + m + n
        graph = [[] for _ in range(node_count)]

        for _ in range(d):
            s, t, e = input().split()
            e = int(e)
            u = idx_map[s]
            v = idx_map[t]
            graph[u].append((v, e))
            graph[v].append((u, e))

        # DPでケーキ屋に立ち寄るかどうか状態管理
        # 状態: (訪問済みケーキ屋ビットマスク, 現在地点) -> 最小正味消費カロリー
        INF = 10**15
        dp = [[INF]*node_count for _ in range(1<<m)]
        # スタートは家、ケーキ屋訪問なし
        dp[0][0] = 0
        # ダイクストラ風に進める
        # 優先度キューに (正味消費カロリー, 訪問済みビット, 現在地点)
        hq = [(0,0,0)]
        while hq:
            cost, mask, pos = heapq.heappop(hq)
            if dp[mask][pos] < cost:
                continue
            # 目的地の市役所にいるなら結果を途中で得ることもできるが，最小値を保証するため全部通す
            for nxt, dist in graph[pos]:
                ncost = cost + dist * k
                nmask = mask
                # ケーキ屋かつ未訪問ならケーキのカロリーを引く
                # ケーキ屋はC1..Cm(2..m+1), idxからケーキ屋の番号番号は pos - 2
                if 2 <= nxt < 2 + m:
                    cake_idx = nxt - 2
                    if (mask & (1 << cake_idx)) == 0:
                        ncost -= cake_cals[cake_idx]
                        nmask = mask | (1 << cake_idx)
                if dp[nmask][nxt] > ncost:
                    dp[nmask][nxt] = ncost
                    heapq.heappush(hq,(ncost,nmask,nxt))
        # 市役所(1)に到達している状態の中で最小
        ans = INF
        for mask in range(1<<m):
            if dp[mask][1] < ans:
                ans = dp[mask][1]
        print(ans)
if __name__ == "__main__":
    solve()