import sys
import heapq

# 点を表すクラス
class Node:
    def __init__(self, kind, index):
        # kind: 'H'(家), 'D'(市役所), 'C'(ケーキ屋), 'L'(ランドマーク)
        self.kind = kind
        self.index = index

    def __hash__(self):
        return hash((self.kind, self.index))

    def __eq__(self, other):
        return self.kind == other.kind and self.index == other.index

    def __str__(self):
        return f"{self.kind}{self.index}" if self.kind in ['C', 'L'] else self.kind

    def __repr__(self):
        return self.__str__()

def parse_point(s):
    # H, Dは index 0固定, CとLは番号を整数で
    if s == 'H' or s == 'D':
        return Node(s, 0)
    else:
        return Node(s[0], int(s[1:]))

def main():
    input = sys.stdin.readline
    while True:
        m, n, k, d = map(int, input().split())
        if m == 0 and n == 0 and k == 0 and d == 0:
            break

        cake_calories = list(map(int, input().split()))
        # ノード総数:
        # H:1, D:1, C:m, L:n
        # ID割り当て: 家=0, 市役所=1, ケーキ屋=2~2+m-1, ランドマーク=2+m~2+m+n-1
        # 探索用にIDを付ける
        node_id_map = {}  # Node -> ID
        id_node_map = []  # ID -> Node

        def get_id(node):
            if node not in node_id_map:
                node_id_map[node] = len(id_node_map)
                id_node_map.append(node)
            return node_id_map[node]

        # まずHとDを登録
        H = Node('H', 0)
        D = Node('D', 0)
        get_id(H)
        get_id(D)
        # ケーキ屋
        cake_nodes = []
        for i in range(1, m+1):
            cnode = Node('C', i)
            cake_nodes.append(cnode)
            get_id(cnode)
        # ランドマーク
        landmark_nodes = []
        for i in range(1, n+1):
            lnode = Node('L', i)
            landmark_nodes.append(lnode)
            get_id(lnode)

        # グラフ：隣接リスト
        # graph[node_id] = list of (neighbor_id, distance)
        graph = [[] for _ in range(len(id_node_map))]

        for _ in range(d):
            s_i, t_i, e_i = input().split()
            e_i = int(e_i)
            u = parse_point(s_i)
            v = parse_point(t_i)
            uid = get_id(u)
            vid = get_id(v)
            graph[uid].append((vid, e_i))
            graph[vid].append((uid, e_i))

        # ビットマスクDP＋ダイクストラで解く

        # 状態: (現在地ノードID, 訪問したケーキ屋のビットマスク)
        # 目的: 市役所(D)に到達し，最小正味消費カロリー（距離*k - ケーキのカロリー合計）の最小値

        INF = 10**9
        from collections import deque

        # ケーキ屋のIDからビット位置対応を作成
        cake_id_to_bitpos = {}
        for i, cnode in enumerate(cake_nodes):
            cid = get_id(cnode)
            cake_id_to_bitpos[cid] = i

        # 距離をminカロリーに換算するためラベル付け
        # 消費カロリー = 距離*k - ケーキカロリー合計
        # 距離*kは移動した距離にkをかけたもの

        # dist[node_id][bitmask] = 最小正味消費カロリー
        dist = [[INF]*(1<<m) for _ in range(len(id_node_map))]

        # スタートは家、ケーキ屋はまだ訪問していない状態
        start = get_id(H)
        goal = get_id(D)

        dist[start][0] = 0
        # 優先度付きキューでダイクストラ。キーは「正味の消費カロリー」
        # 要素：(正味消費カロリー, 現在地node_id, ビットマスク)
        pq = []
        heapq.heappush(pq, (0, start, 0))

        while pq:
            cur_cost, u, mask = heapq.heappop(pq)
            if dist[u][mask] < cur_cost:
                continue
            # ゴールかつ最小更新できたらそれが答えの候補になるのでcontinueしても良い
            if u == goal:
                # 最小値が得られたことを利用
                # ただし最小値が複数ありうるので最後まで探索したいが、
                # ダイクストラ条件によりdistは初めて到達時最小=>最初に取ったcostが最小
                # よってここで出力してbreakでも良いが複数セットあるのでbreakしないで最後まで続けてもOK
                pass

            for (v, dist_uv) in graph[u]:
                # 次の状態のコスト計算
                calorie_cost = cur_cost + dist_uv * k
                new_mask = mask
                node_v = id_node_map[v]
                # ケーキ屋の新規訪問判定
                if node_v.kind == 'C':
                    bitpos = cake_id_to_bitpos[v]
                    if (mask & (1 << bitpos)) == 0:
                        # 未訪問ならケーキカロリーを減算
                        calorie_cost -= cake_calories[bitpos]
                        new_mask = mask | (1 << bitpos)
                # dist更新判定
                if dist[v][new_mask] > calorie_cost:
                    dist[v][new_mask] = calorie_cost
                    heapq.heappush(pq, (calorie_cost, v, new_mask))

        # 答えは市役所（goal）に到達したすべての状態の中で最小値
        ans = min(dist[goal])
        print(ans)

if __name__ == "__main__":
    main()