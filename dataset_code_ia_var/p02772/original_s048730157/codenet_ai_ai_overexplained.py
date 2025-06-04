# Demande à l'utilisateur de saisir un nombre entier.
# La fonction input() permet de lire un texte écrit par l'utilisateur.
# int() convertit ce texte en un nombre entier.
N = int(input())

# Demande à l'utilisateur de saisir une liste de nombres entiers séparés par des espaces.
# input() lit la ligne entière que l'utilisateur a tapée.
# split() sépare cette ligne en plusieurs sous-chaînes en utilisant les espaces comme séparateur par défaut.
# map(int, ...) applique la fonction int() à chaque sous-chaîne pour la convertir en entier.
# Le résultat est un itérable contenant tous les entiers saisis.
A = map(int, input().split())

# Initialise une variable compteur à zéro.
# Ce compteur va servir à compter combien de nombres remplissent certaines conditions.
cnt = 0

# La boucle for permet d'itérer (parcourir) chacun des éléments de l'itérable A.
# À chaque itération, la variable a prend la valeur d'un des éléments de A.
for a in A:
    # On teste si le nombre actuel (a) est un nombre pair.
    # Un nombre est pair lorsqu'il est divisible par 2, c'est-à-dire que le reste de la division (modulo) par 2 est nul.
    if a % 2 == 0:
        # Si le nombre est pair, on vérifie s'il est aussi divisible par 3.
        # a % 3 == 0 signifie que le nombre est un multiple de 3.
        if a % 3 == 0:
            # Si le nombre est pair et divisible par 3, on incrémente le compteur de 1.
            cnt += 1
        # Si le nombre pair n'est pas divisible par 3, on vérifie s'il est divisible par 5.
        # a % 5 == 0 signifie que le nombre est un multiple de 5.
        elif a % 5 == 0:
            # Si le nombre est pair et divisible par 5, on incrémente le compteur de 1.
            cnt += 1
    else:
        # Si le nombre n'est pas pair, c'est-à-dire s'il est impair,
        # dans ce cas, on incrémente aussi le compteur de 1.
        cnt += 1

# À la fin de la boucle, on effectue un test conditionnel pour afficher un résultat.
# Si le nombre total d'éléments (N) est égal au compteur (cnt),
# cela signifie que tous les nombres respectent les conditions.
# L'expression 'APPROVED' if N == cnt else 'DENIED' utilise le ternaire (opérateur conditionnel),
# qui renvoie 'APPROVED' si la condition est vraie, sinon 'DENIED'.
print('APPROVED' if N == cnt else 'DENIED')