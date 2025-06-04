import sys
import heapq

def main():
    input = sys.stdin.readline
    N, T = map(int, input().split())
    A, B = input().split()

    # 駅名 -> 駅ID
    station_id = {}
    def get_id(name):
        if name not in station_id:
            station_id[name] = len(station_id)
        return station_id[name]

    lines = []
    station_positions = {}  # (station, line) -> list of positions on that line

    for _ in range(N):
        a = int(input())
        s = input().split()
        t_list = list(map(int, input().split())) if a > 1 else []
        lines.append((a, s, t_list))
        for i, name in enumerate(s):
            sid = get_id(name)
            if (sid, _) not in station_positions:
                station_positions[(sid, _)] = []
            station_positions[(sid, _)].append(i)

    # 駅ID
    start = station_id.get(A, -1)
    goal = station_id.get(B, -1)
    if start == -1 or goal == -1:
        print(-1)
        return

    # 各路線の途中の隣接駅間の移動は上下に可能なので、両方向に辺を張る
    # 複数路線が同じ駅名は同じ駅ID、乗り換えはT分かかる
    # さらに同じ路線内で同じ駅が複数箇所ある時、それらは乗り換えとして扱わなければならないので、
    # 路線内の同じ駅の異なる位置は別のノードとする
    # したがって、状態は (駅ID, 路線インデックス, 位置) として管理する
    # ノード数の上限は合計のa_iで最大10万

    # ノード番号振り直し
    # node_id[(line_index, position)] = node number
    node_id = {}
    idx = 0
    for i, (a, s, _) in enumerate(lines):
        for pos in range(a):
            node_id[(i, pos)] = idx
            idx += 1
    node_num = idx

    # 各駅IDごとに、その駅に位置するノード群を管理しておく（乗換えに使う）
    station_to_nodes = [[] for _ in range(len(station_id))]
    for (sid, line), positions in station_positions.items():
        for pos in positions:
            station_to_nodes[sid].append(node_id[(line, pos)])

    # グラフ構築
    # グラフは隣接リスト、辺は (次のノード, 時間, 乗換え増加数)
    graph = [[] for _ in range(node_num)]

    # 路線内の上下隣駅へ行く辺を張る（乗換え増えない）
    for i, (a, s, t_list) in enumerate(lines):
        for pos in range(a):
            nid = node_id[(i, pos)]
            # 上方向
            if pos > 0:
                prev_nid = node_id[(i, pos-1)]
                cost = t_list[pos-1]
                graph[nid].append((prev_nid, cost, 0))
                graph[prev_nid].append((nid, cost, 0))

    # 乗換え（同じ駅の異なるノード間）辺を張る、コストT、乗換え +1
    for sid in range(len(station_id)):
        nodes = station_to_nodes[sid]
        # ノードが1つ以上あればすべての組に辺を張る（無向グラフなので片方向で十分）
        # 計算量を考慮し、隣接リストにdoubleの辺を一つずつはって良い
        for i1 in range(len(nodes)):
            for i2 in range(i1+1, len(nodes)):
                n1 = nodes[i1]
                n2 = nodes[i2]
                graph[n1].append((n2, T, 1))
                graph[n2].append((n1, T, 1))

    # スタートノード群、goalノード群
    start_nodes = station_to_nodes[start]
    goal_nodes = set(station_to_nodes[goal])
    if not start_nodes or not goal_nodes:
        print(-1)
        return

    # ダイクストラ：状態はノード。比較は (時間, 乗換え回数)
    # 順序付けは時間が第一、乗換え回数が第二
    dist = [(10**15, 10**15)] * node_num
    dist = list(dist)
    hq = []
    for sn in start_nodes:
        dist[sn] = (0, 0)
        heapq.heappush(hq, (0, 0, sn))  # time, change, node

    while hq:
        time_cur, change_cur, node = heapq.heappop(hq)
        if dist[node] < (time_cur, change_cur):
            continue
        if node in goal_nodes:
            print(time_cur, change_cur)
            return
        for nxt, cost, change_add in graph[node]:
            time_nxt = time_cur + cost
            change_nxt = change_cur + change_add
            if (time_nxt, change_nxt) < dist[nxt]:
                dist[nxt] = (time_nxt, change_nxt)
                heapq.heappush(hq, (time_nxt, change_nxt, nxt))

    print(-1)

if __name__ == '__main__':
    main()