while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    s.sort(reverse=True)
    # 初期状態：押入れにすべての布団をしまう。ここで好きな順序にできるので、大きい順にしておく。
    # ベッドから押入れに、押入れからベッドに1枚ずつしか動かせない。
    # 日ごとにベッドにある布団の枚数を0からNまで動かしやすいように考える。
    # ここでは、ベッドに乗せる枚数を変化させることは制限があるが、その制限を無視して簡単にモジュールを作る。
    # とりあえず、日ごとにベッドの枚数は0~Nまで変わるとし、dpで不快度の最小値を管理する。
    INF = 10**15
    # dp[j][k]: j日目まで終わって、ベッドにk枚の布団が乗っている時の不快度の最小値
    dp = [[INF]*(N+1) for _ in range(M+1)]
    dp[0][0] = 0
    prefix = [0]*(N+1)
    for i in range(N):
        prefix[i+1] = prefix[i] + s[i]
    for j in range(M):
        for k in range(N+1):
            if dp[j][k] == INF:
                continue
            # j日目にベッドにm枚の布団を乗せる
            for m in range(N+1):
                # 0枚からN枚へは一枚ずつしか変えられないが、一日に何回でもできるから問題なし。
                warmth = prefix[m]
                cost = abs(warmth - d[j])
                if dp[j+1][m] > dp[j][k] + cost:
                    dp[j+1][m] = dp[j][k] + cost
    ans = min(dp[M])
    print(ans)