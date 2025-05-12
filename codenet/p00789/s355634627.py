import sys
readline = sys.stdin.readline
write = sys.stdout.write
dp = [0]*601
dp[0] = 1
V = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289]
for v in V:
    for k in range(300, -1, -1):
        x = dp[k]
        w = v
        while k+w <= 300:
            dp[k+w] += x
            w += v

while 1:
    N = int(readline())
    if not N:
        break
    write("%d\n" % dp[N])