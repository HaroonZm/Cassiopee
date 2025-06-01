# Demande à l'utilisateur d'entrer un nombre et le stocke dans la variable n
n = input()

# Crée une liste l contenant n+1 éléments initialisés à 0
# Ceci est utilisé pour stocker les scores de chaque joueur, indexés de 1 à n
l = [0] * (n + 1)

# La boucle suivante va s'exécuter un certain nombre de fois correspondant au nombre de matchs joués
# Le nombre de matchs est donné par la formule n*(n-1)/2, ce qui correspond au nombre de paires uniques entre n joueurs
# Par exemple, si n=4, il y aura 6 matchs (entre joueurs 1-2, 1-3, 1-4, 2-3, 2-4, 3-4)
for i in range(n * (n - 1) / 2):
    # Lit une ligne de saisie utilisateur contenant quatre entiers séparés par des espaces
    # Ces quatre entiers représentent a, b, c, d
    # a et b sont les indices des deux joueurs qui ont joué un match
    # c et d sont les scores respectifs des joueurs a et b dans ce match
    a, b, c, d = map(int, raw_input().split())

    # Compare les scores c et d pour attribuer des points aux joueurs
    # Si c > d, alors le joueur a a gagné, donc on ajoute 3 points à son total
    if c > d:
        l[a] += 3

    # Si c < d, alors le joueur b a gagné, donc on ajoute 3 points à son total
    if c < d:
        l[b] += 3

    # Si c == d, cela signifie que le match s'est terminé par un match nul
    # Dans ce cas, les deux joueurs obtiennent 1 point chacun
    if c == d:
        l[a] += 1
        l[b] += 1

# Après le traitement de tous les résultats de matchs,
# on va calculer et afficher le rang de chaque joueur en fonction de son score
# On parcourt les indices de joueurs de 1 à n inclus
for i in range(1, n + 1):
    # Initialise la position du joueur i à 1
    # Cette variable x va représenter le rang du joueur i
    x = 1

    # Parcourt tous les joueurs de 1 à n pour comparer leurs scores
    for j in range(1, n + 1):
        # Compare le score du joueur i avec le score du joueur j
        # Si le score de i est inférieur à celui de j, cela signifie que j est mieux classé
        # On incrémente donc la position (rang) de i
        if l[i] < l[j]:
            x += 1

    # Affiche le rang final de chaque joueur i sur une ligne distincte
    print x