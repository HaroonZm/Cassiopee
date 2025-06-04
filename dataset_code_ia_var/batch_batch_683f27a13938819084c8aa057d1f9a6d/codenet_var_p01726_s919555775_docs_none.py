import string
import sys
readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    s0 = "^" + string.ascii_uppercase + string.ascii_lowercase
    S = list(map(s0.index, readline().strip()))
    N = len(S)
    T = list(map(s0.index, readline().strip()))
    M = len(T)
    base = 59
    mod = 10**9 + 9
    pw = [1]*(N+1)
    r = 1
    for i in range(N):
        pw[i+1] = r = r * base % mod
    h0 = [0]*(M+1)
    r = 0
    for i in range(M):
        h0[i+1] = r = (r * base + T[i]) % mod
    h1 = [0]*(N+1)
    r = 0
    for i in range(N):
        h1[i+1] = r = (r * base + S[i]) % mod
    ans = 0
    for i in range(N-M+1):
        left = 0
        right = M+1
        while left+1 < right:
            mid = (left + right) >> 1
            if h0[mid] == (h1[mid+i] - h1[i] * pw[mid]) % mod:
                left = mid
            else:
                right = mid
        if left < M:
            if (h0[M] - h0[left+1] * pw[M - (left+1)]) % mod == (h1[M+i] - h1[i+left+1] * pw[M - (left+1)]) % mod:
                ans += 1
    write("%d\n" % ans)
solve()