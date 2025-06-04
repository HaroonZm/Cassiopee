# Importation du module math pour accéder à des fonctions mathématiques avancées, comme la racine carrée
import math

# Boucle infinie afin de traiter plusieurs entrées utilisateur successives
while True:
    # Demander à l'utilisateur d'entrer une valeur et convertir cette valeur saisie (de type chaîne de caractères) en entier
    b = int(input())
    # Vérifier si la valeur de b est égale à 0
    # Si oui, cela indique que l'utilisateur veut arrêter le programme, donc on sort de la boucle avec le mot clé 'break'
    if b == 0:
        break

    # Calcul du nombre maximal de termes k_max pouvant former une somme consécutive égale à b
    # On résout l'inégalité k(k+1)/2 <= b, qui peut être transformée en k^2 + k - 2b <= 0
    # La solution de cette équation quadratique est k = (-1 + sqrt(1 + 8b)) / 2
    # int() tronque la partie décimale pour obtenir la plus grande valeur entière inférieure ou égale au résultat
    k_max = int(((-1 + math.sqrt(1 + 8 * b)) / 2))

    # On parcourt les valeurs possible de k, du plus grand (k_max) jusqu'à 1 inclus (0 exclu), décrémentant de 1 à chaque itération
    for k in range(k_max, 0, -1):
        # Vérification des deux conditions suivantes pour que b puisse être écrit comme la somme de k entiers consécutifs :
        # 1. Il existe un entier n tel que la somme n + (n+1) + ... + (n+k-1) soit égale à b
        # Ce qui revient à vérifier si 2*b est divisible par k (première condition)
        # 2. (2*b / k + 1 - k) doit être un nombre pair pour que n soit un entier
        if 2 * b % k == 0 and (2 * b / k + 1 - k) % 2 == 0:
            # Calcul de la valeur de départ n telle que la somme de k nombres consécutifs à partir de n donne b
            # n = ((2*b / k) + 1 - k) / 2
            # On convertit le résultat final en entier car n doit être un entier
            n = int((2 * b / k + 1 - k) / 2)
            # Affichage des valeurs trouvées n et k, séparées par un espace
            # .format() est une méthode de formatage de chaîne de caractères permettant d'insérer des valeurs dans une chaîne
            print("{} {}".format(n, k))
            # Une fois qu'une telle paire (n, k) a été trouvée et affichée, on sort de la boucle for en utilisant 'break'
            break