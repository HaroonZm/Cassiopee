N = int(input())
S = list(input())
R = []
G = []
B = []
cnt = 0

for i in range(N):
    if S[i] == "R":
        R.append(i)
    elif S[i] == "G":
        G.append(i)
    else:
        B.append(i)

B = set(B)
b = len(B)

for i in R:
    for j in G:
        check = 0
        m = min(i, j)
        M = max(i, j)
        r = M - m
        left = m - r
        right = M + r
        if r % 2 == 0:
            center = m + r // 2
            if center in B:
                check += 1
        if left in B:
            check += 1
        if right in B:
            check += 1
        cnt += b - check

print(cnt)