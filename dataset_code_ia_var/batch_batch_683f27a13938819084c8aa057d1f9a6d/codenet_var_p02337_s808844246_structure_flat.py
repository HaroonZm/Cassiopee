n, k = map(int, input().split())
MOD = 10 ** 9 + 7
ball = n
box = k
S = []
for i in range(ball + 1):
    S.append([0] * (box + 1))
S[0][0] = 1
i = 0
while i < ball:
    j = 0
    while j < box:
        S[i + 1][j + 1] = S[i][j] + S[i][j + 1] * (j + 1)
        S[i + 1][j + 1] %= MOD
        j += 1
    i += 1
B_ij = 0
index = 0
while index <= box:
    B_ij += S[ball][index]
    B_ij %= MOD
    index += 1
print(B_ij)