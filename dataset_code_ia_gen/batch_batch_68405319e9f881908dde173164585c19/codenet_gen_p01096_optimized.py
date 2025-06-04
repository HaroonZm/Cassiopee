import sys
sys.setrecursionlimit(10**7)

def max_removed(blocks):
    n = len(blocks)
    dp = [[0]*(n) for _ in range(n)]
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if length == 2:
                if abs(blocks[i] - blocks[j]) <= 1:
                    dp[i][j] = 2
            else:
                # remove ends if possible and inner fully removed
                if abs(blocks[i] - blocks[j]) <= 1 and dp[i+1][j-1] == length-2:
                    dp[i][j] = length
                # try splitting
                for k in range(i, j):
                    if dp[i][k] + dp[k+1][j] > dp[i][j]:
                        dp[i][j] = dp[i][k] + dp[k+1][j]
    return dp[0][n-1]

input_data = sys.stdin.read().strip().split()
idx = 0
while True:
    if idx >= len(input_data):
        break
    n = int(input_data[idx])
    idx +=1
    if n ==0:
        break
    blocks = list(map(int, input_data[idx:idx+n]))
    idx += n
    print(max_removed(blocks))