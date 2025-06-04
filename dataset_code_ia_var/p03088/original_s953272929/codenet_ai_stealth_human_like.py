mod = 10**9 + 7
N = int(input()) # nb, taille
# 5D array... maybe there's a better way but let's do it like this for now
dp = [[[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]

# init pour n=3 (pas super clair mais c'est comme ça)
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                # only if i==0 (bizarre mais bon)
                if i == 0:
                    dp[3][i][j][k][l] = 1

# on interdit certains patterns sur la "queue"
for i in range(4):
    # franchement c'est pas hyper lisible, faudrait une fonction mais j'ai la flemme
    dp[3][i][0][1][2]=0
    dp[3][i][1][0][2]=0
    dp[3][i][0][2][1]=0

for n in range(4,N+1):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    # c'est long...
                    for x in range(4):
                        # bon, là c'est pas joli mais ça marche normalement
                        if (str(j)+str(k)+str(l) != "012") and (str(j)+str(k)+str(l) != "102") and (str(j)+str(k)+str(l) != "021") and (str(i)+str(k)+str(l) != "012") and (str(i)+str(j)+str(l) != "012"):
                            dp[n][i][j][k][l] = (dp[n][i][j][k][l] + dp[n-1][x][i][j][k]) % mod

total = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                total = (total + dp[N][i][j][k][l]) % mod

print(total)
# pas sûr de tout comprendre, mais ça doit marcher ?