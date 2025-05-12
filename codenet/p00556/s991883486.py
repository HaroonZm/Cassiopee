def main():
    N,M = map(int,input().split())
    a = [int(input())-1 for _ in N*[0]]
    sum = [N*[0] for _ in 20*[0]]
    cnt = 20*[0]
    ans_bit = 0
    for i in range(N):
        ans_bit = ans_bit | (1<<a[i])
        cnt[a[i]] += 1
        sum[a[i]][i] += 1
        if i-1 >= 0:
            for j in range(20):
                sum[j][i] += sum[j][i-1]
    dp = [10**9]*(1<<20)
    dp[0] = 0
    for bit in range(1<<20):
        if( dp[bit] == 10**9 ):
            continue
        v = 0
        for used in range(20):
            if( (bit>>used) & 1 ):
                v += cnt[used]
        for use in range(20):
            if( cnt[use] == 0 ):
                continue
            if( (bit>>use) & 1 ):
                continue
            w = v + cnt[use]
            not_move = sum[use][w-1]
            if( v-1 >= 0 ):
                not_move -= sum[use][v-1]
            move = cnt[use] - not_move
            dp[bit|(1<<use)] = min(dp[bit|(1<<use)],
                                   dp[bit]+move)
    print(dp[ans_bit])
            

if __name__ == "__main__":
    main()