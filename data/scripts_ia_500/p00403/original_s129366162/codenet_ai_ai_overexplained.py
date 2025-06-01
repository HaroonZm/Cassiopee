# Demander à l'utilisateur de saisir un nombre entier, qui représente la taille ou le nombre d'éléments à traiter.
n = int(input())

# Demander à l'utilisateur de saisir une ligne de nombres séparés par des espaces, 
# puis convertir cette chaîne de caractères en une liste d'entiers
# map(int, ...) applique la fonction int à chaque élément obtenu en divisant la chaîne.
cats = list(map(int, input().split()))

# Initialiser une liste vide qui servira de pile pour stocker certains nombres selon une logique spécifique.
hole = []

# Initialiser une variable p avec la chaîne "OK". Cette variable servira à stocker soit "OK" si tout se passe bien,
# soit le numéro d'index (+1) où une condition d'erreur est rencontrée.
p = "OK"

# Parcourir chaque élément dans la liste cats, en utilisant son index i.
for i in range(n):
    # Vérifier si l'élément courant est un nombre négatif.
    if cats[i] < 0:
        # Si la pile hole est vide, ou que l'élément courant n'est pas l'opposé du dernier élément dans hole,
        # alors on a trouvé une inconsistance.
        if len(hole) == 0 or cats[i] != -1 * hole[-1]:
            # Enregistrer la position (index + 1 car on compte à partir de 1) où l'erreur apparaît,
            # puis sortir de la boucle car on a trouvé un problème.
            p = str(i + 1)
            break
        else:
            # Sinon, l'élément courant est bien l'opposé du dernier dans hole, donc on enlève ce dernier élément de la pile.
            hole.pop()
    else:
        # Si l'élément courant est positif, vérifier s'il est déjà dans la pile hole.
        # Cela signifie qu'on essaie d'ajouter un élément déjà présent, ce qui n'est pas permis.
        if cats[i] in hole:
            # Enregistrer la position (index + 1) où cette répétition illégale se produit.
            p = str(i + 1)
            # Sortir de la boucle.
            break
        else:
            # Si l'élément n'est pas déjà présent, on l'ajoute à la pile hole.
            hole.append(cats[i])

# Afficher soit "OK" si aucune incohérence n'a été trouvée,
# soit l'index + 1 où le premier problème a été détecté.
print(p)