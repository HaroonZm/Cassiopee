n, m = input().split()
n = int(n)
m = int(m)

# Création d'une grille avec des zéros
t = []
for i in range(n+2):
    ligne = []
    for j in range(n+2):
        ligne.append(0)
    t.append(ligne)

# Lecture et application des opérations
for i in range(m):
    a, b, x = input().split()
    a = int(a) - 1
    b = int(b) - 1
    x = int(x)
    t[a][b] += 1
    t[a][b+1] -= 1
    t[a+x+1][b] -= 1
    t[a+x+1][b+x+2] += 1
    t[a+x+2][b+1] += 1
    t[a+x+2][b+x+2] -= 1

# Propagation horizontale
for i in range(n+2):
    for j in range(1, n+2):
        t[i][j] = t[i][j] + t[i][j-1]

# Propagation verticale
for i in range(n+2):
    for j in range(1, n+2):
        t[j][i] = t[j][i] + t[j-1][i]

# Propagation diagonale
for i in range(1, n+2):
    for j in range(1, n+2):
        t[i][j] = t[i][j] + t[i-1][j-1]

# Compter les cases utilisées
ans = 0
for i in range(n):
    for j in range(i+1):
        if t[i][j] != 0:
            ans = ans + 1

print(ans)