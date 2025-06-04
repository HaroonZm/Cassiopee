# Prendre trois entiers en entrée séparés par des espaces : a, n, m
# La fonction input() lit la ligne d'entrée depuis la console sous forme de texte (string)
# La méthode split() sépare cette chaîne de caractères en une liste de sous-chaines en coupant sur chaque espace
# La fonction map(int, ...) applique la conversion en entier à chaque élément de la liste produite par split()
# Les trois entiers sont ensuite attribués respectivement aux variables a, n et m
a, n, m = map(int, input().split())

# Création d'une liste vide appelée candi qui va contenir certains nombres candidats (à déterminer dans la boucle suivante)
candi = []

# Initialisation d'un compteur à zéro, la variable ans comptera la quantité de solutions valides trouvées
ans = 0

# On commence une boucle for avec la variable i, 
# i va prendre successivement toutes les valeurs de a+1 (inclus) jusqu'à 9*8+a+1 (exclus donc s'arrête à 9*8+a, ce qui fait 72+a)
for i in range(a + 1, 9 * 8 + a + 1):
    # Pour chaque valeur de i, on élève i à la puissance n (i**n)
    # Si la valeur trouvée est inférieure ou égale à m, alors on l'ajoute à la liste candi
    if i ** n <= m:
        # Ajout de i**n à la liste des candidats
        candi.append(i ** n)

# On parcourt ensuite tous les éléments (appelés j) de la liste candi précédemment construite
for j in candi:
    # On met la valeur de j dans une variable k, qui sera modifiée pour extraire ses chiffres
    k = j

    # Création d'une nouvelle liste vide, digit, pour mémoriser les chiffres individuels de j
    digit = []

    # On répète 9 fois l'extraction d'un chiffre (ce qui sélectionne les 9 derniers chiffres en base 10 de j, éventuellement complétés par des zéros à gauche)
    for _ in range(9):
        # On ajoute à la fin de la liste digit le chiffre des unités de k
        digit.append(k % 10)
        # On retire le chiffre des unités de k pour préparer la prochaine extraction
        k //= 10

    # On calcule la somme de tous les éléments de digit (soit la somme des 9 chiffres extraits de j)
    # On y ajoute la valeur de a, puis on élève le tout à la puissance n
    # Si ce résultat est exactement égal à j, alors la condition est satisfaite
    if (sum(digit) + a) ** n == j:
        # On incrémente le compteur des solutions trouvées (ans) de 1
        ans += 1

# On affiche le nombre total de solutions trouvées à l'écran
print(ans)