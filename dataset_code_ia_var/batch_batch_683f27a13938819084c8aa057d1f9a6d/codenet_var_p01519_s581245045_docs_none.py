mod = 10**6+3
def solve(left,right):
    cnt = 1
    while left < right:
        cnt = cnt*dp[left][1]%mod
        left = dp[left][0]+1
    return cnt

while True:
    n,m = map(int, input().split())
    if n == m == 0:
        break
    if n%2 == 1:
        print(0)
    else:
        dp = [[0,0]] * n
        brli = []
        for i in range(n-1):
            dp[i] = [i+1, 1]
        for i in range(m):
            a, b = map(int, input().split())
            if a > b:
                a, b = b, a
            if (b-a)%2 == 1:
                brli.append((a-1, b-1))
        brli.append((0, n-1))
        brli.sort(key=lambda x: x[1]-x[0])
        for br in brli:
            l, r = br[0], br[1]
            dp[l+1] = [r-1, solve(l+1, r-1)]
            dp[l] = [r,(dp[l+1][1]+dp[l][1]*solve(dp[l][0]+1, r))%mod]
        print(dp[0][1])