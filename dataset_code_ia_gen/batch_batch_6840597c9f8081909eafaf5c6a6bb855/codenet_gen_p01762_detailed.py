import sys
sys.setrecursionlimit(10**7)

def main():
    N = int(sys.stdin.readline())
    # 0番目は根なので蝉0と仮定し、入力からずれるためN-1個読み取る
    C = list(map(int, sys.stdin.readline().split()))
    # 根0の蝉数=0を頭に追加し、頂点0～N-1の蝉数リストを作成
    cicadas = [0] + C

    # 各頂点の隣接リスト（(隣接頂点, 労力)のペアのリスト）
    graph = [[] for _ in range(N)]

    # 枝情報入力。N-1本の辺
    # 各辺の情報はu,v,pとして与えられるが、問題文の形式を踏襲しながら読み込む
    # 入力の形式よりu,v,pの順でN-1本分与えられるがそれぞれが別行で入るケースサンプルなので
    # まとめて読み取る

    # 総行数として2*(N-1)行の辺情報が与えられていると仮定し、
    # 実際は1行にu,v,p全て整数の3つがあると想定し直すため、
    # こちらの想定が合わなければ下のように修正する
    #
    # しかし問題文入力例を見ると、
    # u_i
    # v_i
    # p_i
    # と1つずつ別行にある形式に見える
    # よって以下のように3行単位で読み込むが、サンプル問題の入力と合わないため、
    # 実際には一行にu v pを読み取る書き換えを行う

    # 問題文とサンプルのズレを考慮して、u,v,pが一行ずつ3行単位で入力されると仮定する形から、
    # サンプルを見ると N=5 のとき5行目以降に 0 1 4 のように1行にu,v,pがまとまっている形なので、
    # ここは1行に3つ読む形式で書き換えた。

    for _ in range(N - 1):
        u,v,p = map(int, sys.stdin.readline().split())
        graph[u].append((v, p))
        graph[v].append((u, p))

    # 各頂点のsubtree内の蝉の総数を計算する。
    # DFSで部分木の蝉数を集約しつつ、
    # 枝を切るか切らないかの最小労力を計算する。

    # dfs関数は根からスタートし、親を引数で渡して再帰。
    # 戻り値として
    # 1. その頂点の部分木全体の蝉の数
    # 2. 部分木の蝉を駆除するための最小労力

    def dfs(v, parent):
        total_cicadas = cicadas[v]
        total_cost = 0
        for nv, cost in graph[v]:
            if nv == parent:
                continue
            # 子の部分木の蝉数と最小コストを取得
            child_cicadas, child_cost = dfs(nv, v)
            total_cicadas += child_cicadas
            # 枝を切って駆除するコスト(cost)
            # または子の部分木を再帰的に除去するコスト(child_cost)
            # 最小の方を選ぶ
            total_cost += min(child_cost, cost)
        return total_cicadas, total_cost

    # 根は0。根に蝉は0匹なので必ず上のdfsが正しく働く
    total_cicadas, answer = dfs(0, -1)
    # 全ての蝉を駆除する最小労力が答え
    print(answer)

if __name__ == "__main__":
    main()