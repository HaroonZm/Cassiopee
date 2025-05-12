def solve():
    from sys import stdin
    f_i = stdin
    
    N = int(f_i.readline())
    P = list(map(int, f_i.readline().split()))
    left = P[0]
    
    ans = N * 6
    for i in range(left + 1):
        tP = P[:]
        tP[0] -= i
        t_ans = i
        for j in range(N - 1):
            tpj = tP[j]
            if tpj > 0:
                tP[j + 1] -= tpj
                t_ans += 2 * tpj
        if tP[-1] > 0:
            t_ans += tP[-1]
        if t_ans < ans:
            ans = t_ans
    
    print(ans)

solve()