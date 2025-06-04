# Demande à l'utilisateur de saisir une ligne d'entrée
# input() attend que l'utilisateur entre des valeurs, séparées ici par des espaces
# split() découpe la chaîne saisie en une liste de sous-chaînes selon les espaces
# map(int, ...) applique la fonction int à chaque élément de la liste pour convertir les entrées en nombres entiers
# Puis, nous utilisons l'affectation multiple pour stocker les 4 entiers respectivement dans A, B, C et D
A, B, C, D = map(int, input().split())

# Nous voulons trouver l'intersection entre deux intervalles [A, B] et [C, D]
# max(A, C) trouve le point de début commun le plus tardif entre les deux intervalles (le maximum des deux débuts)
# min(B, D) trouve le point de fin commun le plus précoce entre les deux intervalles (le minimum des deux fins)
# L'intersection, si elle existe, sera donc [max(A, C), min(B, D)]
# x calcule la longueur possible de cette intersection
x = min(B, D) - max(A, C)

# On vérifie si la valeur de x est strictement supérieure à 0
# Cela veut dire qu'il existe effectivement une intersection positive (au moins un point commun)
if x > 0:
    # Si c'est le cas, on affiche la longueur de l'intersection
    print(x)
else:
    # Sinon, les intervalles ne se chevauchent pas ou se touchent exactement aux extrémités (intersection nulle)
    # On affiche "0" pour indiquer l'absence d'intersection réelle
    print("0")