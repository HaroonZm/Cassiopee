N = int(input())
T = [int(input()) for i in range(N)]
T.sort()
if N == 1:
    ans = 0
else:
    y = T[-1]
    R = []
    for x in range(1, y+1):
        if y % x == 0:
            R.append(x)
    cur = ans = 0
    for t in T:
        while R[cur] < t:
            cur += 1
        ans += R[cur] - t
print(ans)