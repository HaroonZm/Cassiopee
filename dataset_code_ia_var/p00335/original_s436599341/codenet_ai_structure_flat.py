from sys import stdin
f_i = stdin

N = int(f_i.readline())
P = list(map(int, f_i.readline().split()))
left = P[0]

ans = N * 6
i = 0
while i <= left:
    tP = P[:]
    tP[0] -= i
    t_ans = i
    j = 0
    while j < N - 1:
        tpj = tP[j]
        if tpj > 0:
            tP[j + 1] -= tpj
            t_ans += 2 * tpj
        j += 1
    if tP[-1] > 0:
        t_ans += tP[-1]
    if t_ans < ans:
        ans = t_ans
    i += 1

print(ans)