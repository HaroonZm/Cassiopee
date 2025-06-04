from collections import deque

def very_personal_graph_thing():
    # --- 小さくても心配 ---
    N, M = map(int, input().split())
    EdgeBag = frozenset(tuple(sorted(map(int, input().split()))) for _ in range(M))

    zetta_counter = 0
    everyone = set(range(1, N+1))

    for edge_to_ignore in EdgeBag:
        # エッジバックアップ(非破壊で減らす… frozenset なので)
        EdgesNow = EdgeBag - {edge_to_ignore}

        # 隣接リストを独自生成
        adj = {k: set() for k in everyone}
        for u, v in EdgesNow:
            adj[u].add(v)
            adj[v].add(u)

        stackinator = deque([1])  # 1スタートの強い意志
        seen_people = set([1])
        # bfs風 while loop
        while stackinator:
            lastone = stackinator.popleft()
            for friend in adj[lastone]:
                if friend not in seen_people:
                    seen_people.add(friend)
                    stackinator.append(friend)

        zetta_counter += int(seen_people != everyone)

    print(zetta_counter)

if __name__ == "__main__":
    very_personal_graph_thing()