mod = 10**9 + 7
stering = [[-1]*1001 for _ in range(1001)]
for i in range(1001):
    stering[i][1] = 1
    stering[i][i] = 1

def roop(n, k):
    if stering[n][k] != -1:
        return stering[n][k]
    else:
        stering[n][k] = (roop(n-1, k-1) + k * roop(n-1, k)) % mod
        return stering[n][k]

n, k = [int(s) for s in input().split()]
if n < k:
    print(0)
else:
    ans = roop(n, k)
    print(ans)