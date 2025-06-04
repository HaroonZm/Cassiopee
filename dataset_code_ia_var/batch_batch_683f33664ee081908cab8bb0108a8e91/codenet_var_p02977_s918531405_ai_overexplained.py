# Demander à l'utilisateur d'entrer un nombre entier et convertir la saisie en entier
n = int(input())  # 'input()' lit une chaîne, 'int()' la convertit en entier

# Calculer la puissance de 2 la plus élevée qui ne dépasse pas n
# 'n.bit_length()' donne le nombre de bits nécessaires pour représenter n
# Soustraire 1 pour obtenir la position du bit le plus à gauche (plus significatif, indexé à 0)
# '1 << (n.bit_length()-1)' décale le bit 1 à gauche pour positionner un 1 au bit le plus significatif de n
b = 1 << (n.bit_length()-1)

# Vérifie si n est exactement égal à cette puissance de 2 (si n - b == 0)
if n - b == 0:
    # Si c'est le cas, afficher "No" (aucune solution ou condition non satisfaite)
    print("No")
else:
    # Si ce n'est pas le cas, continuer le traitement
    print("Yes")  # Afficher "Yes" pour indiquer qu'on continue
    # Afficher la paire (1, 2)
    print(1, 2)
    # Afficher la paire (2, 3)
    print(2, 3)
    # Afficher la paire (3, n+1), on relie le sommet 3 au sommet n+1 (n+1 entier, pas une addition numérique de caractères)
    print(3, n+1)
    # Afficher la paire (n+1, n+2)
    print(n+1, n+2)
    # Afficher la paire (n+2, n+3)
    print(n+2, n+3)
    # Boucler pour générer et afficher les arêtes supplémentaires
    # On commence à 4 et on va jusqu'à n-1 inclus (car 'range' est exclusif en fin), par pas de 2
    for i in range(4, n, 2):
        # Afficher la paire (i, i+1)
        print(i, i+1)
        # Afficher la paire (i+n, i+n+1)
        # Cela crée un décalage de n pour l'autre copie de l'indice
        print(i+n, i+n+1)
        # Afficher la paire (1+n, i+n)
        # Connecte le sommet 1+n à i+n 
        print(1+n, i+n)
        # Afficher la paire (1+n, i+1)
        # Connecte le sommet 1+n à i+1
        print(1+n, i+1)
    # Après la boucle, vérifier si n est pair
    # '~n' est l'opérateur bitwise NOT, il inverse tous les bits de n
    # '&1' teste le bit de poids faible (parité), donc 'if (~n)&1' est vrai si n est pair
    if (~n)&1:
        # Afficher la paire (n, b+n)
        print(n, b+n)
        # Calculer le XOR entre n, b et 1
        # '^' est l'opérateur bitwise XOR
        a = n ^ b ^ 1
        # Afficher la paire (n+n, a)
        print(n+n, a)