def solve():
    # 方針
    # 範囲で並べ方の個数を足し合わせるDP
    
    N = int(input())
    X = [int(input()) for _ in range(N)]
    MOD = int(1e9)+7
    
    colors = set()
    NoDouble = [-1]
    for x in X:
        colors.add(x)
        if x == NoDouble[-1]:
            continue
        NoDouble.append(x)
    del NoDouble[0]
    N = len(NoDouble)
    C = len(colors)

    ForIdxLastNum = [-1] * N # N番目の要素まで見たとき、その色は直前にどこに出現したか
    # 上記を作成するために、inplace な色の出現の位置を記憶
    Onetime_colors = [-1] * (2*10**5+1)

    for e,c in enumerate(NoDouble):
        if Onetime_colors[c] == -1:
            # その色は初出
            Onetime_colors[c] = e
        else:
            ForIdxLastNum[e] = Onetime_colors[c]
            Onetime_colors[c] = e
    
    
    DP = [0] * (N+1) # dp[i], i個目まで見たときの並べ方の個数
    DP[0] = 1

    for e,c in enumerate(NoDouble):
        if ForIdxLastNum[e] == -1:
            # その色は初出
            DP[e+1] = DP[e]
        else:
            lastIdx = ForIdxLastNum[e]
            DP[e+1] = (DP[lastIdx+1] + DP[e]) % MOD
    
    print(DP[N] % MOD)

            
    
    

if __name__ == "__main__":
    solve()