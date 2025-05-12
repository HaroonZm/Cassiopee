N, K = map(int, input().split())
MOD = 10**9 + 7
 
if K < N:
    print(0)
else:
    p = q = 1
    for i in range(N):
        p = p * (K-i) % MOD
        q = q * (i+1) % MOD
 
    print(p * pow(q, MOD-2, MOD) % MOD)