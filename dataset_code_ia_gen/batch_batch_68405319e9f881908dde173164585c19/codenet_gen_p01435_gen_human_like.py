import sys
sys.setrecursionlimit(10**7)

N, E, T = map(int, input().split())
W = list(map(int, input().split()))

# 合成法則を魔女ごとにまとめる
# key: 魔女番号, value: list of lists（素材の魔女番号リスト）
recipes = [[] for _ in range(N)]
for _ in range(E):
    G, C, *S = map(int, input().split())
    recipes[G - 1].append([s - 1 for s in S])

INF = 10**9
memo = [-1] * N  # -1: 未計算

def dp(w):
    if memo[w] != -1:
        return memo[w]
    # 手に入りやすい魔女なら必要なタネは1
    if W[w] == 1:
        memo[w] = 1
        return 1
    # 合成法則がないなら作れない
    if not recipes[w]:
        memo[w] = INF
        return INF
    res = INF
    for recipe in recipes[w]:
        # 同じ魔女を複数個同時に使えない → 全て異なる魔女なので問題なし
        total = 0
        for subw in recipe:
            subcost = dp(subw)
            if subcost == INF:
                break
            total += subcost
        else:
            # 合成に使う特別なタネの数は合成元の合計ではなく、素材特別タネ数の合計－(素材数－1)
            # 問題文にあるように合成後、素材数のうち1個が新しい魔女として残りは空になるので
            # 少なくとも必要なタネ数は素材の合計数から素材数-1引いた値
            # 実際は素材同士が重複しないので、素材合計そのままで良い。
            # よって単純に素材の合計は sum(dp(subw)) で良い。
            # しかし素材特別タネ数はそれぞれ最小値であり、合成で得られる魔女は1個。なので素材数が多いほど複数個の種を使う必要がある。
            # 素材の魔女は別々の特別タネにいるため合計が必要数の最低値になる。
            res = min(res, total - (len(recipe) - 1))
    memo[w] = res
    return res

ans = dp(T - 1)
if ans >= INF:
    print(-1)
else:
    print(ans)