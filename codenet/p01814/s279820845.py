import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    base = 37; MOD = 10**9 + 9
    S = readline().strip()
    L = len(S)
    H = [0]*(L+1)
    pw = [1]*(L+1)
    ca = ord('a')
    v = 0
    for i in range(L):
        H[i+1] = v = (v * base + (ord(S[i]) - ca)) % MOD
    v = 1
    for i in range(1, L+1):
        pw[i] = v = v * base % MOD
    Q = int(readline())
    for i in range(Q):
        l, r, t = map(int, readline().split()); l -= 1
        m = r-l
        if ((H[r]-H[r-t]) - (H[l+t]-H[l]) * pw[m-t]) % MOD == 0:
            write("Yes\n")
            continue
        left = 0; right = m-t+1
        base = H[l] - H[l+t]
        while left+1 < right:
            mid = (left + right) >> 1
            if ((H[l+mid]-H[l+t+mid]) - base * pw[mid]) % MOD == 0:
                left = mid
            else:
                right = mid
        l1 = left
        left = 0; right = m-t-l1+1
        base = (H[r-t]-H[r]) % MOD
        while left+1 < right:
            mid = (left + right) >> 1
            if (H[r-t-mid]-H[r-mid]) * pw[mid] % MOD == base:
                left = mid
            else:
                right = mid
        l2 = left
        if l1+l2+1 == m-t:
            if l1 <= t or l2 <= t:
                write("Yes\n")
            else:
                write("No\n")
        else:
            if ((H[l+m-t-l2-1]-H[l+m-l2-1]) - (H[l+l1+1]-H[l+t+l1+1]) * pw[m-t-l2-l1-2]) % MOD != 0:
                write("No\n")
            else:
                p1 = l1; p2 = m-t-l2-1
                if p2 - p1 == t and S[l+p2-t] == S[l+p2+t]:
                    write("Yes\n")
                else:
                    write("No\n")
solve()