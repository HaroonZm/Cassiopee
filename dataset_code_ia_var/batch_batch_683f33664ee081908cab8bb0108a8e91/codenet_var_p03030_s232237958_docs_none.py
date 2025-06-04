N = int(input())
R_L = []
for n in range(N):
    S, P = input().split()
    R_L.append([S, int(P)])

R_L2 = R_L.copy()
R_L2.sort(key=lambda x: (x[0], -x[1]))
for r in R_L2:
    print(R_L.index(r) + 1)