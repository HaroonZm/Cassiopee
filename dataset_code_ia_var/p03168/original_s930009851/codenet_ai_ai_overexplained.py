# Demande à l'utilisateur d'entrer un entier via le clavier
n = int(input())

# Demande à l'utilisateur d'entrer une ligne de réels séparés par des espaces
# La ligne saisie (input()) est découpée en sous-chaînes par split()
# Chaque sous-chaîne (nombre sous forme de texte) est convertie en float avec map(float, ...)
# Le résultat est transformé en liste avec list()
v = list(map(float, input().split()))

# Création d'une liste dp qui va contenir n sous-listes, une pour chaque élément de v
# Chaque sous-liste contient (len(v) + 1) flottants initialisés à 0.0 (ce sont les zéros initiaux)
# Utilisation d'une compréhension de liste pour faire cela en une ligne
dp = [[0.0] * (len(v) + 1) for i in range(len(v))]

# Boucle externe de 0 à n-1 incluse (range(n) produit n entiers séquentiels)
for x in range(n):
    # Boucle interne de 0 à x+1 inclus (range(x+2) va de 0 à x + 1)
    for a in range(x + 2):

        # Premier cas : on est sur le tout premier élément (x == 0 ET a == 0)
        if x == 0 and a == 0:
            # On attribue à dp[0][0] la valeur v[0] (le premier élément de la liste v)
            dp[x][a] = v[x]

        # Deuxième cas : toujours le premier élément mais a == 1 (donc colonne 1)
        # Il faut aussi que n ne soit pas égal à 1 (au moins deux éléments)
        elif x == 0 and a == 1 and n != 1:
            # On assigne à dp[0][1] la valeur 1 - v[0]
            dp[x][a] = 1 - v[x]

        # Troisième cas : l'indice de colonne (a) est supérieur à la moitié de n
        elif a > n / 2:
            # On multiplie la valeur précédente de la même colonne, dp[x-1][a], par v[x]
            # Cela met à jour la case dp[x][a]
            dp[x][a] = dp[x-1][a] * v[x]

        # Cas général, pour tous les autres cas non captés par les conditions précédentes
        else:
            # On additionne deux contributions :
            # 1) dp[x-1][a] * v[x] : scénario où on ne sélectionne pas l'élément courant
            # 2) dp[x-1][a-1] * (1 - v[x]) : scénario où on sélectionne l'élément courant (remarquez le a-1)
            # On additionne les deux et on affecte à dp[x][a]
            dp[x][a] = dp[x-1][a] * v[x] + dp[x-1][a-1] * (1 - v[x])

# La ligne suivante importerait la bibliothèque numpy, utile pour afficher sous forme de matrice,
# mais elle est actuellement commentée (ne s'exécute pas)
# import numpy
# print(numpy.matrix(dp))

# À la fin, on affiche la somme des valeurs de la dernière ligne du tableau dp (ligne d'indice n-1)
# Cela retourne une seule valeur, résultat final du calcul
print(sum(dp[n-1]))