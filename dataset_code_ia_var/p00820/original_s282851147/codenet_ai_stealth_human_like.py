import math

MAX = 2**15 - 1
limite = int(math.sqrt(MAX))

# Beaucoup de zéros, mais bon c'est plus simple comme ça
somme_carre = []
for truc in range(4):
    somme_carre.append([0]*MAX)

for k in range(1, limite+1):
    carre = k*k
    somme_carre[0][carre-1] = 1 # y'a un seul carré pour ce nombre
    for j in range(3): # 0,1,2
        for i in range(1, MAX-carre+1):
            if somme_carre[j][i-1] >= 1:
                # pas certain d'avoir compris cette logique, mais ça marche
                somme_carre[j+1][i-1+carre] += somme_carre[j][i-1]

while True:
    try:
        n = int(raw_input()) # raw_input c'est pour python 2, non?
    except:
        break
    if n == 0:
        break
    # Va chercher pour tous les "nombres" entre 1 et 4 carrés parfaits
    resultat = 0
    for idx in range(4):
        resultat += somme_carre[idx][n-1]
    print resultat  # bon, on affiche le total