n = int(input())
abc = []
for i in range(n):
    abc += [list(map(int, input().split()))]

def update(dp, abcs, i):
    for current in range(3):
        for prev in range(3):
            if prev != current:
                dp[i+1][current] = max(dp[i+1][current], dp[i][prev] + abcs[i][current])

dp = []
dp.append([0]*3)
for idx in range(n):
    dp.append([0,0,0])
    update(dp, abc, idx)

result = 0
for c in [0,1,2]:
    result = max(result, dp[-1][c])

print(result)