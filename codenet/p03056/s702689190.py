H, W = map(int, input().split())
A = [[1 if a == "#" else 0 for a in input()] for _ in range(H)]
X = [[[-2] * (H + 2) for _ in range(W + 2)] for _ in range(H + 2)]
Y = [[[-2] * (W + 2) for _ in range(W + 2)] for _ in range(H + 2)]

for i in range(H):
    for j in range(W):
        X[i][j][i] = j
        Y[i][j][j] = i
for i in range(H):
    for j in range(W-1)[::-1]:
        if A[i][j] == A[i][j+1]:
            X[i][j][i] = X[i][j+1][i]
for i in range(H-1)[::-1]:
    for j in range(W):
        if A[i][j] == A[i+1][j]:
            Y[i][j][j] = Y[i+1][j][j]

for i in range(H):
    for j in range(W):
        for ii in range(i+1, H):
            if A[ii][j] != A[i][j]:
                break
            X[i][j][ii] = min(X[i][j][ii-1], X[ii][j][ii])
for i in range(H):
    for j in range(W):
        for jj in range(j+1, W):
            if A[i][jj] != A[i][j]:
                break
            Y[i][j][jj] = min(Y[i][j][jj-1], Y[i][jj][jj])

for k in range(16):
    if X[0][0][H-1] == W-1:
        print(k)
        break
    elif k == 15:
        print(16)
        break
    for i in range(H):
        Xi = X[i]
        Yi = Y[i]
        for j in range(W):
            Xij = Xi[j]
            Yij = Yi[j]
            for ii in range(i, H):
                Xijii = Xij[ii]
                if Xijii >= 0 and X[i][Xijii + 1][ii] >= 0:
                    Xij[ii] = X[i][Xijii + 1][ii]
            for jj in range(j, W):
                Yijjj = Yij[jj]
                if Yijjj >= 0 and Y[Yijjj + 1][j][jj] >= 0:
                    Yij[jj] = Y[Yijjj + 1][j][jj]
            
            jj = W - 1
            for ii in range(i, H):
                while jj >= j and Yij[jj] < ii:
                    jj -= 1
                if jj >= j:
                    Xij[ii] = max(Xij[ii], jj)
            
            ii = H - 1
            for jj in range(j, W):
                while ii >= i and Xij[ii] < jj:
                    ii -= 1
                if ii >= i:
                    Yij[jj] = max(Yij[jj], ii)