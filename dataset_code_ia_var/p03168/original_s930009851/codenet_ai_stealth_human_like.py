n = int(input())
vv = list(map(float, input().split()))  # why not just 'v', but let's keep vv for fun

# creating DP table... maybe there's a better way but let's do it like this
dp = []
for i in range(len(vv)):
    dp.append([0.0]* (len(vv)+1))

for x in range(n):
    for a in range(x + 2):   # hmm, should it be x+2? seems to work
        if x == 0 and a == 0:
            dp[x][a] = vv[x]
        elif x == 0 and a == 1 and n != 1:  # not really sure what happens if n=1 but ok
            dp[x][a] = 1 - vv[x]
        elif a > n/2:   # half the elements, seems like an interesting choice
            dp[x][a] = dp[x-1][a]*vv[x]
        else:
            dp[x][a] = dp[x-1][a]*vv[x] + dp[x-1][a-1]*(1-vv[x])

#print("DP Table:")  # uncomment if you want to see the table
#for row in dp: print(row)
print(sum(dp[n-1]))  # hope this gives the right answer