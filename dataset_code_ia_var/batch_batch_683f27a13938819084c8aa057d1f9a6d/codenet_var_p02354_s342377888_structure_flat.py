INF = 10**18

N_S = input().split()
N = int(N_S[0])
S = int(N_S[1])
A_input = input().split()
A = []
for i in range(N):
    A.append(int(A_input[i]))

res = INF
rt = 0
s = 0
lt = 0
while lt < N:
    while rt < N and s < S:
        s += A[rt]
        rt += 1
    if s >= S:
        if rt - lt < res:
            res = rt - lt
    s -= A[lt]
    lt += 1

if res != INF:
    print(res)
else:
    print(0)