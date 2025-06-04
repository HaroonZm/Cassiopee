# On commence par lire deux entiers depuis l'entrée standard (par exemple, la console)
# input() lit une ligne de texte, .split() la sépare en éléments avec l'espace comme séparateur
# map(int, ...) applique int() sur chaque élément de la liste obtenue, convertissant ainsi les chaînes en entiers
# Enfin, avec l'opérateur d'affectation multiple, n reçoit la première valeur, et k la seconde
n, k = map(int, input().split())

# On lit la deuxième ligne contenant n entiers qui seront nos "quantités par type"
# On applique la même logique pour convertir chaque élément de la ligne en int puis les stocker dans une liste nommée a
a = list(map(int, input().split()))

# On crée une liste appelée dp (pour "programmation dynamique") de taille k+1 initialisée avec des zéros
# Cela crée une liste où l'élément d'indice i représentera le nombre de façons d'obtenir la somme i
dp = [0] * (k + 1)

# On définit une variable 'mod' qui sert à faire un modulo lors des calculs pour éviter de trop grands nombres
# 10**9+7 est une grande valeur première souvent utilisée en programmation compétitive
mod = 10**9 + 7

# On initialise les valeurs de dp pour le premier type d'objet (premier élément de la liste a)
# Pour chaque quantité possible de 0 à a[0] pour ce type (inclus, donc range utilise a[0]+1)
for i in range(0, a[0] + 1):
    # Il existe exactement une façon de composer une somme i avec uniquement le premier type d'objet, c'est en prenant i objets
    dp[i] = 1

# On traite maintenant les autres types d'objets, en commençant par le deuxième (indice 1)
# La boucle externe parcourt les types d'objets à partir du deuxième jusqu'au dernier (indices 1 à n-1)
for i in range(1, len(a)):
    # Première sous-boucle : on met à jour dp[] pour prendre en compte les possibilités cumulatives jusqu'à l'indice courant
    # Cela permet d'accélérer le calcul de la somme sur les intervalles
    # La boucle va de j=1 jusqu'à k inclus car l'indice 0 ne change pas ici
    for j in range(1, k + 1):
        # On additionne dp[j-1] à dp[j], chaque combinaison de somme j peut se faire en rajoutant un objet de ce type à une somme précédente j-1
        dp[j] = (dp[j] + dp[j - 1]) % mod

    # Deuxième sous-boucle : on 'corrige' les cas où on aurait pris trop d'objets de ce type (plus que a[i])
    # Pour cela, on retranche certaines contributions précédemment ajoutées qui concernent dépasser la quantité autorisée
    # On parcourt à l'envers pour ne pas interférer avec les valeurs encore utilisées pour des calculs
    # Pour chaque somme j allant de k jusqu'à a[i]+1 inclus (donc supérieure à la quantité autorisée), on ajuste dp[j]
    for j in range(k, a[i], -1):
        # On retire dp[j-a[i]-1] de dp[j] car cela représente les moyens qui dépassaient le stock autorisé pour ce type
        # On ajoute mod pour éviter des résultats négatifs à cause du modulo
        dp[j] = (dp[j] - dp[j - a[i] - 1] + mod) % mod

# À la fin, dp[k] contient le nombre total de façons de composer la somme k avec les quantités d'objets spécifiées
# On l'affiche à l'aide de print()
print(dp[k])