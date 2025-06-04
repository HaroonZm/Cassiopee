# Définition d'une constante nommée 'm' qui va servir de module dans les calculs pour éviter les dépassements d'entiers
m = 10**9 + 7  # 10 puissance 9 plus 7, un grand nombre premier souvent utilisé en algorithmie

# Définition d'une fonction lambda nommée 'f' qui prend un argument x
# Elle renvoie la valeur maximum entre x et 0 (c'est-à-dire, x si x > 0, sinon 0)
f = lambda x: max(x, 0)

# Assignation de l'identifiant 'r' à la fonction Python 'range'
# Ceci permet d'utiliser 'r' comme un alias pour 'range', qui crée une séquence de nombres entiers
r = range

# Démarrage d'une boucle principale
# Pour chaque cas de test, on demande un nombre entier de cas de test à traiter
for _ in r(int(input())):
    # Lecture de deux entiers à partir de l'entrée standard
    # - On split la ligne de saisie par défaut sur les espaces (séparation)
    # - On convertit chaque morceau en entier via map
    # - On utilise la fonction 'sorted' pour trier ces deux entiers par ordre croissant
    x, y = sorted(map(int, input().split()))
    
    # Initialisation de la variable 's' à la valeur -1
    # Cette variable est utilisée pour compter le nombre d'étapes dans une boucle ultérieure
    s = -1
    
    # Initialisation des variables 'i' et 'j' à 1
    # Ces variables correspondent aux termes d'une séquence particulière (proche de Fibonacci « retardé »)
    i = j = 1

    # Exécution d'une boucle 'while' tant que deux conditions sont vraies :
    # 1. j <= x
    # 2. i + j <= y
    while j <= x and i + j <= y:
        # À chaque itération :
        #   - on met i à la valeur de j
        #   - on met j à la somme de i et j (avant modification)
        #   - on incrémente s de 1
        i, j, s = j, i + j, s + 1

    # Condition : si x == 1 ou y < 3
    if x == 1 or y < 3:
        # Alors on affiche deux valeurs :
        #   - 1 : cela représente le nombre d'étapes (ou de solutions) trouvées dans ce cas
        #   - x*y%m : le produit de x et y modulo m
        print(1, x * y % m)
    else:
        # Calcul d'une valeur auxiliaire 'a' :
        # On additionne deux termes, chacun correspondant à un certain nombre de positions valides
        # 1. f((y-j)//i+1) : nombre d’indices où on peut placer un bloc horizontal
        # 2. f((x-j)//i+1) : nombre d’indices où on peut placer un bloc vertical
        # On utilise la fonction f pour éviter les nombres négatifs
        a = f((y - j) // i + 1) + f((x - j) // i + 1)

        # Réinitialisation des variables i et j à la valeur 1
        i = j = 1

        # Début d'une nouvelle boucle sur c allant de 0 à s-1
        # s est le nombre calculé lors de la boucle while précédente
        for c in r(s):
            # Calcul de deux nouvelles variables k et l :
            #   - k prend la valeur de j
            #   - l prend la valeur de i + 2*j (c'est-à-dire i + j*2)
            k, l = j, i + j * 2

            # Démarrage d'une boucle imbriquée, s-c itérations
            for _ in r(s - c):
                # À chaque itération :
                #   - k prend la valeur de l
                #   - l prend la valeur de la somme de l’ancienne k et l’ancienne l
                k, l = l, k + l

            # Condition : si x >= k
            if x >= k:
                # On incrémente a par f((y-l)//k+1)
                a += f((y - l) // k + 1)

            # Condition : si y >= k
            if y >= k:
                # On incrémente a par f((x-l)//k+1)
                a += f((x - l) // k + 1)

            # Mise à jour des variables i et j suivant la récurrence similaire à Fibonacci
            i, j = j, i + j

        # Enfin, on affiche :
        #   - s+1 : le nombre total d'étapes (correspondant à la profondeur calculée)
        #   - a%m : valeur a réduite modulo m
        print(s + 1, a % m)