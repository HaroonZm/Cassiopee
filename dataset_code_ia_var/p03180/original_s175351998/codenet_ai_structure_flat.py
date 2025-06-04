import sys
input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
memo = [0] * (1 << N)
flag = [0] * (1 << N)

stack = []
stack.append(( (1 << N) - 1, 0 )) # (s, step) ; step=0:entrance, 1:resume after rec

while stack:
    s, step = stack.pop()
    if step == 0:
        if flag[s]:
            continue
        p = 0
        for i in range(N):
            for j in range(i + 1, N):
                if ((s >> i) & 1) and ((s >> j) & 1):
                    p += a[i][j]
        memo[s] = p
        t = s
        candidate = []
        while True:
            t = (t - 1) & s
            if not t:
                break
            if not flag[t]:
                stack.append((s, 1))
                stack.append((t, 0))
                break
            if not flag[t ^ s]:
                stack.append((s, 1))
                stack.append((t ^ s, 0))
                break
            p_ = memo[t] + memo[t ^ s]
            if memo[s] < p_:
                memo[s] = p_
        else:
            flag[s] = 1
    else:
        t = s
        while True:
            t = (t - 1) & s
            if not t:
                break
            if not flag[t]:
                stack.append((s, 1))
                stack.append((t, 0))
                break
            if not flag[t ^ s]:
                stack.append((s, 1))
                stack.append((t ^ s, 0))
                break
            p_ = memo[t] + memo[t ^ s]
            if memo[s] < p_:
                memo[s] = p_
        else:
            flag[s] = 1

print(memo[(1 << N) - 1])