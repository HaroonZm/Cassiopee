import sys
input = sys.stdin.readline

for _ in range(20000):
    M, G, Ge, D, Gr, O = map(int, input().split())
    if M+G+Ge+D+Gr+O == 0:
        break
    # Contest types:
    # 1) Math + DP (M+D) >=3 problems per contest
    # 2) Greedy + Graph (G+Gr) >=3
    # 3) Geometry + Other (Ge+O) >=3
    # 4) Balanced: one from (M or D), one from (G or Gr), one from (Ge or O)
    # Must assign disjoint problems to each contest

    # We want to maximize total contests held.
    # Variables:
    # x1 = number of math contests (M+D)/3
    # x2 = number of algo contests (G+Gr)/3
    # x3 = number of impl contests (Ge+O)/3
    # x4 = number of balanced contests
    #
    # Constraints:
    # M+D used in x1 and x4: 3*x1 + x4 <= M+D
    # G+Gr used in x2 and x4: 3*x2 + x4 <= G+Gr
    # Ge+O used in x3 and x4: 3*x3 + x4 <= Ge+O
    #
    # x1,x2,x3,x4 >=0 integers
    #
    # Maximize x1+x2+x3+x4

    MD = M+D
    GG = G+Gr
    GO = Ge+O

    # Iterate over possible x4 values and pick max total
    # x4 can be at most min(MD,GG,GO)
    limit = min(MD, GG, GO)
    ans = 0
    for x4 in range(limit+1):
        x1 = (MD - x4)//3
        x2 = (GG - x4)//3
        x3 = (GO - x4)//3
        total = x1 + x2 + x3 + x4
        if total > ans:
            ans = total
    print(ans)