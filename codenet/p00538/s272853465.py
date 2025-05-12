n  = int(input())
a  = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    if i%2 == n%2:
        dp = [ dp[(l+1)%n] if a[l]>a[(l+i)%n] else dp[l] for l in range(n)]
    else:
        dp = [ max( a[l]+dp[(l+1)%n], a[(l+i)%n]+dp[l] ) for l in range(n)]

print(max(dp))