n,m= map(int,input().split())
c= list(map(int,input().split()))

dp = [['']*(m+1) for _ in range(n+1)]
dp[0][0] = ''

for i in range(n):
    for money in range(m+1):
        if dp[i][money] == '':
            continue
        for d in range(10):
            cost = c[d]
            new_money = money + cost
            if new_money <= m:
                candidate = dp[i][money] + str(d)
                # Compare lex order to keep minimal number
                if dp[i+1][new_money] == '' or candidate < dp[i+1][new_money]:
                    dp[i+1][new_money] = candidate

res = ''
for money in range(m+1):
    if dp[n][money] != '':
        if res == '' or dp[n][money] < res:
            res = dp[n][money]

if res == '':
    print("NA")
else:
    print(res)