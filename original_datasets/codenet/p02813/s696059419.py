import math
N = int(input())
p = [int(x) for x in input().split()]
q = [int(x) for x in input().split()]

P = 0
Q = 0
for i in range(N-1):
    cnt_p = 0
    cnt_q = 0
    for j in range(i+1, N):
        if p[i] > p[j]:
            cnt_p += 1
        if q[i] > q[j]:
            cnt_q += 1
    P += cnt_p*math.factorial(N-1-i)
    Q += cnt_q*math.factorial(N-1-i)
print(abs(P-Q))