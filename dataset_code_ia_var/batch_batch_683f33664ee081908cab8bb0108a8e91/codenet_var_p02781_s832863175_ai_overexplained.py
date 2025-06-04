import sys  # Le module sys fournit des fonctions et des variables utiles pour manipuler l'environnement d'exécution Python
import collections as cl  # collections est un module standard, ici abrégé 'cl', souvent utilisé pour des structures de données avancées
import bisect as bs  # bisect est un module pour gérer efficacement les tris et recherches dans les listes, ici abrégé 'bs'

# Augmente la limite de récursion pour autoriser des appels récursifs plus profonds que la limite standard (par défaut ~1000)
sys.setrecursionlimit(100000)

# Redéfinit la fonction d'entrée pour récupérer plus facilement des lignes depuis stdin (entrée standard)
input = sys.stdin.readline

# Définit une constante 'mod' à 10^9 + 7, communément utilisée comme modulateur dans des problèmes pour éviter les débordements d'entiers
mod = 10**9+7

# Définit 'Max' comme la plus grande valeur d'entier supportée par ce système (utilisée pour initialiser des bornes hautes)
Max = sys.maxsize

# Fonction qui retourne une liste d'entiers, après découpage de l'entrée sur les espaces
def l():
    # Prend une ligne d'entrée, la découpe sur les espaces, convertit chaque morceau en entier, et retourne la liste résultante
    return list(map(int, input().split()))

# Fonction qui retourne un map des entiers (permet d'accéder en itérateur directement)
def m():
    # Prend une ligne d'entrée, la découpe sur les espaces, convertit et retourne un itérateur d'entiers
    return map(int, input().split())

# Fonction qui lit et retourne directement un entier (utile pour lire les coordonnées ou longueurs)
def onem():
    # Prend une ligne d'entrée, la convertit en entier et la retourne
    return int(input())

# Fonction de "compression": compte et regroupe les valeurs consécutives dans une liste ou chaîne
def s(x):
    # Initialise une liste vide pour stocker le résultat compressé
    a = []
    # Prend le premier élément comme élément courant à compresser
    aa = x[0]
    # Initialise le compteur pour le nombre d'éléments consécutifs identiques
    su = 1
    # Parcourt la liste de l'index 0 à l'avant-dernier index
    for i in range(len(x)-1):
        # Vérifie si la valeur courante et la prochaine sont différentes
        if aa != x[i+1]:
            # Ajoute le couple (valeur, nombre de répétitions consécutives) au tableau des résultats
            a.append([aa, su])
            # Redéfinit l'élément courant (pour la prochaine série consécutive)
            aa = x[i+1]
            # Réinitialise le compteur
            su = 1
        else:
            # Si la même valeur se répète, augmente le compteur
            su += 1
    # Après la boucle, ajoute le dernier bloc compressé
    a.append([aa, su])
    # Retourne la liste des blocs compressés
    return a

# Fonction qui rassemble les éléments d'une liste en chaîne de caractères, séparées par un espace
def jo(x):
    # Utilise la fonction map pour convertir chaque élément de la liste en chaîne, puis les joint avec un espace entre eux
    return " ".join(map(str, x))

# Fonction pour trouver la plus grande valeur dans une liste de listes à deux dimensions
def max2(x):
    # Applique 'max' à chaque liste (trouve le maximum de chaque ligne) puis prend le maximum général
    return max(map(max, x))

# Fonction qui vérifie si 'x' est présent dans une liste 'a' supposée triée, en utilisant la recherche dichotomique
def In(x, a):
    # Cherche la première position où insérer x dans a pour maintenir l'ordre trié
    k = bs.bisect_left(a, x)
    # Si l'indice trouvé n'est pas hors limite et que l'élément à cet indice est bien 'x', alors il existe dans a
    if k != len(a) and a[k] == x:
        return True
    else:
        return False

"""
# Exemple de squelette pour une recherche binaire personnalisée, utilisé couramment pour chercher des valeurs ou bornes dans une plage
def nibu(x, n, r):
    ll = 0  # Borne basse de la plage recherchée
    rr = r  # Borne haute de la plage recherchée
    while True:
        mid = (ll + rr) // 2  # Calcule le point à tester (milieu)
        # Il manque ici la condition (par exemple, si ok(mid): rr = mid else: ll = mid + 1)
    if rr == mid:
        return ll
    if (ici mettre la condition de coupure):
        rr = mid
    else:
        ll = mid + 1
"""

# Lit un entier 'n' depuis l'entrée standard ; cela sert généralement de borne supérieure ou de quantité
n = onem()

# Lit un entier 'k', valeur de référence ou contrainte pour le problème
k = onem()

# Convertit l'entier 'n' en chaîne de caractères pour pouvoir accéder à chaque chiffre individuellement
s = str(n)

# Crée une table dp0 pour les cas "plus petits" que le préfixe de n, dimensions : [longueur de n + 1][4]
dp0 = [[0 for j in range(4)] for i in range(len(str(n)) + 1)]

