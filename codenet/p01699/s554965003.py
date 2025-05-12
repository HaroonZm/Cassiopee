import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    N = int(readline())
    if N == 0:
        return False
    A = [0]*N; B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, readline().split())
    dp = [[0]*(1 << (3*N)) for i in range(2*N+1)]
    for i in range(1, 10):
        c = 0
        if A[0] <= i <= B[0]:
            c |= 1
        if A[0]//10 <= i < B[0]//10 or A[0]//10 == B[0]//10 == i:
            c |= 2
        if A[0]//10 < i <= B[0]//10:
            c |= 4
        dp[1][c] += 1
    N0 = 1 << (3*N)
    for i in range(1, N*2):
        dp0 = dp[i]
        dp1 = dp[i+1]
        for j in range(1, N0):
            v = dp0[j]
            if v == 0:
                continue
            for k in range(10):
                c = 0
                for l in range(N):
                    a0 = A[l]; b0 = B[l]
                    s = 1 << (3*l)
                    if j & s and l < N-1 and k > 0:
                        a1 = A[l+1]; b1 = B[l+1]
                        if a1 <= k <= b1:
                            c |= (s << 3)
                        if a1//10 <= k < b1//10 or a1//10 == b1//10 == k:
                            c |= (s << 4)
                        if a1//10 < k <= b1//10:
                            c |= (s << 5)
                    if j & (s << 1):
                        if j & (s << 2):
                            c |= s
                        elif a0//10 == b0//10:
                            if a0%10 <= k <= b0%10:
                                c |= s
                        elif a0%10 <= k:
                            c |= s
                    if j & (s << 2):
                        if k <= b0%10:
                            c |= s
                if c:
                    dp1[c] += v
    ans = 0
    for i in range(2*N+1):
        dpi = dp[i]
        ans += sum(dpi[j] for j in range(N0) if j & (1 << (3*N-3)))
    write("%d\n" % ans)
    return True
while solve():
    ...