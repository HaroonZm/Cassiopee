# Demande à l'utilisateur de saisir un nombre entier, stocké dans la variable 'n'
# Cela détermine la taille des listes que nous traiterons ensuite
n = int(input())

# Demande à l'utilisateur de saisir une ligne d'entiers séparés par des espaces
# input() reçoit la ligne sous forme de chaîne de caractères, par exemple "1 2 3"
# split() découpe la chaîne en liste de sous-chaînes ['1','2','3']
# map(int, ...) convertit chaque sous-chaîne en un entier
# list(...) convertit le résultat en une liste Python, assignée à la variable 'a1'
a1 = list(map(int, input().split()))

# Même logique que précédemment, cette fois pour la deuxième liste d'entiers : 'a2'
a2 = list(map(int, input().split()))

# Initialise une variable pour suivre la plus grande somme trouvée
# On commence à 0, supposant que toutes les sommes seront supérieures ou égales à zéro
max_sum = 0

# Boucle for qui itère la variable 'i' de 0 à n-1 inclus
# range(0,n) génère une séquence d'entiers [0, 1, ..., n-1]
for i in range(0, n):
    # Calcule la somme de deux parties :
    # Première partie : sum(a1[0:i+1])
    #   a1[0:i+1] crée une sous-liste de a1, contenant les éléments d'index 0 jusqu'à i inclus (découpage exclusif à l'indice de fin)
    #   sum(...) additionne tous ces éléments
    # Deuxième partie : sum(a2[i:n+1])
    #   a2[i:n+1] crée une sous-liste de a2, des éléments d'index i jusqu'à n inclus (découpage exclusif à n+1, donc inclut l'élément d'index n)
    #   sum(...) additionne ces éléments
    # On additionne les deux sommes pour obtenir 'x'
    x = sum(a1[0:i+1]) + sum(a2[i:n+1])
    
    # Compare la valeur actuelle de 'x' à la valeur la plus élevée trouvée jusqu'à présent ('max_sum')
    # Si 'x' est plus grand ou égal à 'max_sum', on met à jour 'max_sum' pour qu'il devienne 'x'
    if max_sum <= x:
        max_sum = x

# Affiche enfin la valeur finale de 'max_sum' sur la sortie standard (habituellement l'écran)
print(max_sum)