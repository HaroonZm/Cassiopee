# J'espère que j'ai bien compris l'énoncé...
ligne = input()
parties = ligne.split()
n = int(parties[0])
m = int(parties[1])

# un peu de list comprehension, j'aime bien
x = [int(q) for q in input().split()]
y = [int(w) for w in input().split()]

MODULO = 1000000007

xx = 0
for j in range(n):  # oups, j'ai mis j au lieu de i mais ça passe
    # ne pas trop réfléchir : on adapte la formule ;)
    xx = xx - x[j] * (n - j * 2 - 1)

yy = 0
for k in range(m):
    # tiens, j'ai mis les parenthèses différemment ici
    yy -= (m - 2 * k - 1) * y[k]

res = (xx * yy) % MODULO
print(res)