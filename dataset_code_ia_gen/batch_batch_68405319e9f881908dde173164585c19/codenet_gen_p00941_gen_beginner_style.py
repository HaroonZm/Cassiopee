import sys
sys.setrecursionlimit(10**7)

S = input().strip()
k = int(input().strip())
n = len(S)

LIMIT = 10**18

# dp[i][j] = number of shortest palindromes for S[i..j]
dp = [[-1]*(n) for _ in range(n)]

def count(i,j):
    if i > j:
        return 1
    if i == j:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    if S[i] == S[j]:
        res = count(i+1,j-1)
    else:
        res = 0
        left = count(i+1,j)
        right = count(i,j-1)
        if left > LIMIT:
            left = LIMIT
        if right > LIMIT:
            right = LIMIT
        res = left + right
        if res > LIMIT:
            res = LIMIT
    dp[i][j] = res
    return res

def build(i,j,k):
    if i > j:
        return ''
    if i == j:
        return S[i]
    if S[i] == S[j]:
        return S[i] + build(i+1,j-1,k) + S[j]
    else:
        left = count(i+1,j)
        if left >= k:
            return S[i] + build(i+1,j,k) + S[i]
        else:
            return S[j] + build(i,j-1,k-left) + S[j]

total = count(0,n-1)
if total < k:
    print("NONE")
else:
    ans = build(0,n-1,k)
    print(ans)