from functools import reduce

def get_input():
    return list(map(int, input().split()))
    
MOD = 10**9 + 7

def main():
    n, k = get_input()
    dp = []
    for i in range(k+1):
        dp.append([0]*(n+1))
    dp[0][0]=1
    for index in range(1, k+1):
        j = 0
        while j <= n:
            if j - index >= 0:
                dp[index][j] = (dp[index-1][j] + dp[index][j-index]) % MOD
            else:
                dp[index][j] = dp[index-1][j]
            j += 1
    print((lambda row,col: row[col]) (dp[k], n))

if __name__ == '__main__':
    main()