# Crée une table dp1 pour les cas "égaux" au préfixe de n, dimensions : [longueur de n + 1][4]
dp1 = [[0 for j in range(4)] for i in range(len(str(n)) + 1)]

# Initialise un compteur 'po' à 0, utilisé pour compter les occurrences d'un chiffre ‘0’ parmi les chiffres parcourus
po = 0

# Initialise le point de départ pour les états ‘dp’ :
# dp0 à l'indice 0 et pour 0 chiffre non-zéro est bien 0 ; il n'y a aucune façon de former un nombre en partant de rien
dp0[0][0] = 0
# dp1 à l'indice 0 et pour 0 chiffre non-zéro est 1 ; il y a exactement une façon de former un "nombre vide"
dp1[0][0] = 1

# Boucle sur chaque position de chiffre de la gauche vers la droite (i de 1 jusqu'à longueur de s incluse)
for i in range(1, len(str(n)) + 1):
    # Calcule l'indice du chiffre actuel (i-1 car les index de chaînes commencent à 0)
    point = i - 1
    # Convertit le chiffre courant en entier
    np = int(s[point])
    # Si le chiffre courant est égal à 0, incrémente le compteur de zéros rencontrés jusqu'ici
    po += 1 if np == 0 else 0

    # Il y a exactement 1 façon de conserver un nombre vide lors du passage à la position suivante
    dp0[i][0] = 1
    # Quand on est dans la branche "égale à n", il n'y a aucune façon d'avoir 0 chiffre non-zéro sauf au tout début
    dp1[i][0] = 0

    # Pour 1 chiffre non-zéro :
    #   - dp1[i-1][0] * max(0, np-1): nombres ayant 0 chiffre non-zéro et dont le chiffre courant est strictement inférieur à np et non nul
    #   - dp0[i-1][0]*9: nombres strictement inférieurs à n à la position précédente et ajouter 1..9 ici (toujours un chiffre non-zéro)
    #   - dp0[i-1][1]: nombres strictement inférieurs à n déjà avec 1 chiffre non-zéro, on peut ajouter un zéro ici
    #   - (dp1[i-1][1] if np != 0 else 0): nombres "égaux" à n avec déjà 1 chiffre non-zéro, il est possible de poursuivre seulement si np!=0
    dp0[i][1] = (
        dp1[i-1][0] * (max(0, np-1)) +  # Prend tous les chiffres de 1 jusqu’à (np-1)
        dp0[i-1][0] * 9 +               # Ajoute un chiffre non-zéro à une séquence déjà plus petite que n
        dp0[i-1][1] +                   # Ajoute un zéro à une séquence déjà plus petite avec 1 chiffre non-zéro
        (dp1[i-1][1] if np != 0 else 0) # Continue la séquence égale si possible
    )
    # Il y a exactement 1 façon d'avoir exactement 1 chiffre non-zéro, c'est quand on a placé autant de chiffres que (i == 1 + nombre de 0)
    dp1[i][1] = 1 if i == 1 + po else 0

    # Pour 2 chiffres non-zéro, raisonnement analogue mais commence à partir d’avoir déjà 1 chiffre non-zéro
    dp0[i][2] = (
        dp1[i-1][1] * (max(0, np-1)) +  # Prend tous les chiffres < np pour la deuxième non-zero
        dp0[i-1][1] * 9 +               # Ajoute n'importe quel chiffre non-zéro à une séquence déjà plus petite avec 1 chiffre non-zéro
        dp0[i-1][2] +                   # Ajoute un zéro à une séquence déjà plus petite avec 2 chiffres non-zéro
        (dp1[i-1][2] if np != 0 else 0) # Continue la séquence égale si possible
    )
    # Il n'existe qu'une seule façon d'avoir 2 chiffres non-zéro si on a avancé sur (2 + nombre de 0) positions
    dp1[i][2] = 1 if i == 2 + po else 0

    # Pour 3 chiffres non-zéro, itération supplémentaire, selon la même logique
    dp0[i][3] = (
        dp1[i-1][2] * (max(0, np-1)) +  # Prend toutes les possibilités de la branche égale avant dernière non-zero
        dp0[i-1][2] * 9 +               # Ajoute n'importe quel chiffre non-zéro à une séquence déjà plus petite avec 2 chiffres non-zéro
        dp0[i-1][3] +                   # Ajoute un zéro à une séquence déjà plus petite avec 3 chiffres non-zéro
        (dp1[i-1][3] if np != 0 else 0) # Continue la séquence égale si possible
    )
    # Exactement une possibilité si on est sur la position (3 + nombre de 0 parcourt jusque là)
    dp1[i][3] = 1 if i == 3 + po else 0

# Affiche le nombre total de possibilités pour les chaînes de longueur égale à n, ayant k chiffres non-zéro
# On ajoute les deux cas : "strictement plus petit que n" et "exactement égal à n"
print(dp0[-1][k] + dp1[-1][k])  # -1 indique le dernier index de la table, soit tous les chiffres considérés