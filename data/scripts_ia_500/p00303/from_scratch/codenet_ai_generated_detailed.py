# デッドロック検出プログラム
# 入力として与えられたユーザとデータの依存関係から、有向グラフを構築し、
# そのグラフにサイクル（循環）が存在するか調べることでデッドロックを検出する。

import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(sys.stdin.readline())  # 依存関係の数
    # グラフの頂点はユーザとデータの集合で構成される。
    # ユーザは "u{番号}" の形式、データは "d{番号}" の形式で頂点名を区別する。
    graph = dict()  # 隣接リストとして表現。キーは頂点名、値は依存先の頂点名リスト
    
    def add_edge(from_node, to_node):
        if from_node not in graph:
            graph[from_node] = []
        graph[from_node].append(to_node)
    
    # 入力の関係を読み込みグラフを構築
    for _ in range(N):
        line = sys.stdin.readline().strip()
        u, rel, d = line.split()
        user_node = f"u{u}"
        data_node = f"d{d}"
        
        if rel == "lock":
            # u lock d → データからユーザへの矢印
            add_edge(data_node, user_node)
        else:
            # u wait d → ユーザからデータへの矢印
            add_edge(user_node, data_node)
    
    # サイクル検出のために深さ優先探索（DFS）を使う
    # 各頂点の状態を管理: 0=未訪問, 1=訪問中(探索中), 2=完了
    visited = dict()
    
    def dfs(node):
        visited[node] = 1  # 探索中
        for nxt in graph.get(node, []):
            if visited.get(nxt, 0) == 0:
                if dfs(nxt):
                    return True
            elif visited.get(nxt) == 1:
                # 探索中の頂点に戻ってきた → サイクル検出
                return True
        visited[node] = 2  # 探索完了
        return False
    
    # グラフ内のすべての頂点を走査してサイクルを検出する
    for node in graph.keys():
        if visited.get(node, 0) == 0:
            if dfs(node):
                print(1)
                return
    
    # サイクルがなければデッドロックなし
    print(0)

if __name__ == "__main__":
    main()