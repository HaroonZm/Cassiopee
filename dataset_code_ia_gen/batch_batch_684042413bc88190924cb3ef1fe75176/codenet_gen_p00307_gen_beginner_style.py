M, N = map(int, input().split())
weights = []
thicks = []
for _ in range(M):
    w, t = map(int, input().split())
    weights.append(w)
    thicks.append(t)
caps = []
widths = []
for _ in range(N):
    c, b = map(int, input().split())
    caps.append(c)
    widths.append(b)

# まず累積和を作る（重さと厚さ）
w_cum = [0]
t_cum = [0]
for i in range(M):
    w_cum.append(w_cum[-1] + weights[i])
    t_cum.append(t_cum[-1] + thicks[i])

def can_place(x):
    # x巻まで並べられるか判定（0の場合は何も並べないので常にTrue）
    if x == 0:
        return True
    # 段ごとに連続巻数を並べる必要あり
    # dp[i] = Trueなら、i巻まできちんと並べられるという意味
    # iは0からxまで
    dp = [False]*(x+1)
    dp[0] = True
    for i in range(x):
        if not dp[i]:
            continue
        # 次の段に本を何巻並べるか試す
        for j in range(i+1, x+1):
            w_sum = w_cum[j] - w_cum[i]
            t_sum = t_cum[j] - t_cum[i]
            seg_index = -1
            # 現在並べる段は何段目かを求める
            # iまでは何巻並べているので段の数カウント
            used_shelves = 0
            count = i
            for shelf_i in range(N):
                used_shelves += 1
                # 段ごとにdpの遷移なので段は1ずつ増やす
                # ここから並べる巻数はj - iなので1段で収まる必要あり
                if used_shelves == used_shelves:
                    seg_index = shelf_i
                    break
            # 上記の段数計算を簡単にするため、改めて試す
            # approachを変えて段ごとに並べることを試す
            # ここは非効率だけど段ごとに試す
            pass
    # ここは処理を簡単にするため段ごとに並べることを確認する処理を別に作る
    return False

# 上の判定は複雑なので、段数は最大15なので逐次的に解くやり方に切り替える

def possible(x):
    # x巻まで並べるかどうか調べる
    # xが0ならTrue
    if x == 0:
        return True
    # dp[i] = Trueならi巻まで層割りできる
    dp = [False]*(x+1)
    dp[0] = True
    for shelf in range(N):
        ndp = [False]*(x+1)
        for i in range(x+1):
            if not dp[i]:
                continue
            # shelf段目に何巻か並べる
            for j in range(i+1, x+1):
                w_sum = w_cum[j]-w_cum[i]
                t_sum = t_cum[j]-t_cum[i]
                if w_sum <= caps[shelf] and t_sum <= widths[shelf]:
                    ndp[j] = True
                else:
                    break
        dp = ndp
        if dp[x]:
            return True
    return False

low = 0
high = M+1
while high - low > 1:
    mid = (low+high)//2
    if possible(mid):
        low = mid
    else:
        high = mid

print(low)