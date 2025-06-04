import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        # 0-indexed internally
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 目的は各頂点iの美しさをa[i]からb[i]に変えること。
    # 操作は頂点iのボタンを押すと、iの美しさは隣接数kだけ減り、
    # 隣接する各頂点は1ずつ増える。
    #
    # この変化は隣接した2頂点間で「美しさの差」を移動させるイメージと考えられる。
    #
    # 問題は、合計押下回数の最小化。
    #
    # 解法の要点は木を根としてDFSし、差分を集約していくこと。
    # 各頂点での「美しさの変化量の差 delta_i = a_i - b_i」(初期 - 目標)
    # を根から葉に流すことで、その差を埋める押下回数を計算する。
    #
    # 具体的には根を1(0-indexで0)に設定し、再帰で子からの「美しさの流れ」を集約。
    # 各頂点において、
    # 自身での差分 + 子からの合計差分を親に返す。
    # 押す回数の合計は差分の絶対値の和に等しい。
    #
    # なぜなら、ボタンを押すことで各辺間の差が1ずつ移動し、
    # 差分を辺にそって運ばねばならないため、その移動の絶対値和が最小押下回数になる。
    #
    # 実装では根からDFSし、子を訪れて子の差分を得て絶対値を加算。
    # これを繰り返し、根の返り値は最終的に0（sum a_i = sum b_i のため）
    # 押した回数の合計は各辺で押す回数の絶対値の合計なので、DFS中に加算していく。

    sys.setrecursionlimit(10**7)

    ans = 0

    def dfs(cur, parent):
        nonlocal ans
        diff = a[cur] - b[cur]  # 差分
        for nxt in edges[cur]:
            if nxt == parent:
                continue
            child_diff = dfs(nxt, cur)
            # 子からの差分を集約
            diff += child_diff
            # 差を移動させるために必要な押下回数は差分の絶対値
            ans += abs(child_diff)
        return diff

    dfs(0, -1)
    print(ans)

if __name__ == "__main__":
    main()