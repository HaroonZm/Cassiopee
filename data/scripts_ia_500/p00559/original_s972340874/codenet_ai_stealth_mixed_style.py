N, Q, S, T = map(int, input().split())
A = []
for _ in range(N+1):
    A.append(int(input()))

C = 0
i = 0
while i < N:
    if A[i] < A[i+1]:
        C += S * (A[i] - A[i+1])
    else:
        C += T * (A[i] - A[i+1])
    i += 1

def add(k, x):
    if x >= 0:
        if B[k] <= 0:
            if B[k] + x <= 0:
                return -T * x
            else:
                return T * B[k] - S * (B[k] + x)
        else:
            return -S * x
    else:
        if B[k] >= 0:
            if B[k] + x >= 0:
                return -S * x
            else:
                return S * B[k] - T * (B[k] + x)
        else:
            return -T * x

B = list(map(lambda i: A[i+1] - A[i], range(N)))
ans = []
for _ in range(Q):
    l, r, x = [int(x) for x in input().split()]
    C += add(l - 1, x)
    B[l - 1] += x

    if r < N:
        C += add(r, -x)
        B[r] -= x

    ans.append(C)

print('\n'.join(str(a) for a in ans))