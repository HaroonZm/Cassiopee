import sys
readline = sys.stdin.readline
write = sys.stdout.write
def solve():
    H, N = map(int, readline().split())
    if H == N == 0:
        return False
    def get_block():
        s = readline().strip()
        v = (s[0] == '#') + (s[1] == '#')*2
        s = readline().strip()
        v += (s[0] == '#')*4 + (s[1] == '#')*8
        return v
    R = []
    for i in range(H):
        R.append(get_block())
    R.extend([0]*8)
    H += 8
    I = []
    for i in range(N):
        v = get_block(); w = get_block()
        if v == 0:
            v, w = w, 0
        if v & 3 == 0 and w & 3 == 0:
            v >>= 2; w >>= 2
        if v & 5 == 0 and w & 5 == 0:
            v >>= 1; w >>= 1
        I.append((v, w))
    def dfs(i, R0):
        if i == N:
            return 0
        v0, w0 = I[i]
        r = 0
        for k, f in ((0, 0), (1, 5), (2, 3), (3, 0)):
            v = v0 << k; w = w0 << k
            if v >= 16 or w >= 16 or v & f or w & f:
                continue
            h = H-1
            while h and R0[h-1] & v == 0 and R0[h] & w == 0:
                h -= 1
            R = R0[:]
            R[h] |= v; R[h+1] |= w
            c = 0
            if R[h+1] == 15:
                for j in range(h+2, H):
                    R[j-1] = R[j]
                c += 1
            if R[h] == 15:
                for j in range(h+1, H):
                    R[j-1] = R[j]
                c += 1
            r = max(r, dfs(i+1, R) + c)
        return r
    write("%d\n" % dfs(0, R))
    return True
while solve():
    ...