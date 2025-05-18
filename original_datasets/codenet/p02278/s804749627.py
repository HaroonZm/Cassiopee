n = int(input())
w = list(map(int, input().split()))
s = sorted(w)

cost = 0
for i in range(n):
    # 最小の要素と最小の要素の位置に適した要素と交換していく
    now_v = s[i]
    now_idx = w.index(s[i])
    j = 0 # 交換回数
    while now_idx > i:
        j += 1
        target_v = s[now_idx]
        target_idx = w.index(target_v)
        cost += w[target_idx] # ターゲットの方だけ足していく
        w[now_idx], w[target_idx] = w[target_idx], w[now_idx]
        now_idx = target_idx
    # now_v * j: 普通の交換。
    # now_v * 2 + s[0] * (j + 2): 
    #       s[0]は最小値。
    #       最小値と現在値を交換して(コスト: now_v + s[0])、
    #       ソート完了後に(コスト: s[0] * j)
    #       最小値と現在値を元に戻すコスト(コスト: now_v + s[0])。
    #       2回以上ならこっちが少ない。
    cost += min(now_v * j, now_v * 2 + s[0] * (j + 2))
print(cost)