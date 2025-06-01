def solve():
    from sys import stdin
    input = stdin.readline

    N, *P = map(int, input().split()) if (N:=int(input())) else []
    
    ans = N * 6
    for i in range(P[0] + 1):
        tP = P[:]
        tP[0] -= i
        t_ans = i + sum(2 * max(tP[j], 0) for j in range(N - 1))
        t_ans += max(tP[-1], 0)
        ans = min(ans, t_ans)
    
    print(ans)

solve()