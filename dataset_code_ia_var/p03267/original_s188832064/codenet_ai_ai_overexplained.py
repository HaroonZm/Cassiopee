# Demande à l'utilisateur de saisir un entier, stocke la valeur dans la variable l
l = int(input())

# Boucle for pour trouver le plus petit entier n tel que 2^n > l
# La plage est de 0 à 20 inclus (car range(21) s'arrête avant 21)
for i in range(21):
    # Calculer 2 exposant i (i.e., 2^i)
    if 2 ** i > l:
        # Si 2^i est strictement supérieur à l, on a trouvé notre n minimal
        n = i     # On sauvegarde la valeur de i dans n
        break     # On sort immédiatement de la boucle car la condition est satisfaite

# On calcule la valeur de m, qui est le double de n-1
m = (n - 1) * 2

# On calcule s, la différence entre l et 2^(n-1)
s = l - 2 ** (n - 1)

# On initialise value avec la puissance de 2 maximale qui ne dépasse pas l
value = 2 ** (n - 1)

# On crée une liste path_add de taille n-1 remplie de zéros
# Cette liste indiquera pour chaque rang si un chemin alternatif doit être ajouté (1) ou non (0)
path_add = [0 for i in range(n - 1)]

# On crée une liste path_add_value de taille n-1 remplie de zéros
# Cette liste contiendra les valeurs à ajouter aux chemins alternatifs correspondants
path_add_value = [0 for i in range(n - 1)]

# Boucle sur chaque indice i de 0 à n-2 inclus (les étapes du chemin)
for i in range(n - 1):
    # On regarde si s est supérieur ou égal à 2^(n-2-i)
    if s >= 2 ** (n - 2 - i):
        # On retire 2^(n-2-i) à s
        s -= 2 ** (n - 2 - i)
        # On marque que pour ce rang, il y aura un chemin supplémentaire
        path_add[-(i + 1)] = 1   # On utilise -(i + 1) pour remplir la liste à l'envers (à partir de la fin)
        # On sauvegarde la valeur actuelle à utiliser pour ce nouveau chemin
        path_add_value[-(i + 1)] = value
        # On augmente 'value' de 2^(n-2-i) pour le prochain potentiel ajout
        value += 2 ** (n - 2 - i)

# Les lignes suivantes étaient commentées dans le code d'origine, donc inutiles ici, on ne les décommente pas.

# Affichage du résultat :
# Premier print : affiche deux entiers séparés par un espace
# 'n' correspond au nombre total de sommets,
# 'm' au nombre total d'arêtes de base,
# puis on ajoute à 'm' la somme des 1 dans la liste path_add (nombre de chemins alternatifs à ajouter)
print(n, m + sum(path_add))

# Deuxième boucle pour afficher les arêtes de base
# Jusqu'à n-1 car il existe toujours n-1 arêtes entre les sommets consécutifs dans le chemin principal
for i in range(n - 1):
    # Affiche une arête du sommet i+1 au sommet i+2 avec un poids de 0
    print(i + 1, i + 2, 0)
    # Affiche une arête du sommet i+1 au sommet i+2 avec un poids de 2^i
    print(i + 1, i + 2, 2 ** i)

# Troisième boucle pour afficher les chemins alternatifs s'il y en a
for i in range(n - 1):
    # Si pour ce rang il faut ajouter un chemin alternatif alors path_add[i]==1
    if path_add[i] == 1:
        # Affiche une arête partant du sommet i+1 vers le dernier sommet n avec le poids associé
        print(i + 1, n, path_add_value[i])