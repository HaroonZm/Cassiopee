import sys
input = sys.stdin.readline

h,w = map(int,input().split())

c = []
for i in range(w):
    c.append(chr(150+i))

for i in range(h):
    inp = input()
    for j in range(w):
        c.append(inp[j])
h += 1
h2 = h**2
res = 0

for j in range(1,w):
    
    #d[x][y] : j列目x個とj-1列目y個の時の一致数
    d = [0]*(h2)

    for x in range(1,h):
        for y in range(1,h):
            if c[x*w+j] == c[y*w+j-1]:
                d[x*h+y] = d[x*h+y-h-1] + 1
            else:
                d[x*h+y] = d[x*h+y-h-1]
    
    #dp[x][y] : j列目x個とj-1列目y個までの最小一定数和
    dp = [10**10]*h2

    for i in range(h):
        dp[i] = dp[i*h] = 0

    for x in range(1,h):
        for y in range(1,h):
            if dp[x*h+y-1] < dp[x*h-h+y]:
                dp[x*h+y] = dp[x*h+y-1] + d[x*h+y]
            else:
                dp[x*h+y] = dp[x*h-h+y] + d[x*h+y]
    res += dp[-1]

print(res)