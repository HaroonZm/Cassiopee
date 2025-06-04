# 入力された依存関係からグラフ（有向グラフ）を作成し、循環（サイクル）の有無を検出するプログラムを作成する。
# ユーザとデータをノードとして管理し、矢印の向きに注意してグラフを構築。
# u lock d : データdからユーザuへ向かうエッジを追加
# u wait d : ユーザuからデータdへ向かうエッジを追加
# グラフにサイクルがあるかどうかは、DFSによる頂点の訪問状態管理で検出

import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(sys.stdin.readline())
    
    # ユーザIDとデータIDを区別してノードとして扱うために、文字列として管理する
    # ユーザは "U"+番号、データは "D"+番号 とする
    graph = dict()  # 各ノードに対して出るエッジのリストを保持
    
    def add_edge(frm, to):
        if frm not in graph:
            graph[frm] = []
        graph[frm].append(to)
    
    # 入力を受け取り、グラフに変換
    for _ in range(N):
        line = sys.stdin.readline().strip()
        u_str, rel, d_str = line.split()
        user_node = "U" + u_str
        data_node = "D" + d_str
        
        if rel == "lock":
            # データ -> ユーザ
            add_edge(data_node, user_node)
        else:
            # wait: ユーザ -> データ
            add_edge(user_node, data_node)
    
    # サイクル検出用のフラグと訪問状態
    # 0: 未訪問, 1: 探索中, 2: 探索済
    visited = dict()
    for node in graph.keys():
        visited[node] = 0
    # グラフに存在するノードは鍵だけでなく値（to）もあるので、
    # 全ノードを集める目的で、追加
    for edges in graph.values():
        for node in edges:
            if node not in visited:
                visited[node] = 0
    
    def dfs(v):
        visited[v] = 1  # 探索中
        for nxt in graph.get(v, []):
            if visited[nxt] == 0:
                if dfs(nxt):
                    return True
            elif visited[nxt] == 1:
                # 探索中のノードに再度訪問＝サイクル検出
                return True
        visited[v] = 2  # 探索済
        return False
    
    # ノードが複数あることがあるので、すべてのノードからDFSを行いサイクル検出
    for node in visited.keys():
        if visited[node] == 0:
            if dfs(node):
                print(1)
                return
    
    print(0)

if __name__ == "__main__":
    main()