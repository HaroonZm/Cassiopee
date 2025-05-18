N = int(input())
S = input()
T = input()
for x in range(N, 2 * N + 1):
    if S[x - N:] == T[:2 * N - x]:
        print(x)
        exit()