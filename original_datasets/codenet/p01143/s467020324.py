readline = open(0).readline
ans = []
while 1:
    N, M, P = map(int, readline().split())
    if N == 0:
        break
    X = [int(readline()) for i in range(N)]
    s = sum(X)
    t = X[M-1]
    if t == 0:
        ans.append("0\n")
        continue
    ans.append("%d\n" % int(s * (100-P) / t))
open(1, 'w').writelines(ans)