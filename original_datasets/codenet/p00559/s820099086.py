N, Q, S, T = map(int, input().split())
A = [int(input()) for i in range(N + 1)]
diff = [A[i + 1] - A[i] for i in range(N)]

def calc(v):
    if v > 0:
        return -S * v
    else:
        return -T * v

ret = 0
for i in range(N):
    ret += calc(diff[i])
    
for i in range(Q):
    a, b, c = map(int, input().split())
    ret -= calc(diff[a - 1])
    diff[a - 1] += c
    ret += calc(diff[a - 1])
    if b != N:
        ret -= calc(diff[b])
        diff[b] -= c
        ret += calc(diff[b])
    print(ret)