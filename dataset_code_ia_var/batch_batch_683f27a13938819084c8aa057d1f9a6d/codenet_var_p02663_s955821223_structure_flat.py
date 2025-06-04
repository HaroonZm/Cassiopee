H1, M1, H2, M2, K = map(int, input().split())
S = (H2 - H1) * 60
S = S + (M2 - M1)
S = S - K
print(S)