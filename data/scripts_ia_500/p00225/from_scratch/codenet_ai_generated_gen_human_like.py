import sys
sys.setrecursionlimit(10**7)

def can_form_shiritori(words):
    n = len(words)
    # グラフを作る（頂点は a-z の26文字）
    graph = [[] for _ in range(26)]
    in_degree = [0]*26
    out_degree = [0]*26

    # 各単語を辺として追加
    for w in words:
        start = ord(w[0]) - ord('a')
        end = ord(w[-1]) - ord('a')
        graph[start].append(end)
        out_degree[start] += 1
        in_degree[end] += 1

    # オイラー道（オイラー閉路）判定用関数
    def check_eulerian():
        start_nodes = 0
        end_nodes = 0
        for i in range(26):
            diff = out_degree[i] - in_degree[i]
            if diff == 1:
                start_nodes += 1
            elif diff == -1:
                end_nodes += 1
            elif diff != 0:
                return False
        # オイラー閉路またはオイラー道の条件を満たすならTrue
        return (start_nodes == 0 and end_nodes == 0) or (start_nodes == 1 and end_nodes == 1)

    # 強連結成分を判定するためのDFS（使用されている頂点のみ）
    used_vertices = set()
    for w in words:
        used_vertices.add(ord(w[0]) - ord('a'))
        used_vertices.add(ord(w[-1]) - ord('a'))

    # 辺のある頂点からDFS
    def dfs(u, graph, visited):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v, graph, visited)

    # 逆辺のグラフを作る
    reverse_graph = [[] for _ in range(26)]
    for u in range(26):
        for v in graph[u]:
            reverse_graph[v].append(u)

    # すべての単語の最初の文字をもつ頂点から出発
    # 代表として、単語の先頭文字の頂点を一つ選ぶ
    start_vertex_candidates = [i for i in range(26) if out_degree[i] - in_degree[i] == 1]
    if start_vertex_candidates:
        start_vertex = start_vertex_candidates[0]
    else:
        start_vertex = next(iter(used_vertices))

    visited = [False]*26
    dfs(start_vertex, graph, visited)
    for v in used_vertices:
        if not visited[v]:
            return False

    visited = [False]*26
    dfs(start_vertex, reverse_graph, visited)
    for v in used_vertices:
        if not visited[v]:
            return False

    # トータルの入次数と出次数の条件
    if not check_eulerian():
        return False

    # さらに条件：最初の単語の最初の文字と最後の単語の最後の文字が同じこと
    # オイラー路なら、始点と終点の文字は異なるが、問題の条件は閉路（始点=終点）
    # なのでオイラー閉路でなければダメ
    count_start_end_diff = 0
    for i in range(26):
        if out_degree[i] != in_degree[i]:
            count_start_end_diff += 1
    if count_start_end_diff != 0:
        return False
    # 条件満たせばOK
    return True

input_lines = sys.stdin.read().strip().split('\n')
idx = 0
while True:
    if idx >= len(input_lines):
        break
    n = input_lines[idx]
    idx += 1
    if n == '0':
        break
    n = int(n)
    words = input_lines[idx:idx+n]
    idx += n
    print('OK' if can_form_shiritori(words) else 'NG')