# Demande à l'utilisateur d'entrer deux entiers séparés par un espace : n et t
# map() applique int à chaque partie obtenue par split() de l'entrée, pour convertir en entiers
# Les deux entiers sont ensuite assignés à n et t respectivement
n, t = map(int, input().split())

# Initialisation de trois variables à zéro :
# s : somme cumulative utilisée dans le calcul
# x : sert à stocker une valeur de h précédente (voir plus bas)
# y : garde en mémoire la valeur maximale rencontrée de h jusqu'à maintenant
s = 0  # somme cumulée pour les besoins du calcul
x = 0  # stocke la valeur précédente de h pour le prochain calcul de s
y = 0  # gardera la valeur maximale atteinte de h jusqu'à l'instant présent

# On boucle n fois, de 0 à n-1 (n étant le nombre d'itérations désirées)
for i in range(n):
    # Pour chaque itération, on demande à l'utilisateur d'entrer un entier h via input()
    # int() convertit la chaîne saisie en entier numérique
    h = int(input())

    # Mise à jour des variables multiples en une seule ligne :
    # s prend la valeur s + x (somme cumulée plus la valeur précédente de h)
    # x prend la valeur courante de h (utilisée lors du prochain tour de boucle)
    # y est mis à jour pour garder le maximum entre sa valeur actuelle et h (stocke le plus grand h vu jusque-là)
    # L'affectation multiple est lue de droite à gauche, i.e. la partie de droite s'évalue avant l'affectation
    s, x, y = s + x, h, max(h, y)

    # Calcul du résultat à afficher :
    # 1. (t - x - s) : on enlève x (dernier h lu) et s (somme cumulée) à t
    # 2. // y : division entière du résultat précédent par la plus grande valeur rencontrée de h jusqu'ici
    # 3. +2 : ajoute 2 au quotient pour aboutir à la valeur désirée
    # 4. max(val, 1) : garantit que l'on ne retourne jamais une valeur inférieure à 1 (jamais moins de 1)
    # print() affiche le résultat immédiatement à l'utilisateur
    print(
        max(
            # Calcul détaillé, étape par étape :
            ((t - x - s) // y) + 2,  # division entière (quotient) puis addition de 2
            1  # valeur minimale autorisée
        )
    )