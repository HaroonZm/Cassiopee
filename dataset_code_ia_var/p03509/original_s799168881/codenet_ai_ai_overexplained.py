# Lecture de deux entiers depuis l'entrée standard.
# input() permet à l'utilisateur de saisir une ligne au clavier.
# split() sépare la chaîne obtenue en une liste d'éléments, ici supposés séparés par des espaces.
# map(int, ...) convertit chaque élément (au départ sous forme de chaîne de caractères) en un entier (int).
# Enfin, on affecte le premier entier à N et le deuxième à P.
N, P = map(int, input().split())

# Initialisation de la variable B à 0.
# Cette variable va servir à accumuler les valeurs b lues à chaque itération dans la boucle suivante (somme totale des b).
B = 0

# Initialisation de Q comme une liste vide.
# Q sera utilisée pour stocker des valeurs calculées à partir de w et b à chaque itération.
Q = []

# La boucle for suivante permet de faire N itérations, correspondant au nombre total d'objets, d'éléments ou de lignes à traiter.
for i in range(N):
    # Lecture de deux entiers w et b pour chaque itération, à partir de l'entrée standard, selon le même principe que l'étape précédente.
    w, b = map(int, input().split())

    # On ajoute la valeur de b à B, effectuant ainsi une somme cumulative de tous les b lus jusqu'à présent.
    B += b

    # Calcul d'une expression impliquant w, b, P et des constantes.
    # (100 - P) est multiplié par w, P est multiplié par b, ensuite ces deux résultats sont additionnés.
    # Le tout est ajouté à la liste Q à l'aide de la méthode append.
    Q.append((100 - P) * w + P * b)

# La méthode sort() permet d'ordonner la liste Q par ordre croissant (de la plus petite à la plus grande valeur).
Q.sort()

# Initialisation d'une variable s à 0.
# La variable s servira à accumuler la somme de certains éléments de Q lors de la boucle suivante.
s = 0

# Nouvelle boucle for exécutée N fois, permettant de parcourir les indices de 0 jusqu'à N-1.
for i in range(N):
    # La notation Q[-i-1] permet d'accéder aux éléments de Q en partant de la fin de la liste.
    # Q[-1] est le dernier élément (le plus grand après le tri), Q[-2] l'avant-dernier, etc.
    # On additionne l'élément courant à la variable s, effectuant ainsi une somme cumulative des plus grandes valeurs de Q.
    s += Q[-i-1]

    # On évalue une condition :
    # Si le produit de B (somme totale des b précédemment obtenus) et de P (entier d'entrée) est inférieur ou égal à s,
    # alors on considère que l'on a atteint ou dépassé un seuil désiré.
    if B * P <= s:
        # On affiche la valeur i + 1 à l'écran à l'aide de print().
        # Cela correspond au nombre d'éléments sélectionnés jusque-là (par conventions des indices en Python commençant à 0, d'où le "+1").
        print(i + 1)
        # La commande break permet de sortir immédiatement de la boucle for dès que la condition précédente est vérifiée.
        break