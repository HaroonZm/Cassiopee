# Demande à l'utilisateur de saisir une valeur entière qui sera affectée à la variable n
n = int(input())  # 'n' représente le nombre de pièces lancées

# Demande à l'utilisateur de saisir n probabilités séparées par des espaces
# La fonction 'input()' récupère la chaîne de caractères saisie, puis 'split()' la découpe en une liste de chaînes
# 'map(float, ...)' convertit chaque chaîne en nombre à virgule flottante
# 'list(...)' encapsule tout pour transformer l'objet map en liste réelle nommée 'p'
p = list(map(float, input().split()))

# Création d'une structure de programmation dynamique (DP) de taille n x (n+1)
# 'dp[i][d]' représentera la probabilité d'obtenir exactement d faces aux pièces parmi les premières i+1 pièces
# dp est donc une liste de listes, initialisée à zéro partout
dp = [[0] * (n + 1) for _ in range(n)]

# Les faces des pièces sont représentées par 0 (pile/裏) ou 1 (face/表)
# Le cas de base : pour la première pièce (indice 0)
# La probabilité qu'il y ait 0 face parmi 1 pièce est la probabilité que la première pièce tombe sur pile : 1-p[0]
dp[0][0] = 1 - p[0]
# La probabilité qu'il y ait 1 face parmi 1 pièce est la probabilité que la première pièce tombe sur face : p[0]
dp[0][1] = p[0]
# Autres valeurs du premier lancer (par exemple, plus de 1 face dans 1 pièce) restent nulles

# Remplissage du tableau dp pour le reste des pièces (à partir de la deuxième pièce)
# On parcourt les pièces à partir de la pièce d'indice 1 (c'est-à-dire la deuxième) jusqu'à la dernière (indice n-1)
for i in range(1, n):
    # Pour chaque nombre possible de faces (d), c'est-à-dire de 0 jusqu'à i+1, inclus (car pour i pièces, on peut avoir au maximum i+1 faces)
    # range(i+2) car le maximum de faces sur (i+1) pièces est (i+1)
    for d in range(i + 2):
        # On calcule dp[i][d] comme la somme de deux cas exclusifs :
        # 1. Obtenir 'd' faces lorsque la i-ème pièce tombe pile : (1 - p[i]) * dp[i-1][d]
        #    - (1 - p[i]) est la probabilité que la (i+1)-ème pièce tombe pile
        #    - dp[i-1][d] est la probabilité d'obtenir déjà 'd' faces sur les i premières pièces
        # 2. Obtenir 'd' faces lorsque la i-ème pièce tombe face : p[i] * dp[i-1][d-1]
        #    - p[i] est la probabilité que la (i+1)-ème pièce tombe face
        #    - dp[i-1][d-1] est la probabilité d'avoir eu 'd-1' faces sur les i premières pièces, ce qui, ajouté à une face supplémentaire, donne 'd'
        #    - Pour d=0, dp[i-1][-1] ne doit pas être considéré (cela donnerait une indexation invalide); mais en multipliant par p[i] nul ou en initialisant dp à zéro, ça va
        dp[i][d] = p[i] * dp[i - 1][d - 1] + (1 - p[i]) * dp[i - 1][d]

# À l'issue des boucles, dp[n-1][d] contient la probabilité d'obtenir exactement d faces sur n lancers

# Calcul de la somme des probabilités d'obtenir strictement plus de la moitié de faces (majorité de faces)
# n//2 est la partie entière de la moitié de n (par exemple, si n=3, n//2=1, donc plus de la moitié c'est au moins 2)
# On somme dp[n-1][d] pour d allant de (n//2)+1 jusqu'à n inclus
ans = sum(dp[n - 1][n // 2 + 1:])

# Affiche le résultat final (la probabilité d'obtenir une majorité de faces)
print(ans)