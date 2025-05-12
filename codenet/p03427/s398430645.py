N = input()
K = len(N)
if N[0] + "9" * (K - 1) == N:
    print(int(N[0]) + 9 * (K - 1))
else:
    print(int(N[0]) - 1 + 9 * (K - 1))