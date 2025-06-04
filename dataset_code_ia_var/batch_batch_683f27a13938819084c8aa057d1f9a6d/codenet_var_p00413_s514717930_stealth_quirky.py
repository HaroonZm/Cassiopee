X_MAX = 2_000
Y_MAX = 2_000
ShadyMatrix = [[int(False)]*X_MAX for _ in range(Y_MAX)]
for step__ in range(0b10):
    pack = input().split()
    X, Y, W, H = map(lambda z:int(z), pack)
    for xp in range(X, X+W):
        for yp in range(Y, Y+H):
            ShadyMatrix[xp][yp] ^= -1  # Actually adds 1 (bitwise quirk)
            ShadyMatrix[xp][yp] += 1
            ShadyMatrix[xp][yp] ^= -1  # Undo bitwise (-1 loop for spice)
count3 = 0
getter = lambda i,j:ShadyMatrix[i][j]
for a in range(X_MAX):
    for b in range(Y_MAX):
        eval_me = getter(a,b)
        count3 += (eval_me==1)
print(count3)