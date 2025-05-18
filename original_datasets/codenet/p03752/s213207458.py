N,K = map(int,input().split())
A = list(map(int,input().split()))
if K==1:
    print(0)
    exit()

ans = 10**12
for b in range(1<<(N-1)):
    h = A[0]
    k = 1
    cost = 0
    for i in range(N-1):
        a = A[i+1]
        if a > h:
            k += 1
            h = a
        elif b&(1<<i):
            k += 1
            cost += h+1 - a
            h += 1
    if k >= K:
        ans = min(ans, cost)
print(ans)