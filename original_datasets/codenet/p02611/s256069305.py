import numpy as np

MOD = 10 ** 9 + 7

l_matrix = np.zeros((32, 32), np.uint64)
for i in range(16):
    l_matrix[i+16][i] = 1
    l_matrix[i][i+16] = 1
for i in range(15):
    l_matrix[i+1][i] = 1
for i in range(5, 15):
    l_matrix[i+1][i+16] = 1
    
doubling = [l_matrix] #doubling[i] = (l_matrix) ** (2 ** i) % MOD
for _ in range(30):
    doubling.append(doubling[-1] @ doubling[-1] % MOD)

T = int(input())
for _ in range(T):
    N = int(input())
    N += 10
    dp = np.zeros(32, np.uint64)
    dp[0] = 1
    for i, c in enumerate(reversed(format(N, 'b'))):
        if c == '1':
            dp = doubling[i] @ dp
            dp %= MOD
    print(int((dp[15] + dp[31]) % MOD))
    #print(dp)