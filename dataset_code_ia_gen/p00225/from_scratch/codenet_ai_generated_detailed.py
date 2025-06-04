import sys
sys.setrecursionlimit(10**7)

# 関数説明:
# このプログラムは、与えられた単語群から「しりとり」が可能かを判定する。
# しりとりの条件は、
# 1) 単語の最後の文字と次の単語の最初の文字が一致し、
# 2) すべての単語を一度ずつ使い、
# 3) 最初の単語の最初の文字と最後の単語の最後の文字が一致する
# ことである。
#
# この問題はグラフのオイラー路またはオイラー閉路判定に帰着される。
# 単語の最初と最後の文字をノードとし、その間に辺（単語）を張る。
# すべての辺を一度ずつ通るパス（オイラー路）が存在し、
# さらに「閉路」（オイラー閉路）である必要があるため、
# 連結性の確認と同時にノードの次数の条件を判定する。

def can_make_shiritori(words):
    # 単語の最初と最後の文字で表されるノードは26文字以下の英小文字
    # グラフの次数、入次数、出次数を管理
    out_degree = [0]*26 # 出次数
    in_degree = [0]*26  # 入次数
    graph = [[] for _ in range(26)] # グラフの辺集合（隣接リスト）
    used_nodes = set()  # 単語の始まりまたは終わりに現れるノードを保存
    word_count = len(words)
    
    # 辺を張る
    for w in words:
        start = ord(w[0]) - ord('a')
        end = ord(w[-1]) - ord('a')
        out_degree[start] += 1
        in_degree[end] += 1
        graph[start].append(end)
        used_nodes.add(start)
        used_nodes.add(end)
    
    # 次にグラフの連結性を判定する。
    # しりとりは使われるノードのみで連結なオイラー路である必要があるため、
    # 入力単語の開始と終了ノードで少なくとも1つのノードからDFSし、
    # 使われた辺とノードがすべて訪問可能であることを確認する。
    
    # 連結判定のため無向グラフを作成（出次数・入次数は無視）
    undirected_graph = [[] for _ in range(26)]
    for u in range(26):
        for v in graph[u]:
            undirected_graph[u].append(v)
            undirected_graph[v].append(u)
    
    # DFSで連結なノード集合を探る
    def dfs(u, visited):
        visited[u] = True
        for nxt in undirected_graph[u]:
            if not visited[nxt]:
                dfs(nxt, visited)
    
    visited = [False]*26
    
    # 使われるノードのうち1つ目を起点にDFS開始
    start_node = next(iter(used_nodes))
    dfs(start_node, visited)
    
    # 使われているノードのうち訪問できなかったノードがあればNG
    for node in used_nodes:
        if not visited[node]:
            return False
    
    # オイラー路・閉路の判定
    # すべてのノードのin_degree と out_degree の差を調べる
    # 今回は閉路の条件（最初の単語の最初の文字と最後の単語の最後の文字が同じ）なので
    # in_degree[node] == out_degree[node] がすべてのノードで必要
    
    for i in range(26):
        if in_degree[i] != out_degree[i]:
            return False
    
    # 上記条件を満たしていれば、しりとりで単語を順に並べて
    # 最初と最後も同じ文字で終わるパスが存在する (オイラー閉路の存在)
    return True

def main():
    input = sys.stdin.readline
    while True:
        n = input()
        if not n:
            break
        n = n.strip()
        if n == '0':
            break
        n = int(n)
        words = [input().strip() for _ in range(n)]
        if can_make_shiritori(words):
            print("OK")
        else:
            print("NG")

if __name__ == "__main__":
    main()