import sys
input = sys.stdin.readline
n,k = map(int,input().split())
a = tuple(map(int,input().split()))

dp = [False] + [True]*k
for i in range(1,k+1):
    judge = False
    for j in range(n):
        if i-a[j] >= 0 and not dp[i-a[j]]:
            judge = True
    dp[i] = judge

if dp[k]:
    print('First')
else:
    print('Second')