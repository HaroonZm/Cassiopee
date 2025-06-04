while True:
    M,G,E,D,R,O = map(int,input().split())
    if M==0 and G==0 and E==0 and D==0 and R==0 and O==0:
        break
    ans=0
    #Approach: try all possible numbers of balanced contests b,
    # and compute how many other contests can be formed with remaining problems.
    max_b = min(M+D,G+R,E+O)
    ans=0
    for b in range(max_b+1):
        m_rem = M + D - b
        g_rem = G + R - b
        e_rem = E + O - b
        # Number of math-only contests
        math_only = (m_rem)//3
        # Number of greedy-only contests
        greedy_only = (g_rem)//3
        # Number of geometry-only contests
        geometry_only = (e_rem)//3
        total = b + math_only + greedy_only + geometry_only
        if total > ans:
            ans = total
    print(ans)