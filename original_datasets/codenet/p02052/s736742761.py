# from sys import exit
H, W = [int(n) for n in input().split()]
c = [[0 for _ in range(W)] for __ in range(H)]
Bs = []

for i in range(H):
    c[i] = list(str(input()))
    for j in range(W):
        if c[i][j] == "B":
            Bs.append((i, j))

ans = 0
for e0 in Bs:
    for e1 in Bs:
        ans = max(ans, abs(e0[0] - e1[0]) + abs(e0[1] - e1[1]))
print(ans)