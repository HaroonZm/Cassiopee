# Demande à l'utilisateur de saisir deux valeurs séparées par un espace, puis attribue la première à 'h' et la seconde à 'r'
# 'input()' lit les données saisies, 'split()' les découpe selon les espaces
# 'map(int, ...)' transforme toutes les sous-chaînes en entiers
h, r = map(int, input().split())

# Cette condition teste si la variable 'h' est strictement inférieure à zéro
if h < 0:
    # Si 'h' est négatif, on doit examiner la somme de 'h' et 'r'
    # On teste ici si cette somme est strictement négative
    if h + r < 0:
        # Si la somme est négative, on affiche '-1'
        print(-1)
    # Sinon, on vérifie si la somme de 'h' et 'r' est exactement égale à zéro
    elif h + r == 0:
        # Si la somme est nulle, on affiche '0'
        print(0)
    else:
        # Si aucune des conditions précédentes n'est vérifiée, donc la somme est positive
        # Dans ce cas, on affiche '1'
        print(1)
else:
    # Si 'h' n'est pas négatif (donc s'il est zéro ou positif), on affiche simplement '1'
    print(1)