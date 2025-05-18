import copy

def main():
    """
    自己ループを含まない
    二重辺を含まない: 点AからBへの辺は１つ(以下)
    連結グラフ：任意の点から任意の点に移動できる

    ある辺を取り除くと非連結になる場合、その辺を橋という
    →橋がなくなるとたどり着けない

    N: <=50
    M: <= 50

    ある辺を取り除いてすべてのノードにたどり着けるか
    すべてのノードを列挙する
    ノードを辿ってみる（探索アルゴリズム）
    たどれたらたどれたノードをため込む
    終わったら列挙したノードと比較して同じならOK
    """
    N, M = map(int, input().split())
    e = set()
    for _ in range(M):
        a, b = map(int, input().split())
        e.add((a, b))

    ans = 0
    for k in e:
        searched = set()
        e_copy = copy.deepcopy(e)
        e_copy.remove(k)

        def dfs(v1):
            searched.add(v1)
            for v2 in range(1, N + 1):
                if v2 in searched:
                    continue
                if (v1, v2) in e_copy or \
                        (v2, v1) in e_copy:
                    dfs(v2)

        dfs(1)
        if len(searched) < N:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()