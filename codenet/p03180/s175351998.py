import sys
input = sys.stdin.readline

def f(s):
    if flag[s]:
        return(memo[s])
    # 分けない場合
    p = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (s >> i) & 1 and (s >> j) & 1:
                p += a[i][j]
    t = s
    while True:
        t = (t - 1) & s
        if not t:
            break
        p_ = f(t) + f(t ^ s)
        if p < p_:
            p = p_
    flag[s] = 1
    memo[s] = p
    return(p)

N = int(input()) # 1 <= N <= 16
a = [list(map(int, input().split())) for _ in range(N)]
memo = [0] * (1 << N)
flag = [0] * (1 << N)
print(f((1 << N) - 1))