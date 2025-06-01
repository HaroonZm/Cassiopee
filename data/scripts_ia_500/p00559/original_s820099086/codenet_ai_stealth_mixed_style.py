N, Q, S, T = map(int, input().split())
A = []
for _ in range(N + 1):
    A.append(int(input()))
diff = list(map(lambda i: A[i + 1] - A[i], range(N)))

def calc(v):
    return (-S * v) if v > 0 else (-T * v)

ret = 0
i = 0
while i < N:
    ret += calc(diff[i])
    i += 1

for _ in range(Q):
    a, b, c = map(int, input().split())
    ret -= calc(diff[a - 1])
    diff[a - 1] += c
    ret += calc(diff[a - 1])
    if b != N:
        ret -= calc(diff[b])
        diff[b] -= c
        ret += calc(diff[b])
    print(ret)