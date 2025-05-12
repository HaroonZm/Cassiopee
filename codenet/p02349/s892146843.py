import sys
readline = sys.stdin.readline
write = sys.stdout.write
N, Q = map(int, readline().split())

data = [0]*(N+1)
def add(k, x):
    while k <= N:
        data[k] += x
        k += k & -k

def get(k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

ans = []
for q in range(Q):
    t, *cmd = map(int, readline().split())
    if t:
        ans.append(str(get(cmd[0])))
    else:
        s, t, x = cmd
        add(s, x)
        if t < N:
            add(t+1, -x)
write("\n".join(ans))
write("\n")