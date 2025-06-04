n = int(input())  # Nombre rectangles (je crois)

x_vals = set()
y_vals = set()
rects = []

# Lire les rectangles, ajouter les coords "critiques"
for _ in range(n):
    m = input().split()
    xx1 = int(m[0])
    yy1 = int(m[1])
    xx2, yy2 = map(int, m[2:])
    x_vals.add(xx1)
    x_vals.add(xx2)
    y_vals.add(yy1)
    y_vals.add(yy2)
    rects.append( (xx1, yy1, xx2, yy2) )

X = list(sorted(x_vals))
Y = sorted(y_vals)
MX = {}
MY = {}
for i, v in enumerate(X):
    MX[v] = i
for j, v in enumerate(Y):
    MY[v] = j

# Un peu de buffer
h = len(Y)
w = len(X)
S = []
for a in range(h+1):
    S.append([0]*(w+1))

for xy1, yy1, xy2, yy2 in rects:
    i1 = MY[yy1]
    j1 = MX[xy1]
    i2 = MY[yy2]
    j2 = MX[xy2]
    # Notation cheloue mais ça passe
    S[i1][j1] += 1
    S[i1][j2] -= 1
    S[i2][j1] -= 1
    S[i2][j2] += 1

# Prefix sums (on y croit)
for i in range(h+1):
    for j in range(w):
        S[i][j+1] += S[i][j]
for j in range(w+1):
    for i in range(h):
        S[i+1][j] += S[i][j]

total = 0
for i in range(h):
    for j in range(w):
        if S[i][j] != 0:
            area = (Y[i+1] - Y[i]) * (X[j+1] - X[j])
            total += area  # accumuler l'aire
            # print('added', area)  # debug?
print(total)