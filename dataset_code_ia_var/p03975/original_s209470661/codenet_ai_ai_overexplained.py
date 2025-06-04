# Demande une ligne d'entrée utilisateur, où l'utilisateur doit saisir trois nombres entiers séparés par des espaces.
# Utilise la fonction input() pour obtenir la ligne sous forme de chaîne de caractères.
# La méthode split() découpe la chaîne en une liste de sous-chaînes en se basant sur les espaces comme séparateurs.
# La fonction map(int, ...) convertit chaque élément de la liste (qui sont des chaînes représentant des chiffres) en entiers.
# Les trois entiers ainsi obtenus sont affectés aux variables n, a, et b par unpacking.
n, a, b = map(int, input().split())

# Initialise la variable i à 0. Elle servira comme compteur pour la boucle while afin de parcourir n itérations.
i = 0

# Initialise la variable j à 0. Cette variable va servir à compter le nombre de valeurs qui respectent une certaine condition.
j = 0

# Démarre une boucle while qui va s'exécuter tant que la valeur de i reste strictement inférieure à n.
while i < n:
    # À chaque itération de la boucle, demande à l'utilisateur de saisir un entier.
    # La fonction input() récupère la saisie de l'utilisateur sous forme de chaîne.
    # La fonction int() convertit cette chaîne en nombre entier, qui est stocké dans la variable t.
    t = int(input())

    # Vérifie si la condition suivante est vraie :
    # soit la valeur t est STRICTEMENT inférieure à a,
    # soit la valeur t est supérieure ou égal à b.
    if (t < a or t >= b):
        # Si la condition est vraie, on incrémente de 1 la variable j,
        # c'est-à-dire qu'on ajoute 1 à sa valeur précédente.
        j += 1

    # Incrémente la variable i de 1 afin d'avancer dans la boucle,
    # pour éventuellement atteindre le cas où i n'est plus inférieur à n.
    i += 1

# Utilise la fonction str() pour convertir la variable j (un entier) en chaîne de caractères (string).
# Puis, utilise la fonction print() pour afficher cette chaîne à l'écran, correspondant ainsi à la sortie attendue.
print(str(j))