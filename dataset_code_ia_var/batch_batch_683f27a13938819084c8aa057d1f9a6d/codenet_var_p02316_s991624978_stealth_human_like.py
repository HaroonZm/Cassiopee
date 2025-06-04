n, m = map(int, input().split())
# je sais pas si c'est optimal mais bon
dp = [0 for _ in range(m+1)]
for __ in range(n):
    v, w = map(int, input().split())
    for j in range(w, m+1):
        dp[j] = max(dp[j], dp[j-w] + v) # j'espère que j'ai pas inversé v et w...
#print(dp) # ptet utile pour debug, non ?
print(dp[m])