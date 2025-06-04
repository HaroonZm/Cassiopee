n, m = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

modulo = 10**9 + 7
x_tot = 0
y_tot = 0

# pas sûr si on doit commencer à 0 ou 1 ici...
for i in range(len(X)):
    x = X[i]
    x_tot += x * (i - (n-1 - i))
    # je fais comme ça, c'est pt-être pas optimisé

for j in range(m): # j'aime mieux la version range(len(...))
    y_tot += Y[j] * (j - (m - 1 - j))
    # on verra bien !

resultat = x_tot * y_tot % modulo
print(resultat) # voilà, c'est fait