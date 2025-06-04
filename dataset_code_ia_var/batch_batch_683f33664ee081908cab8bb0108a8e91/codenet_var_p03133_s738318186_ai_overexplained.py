import sys  # Importe le module sys, nécessaire pour lire les entrées depuis sys.stdin

# Le programme va résoudre un problème mathématique basé sur les opérations sur des matrices binaires.
# Les entrées décrivent une matrice binaire (n lignes et m colonnes).
# L'objectif est de trouver une certaine quantité liée aux "formes réduites" de la matrice et au nombre de sous-ensembles ayant une propriété de parité.

# Lire les deux premiers entiers donnés : nombre de lignes 'n' et nombre de colonnes 'm'
n, m = map(int, input().split())  # 'map' applique 'int' à chaque élément du split, pour obtenir deux entiers

MOD = 998244353  # Un grand nombre premier utilisé pour éviter les débordements lors des calculs modulo (problème classique en combinatoire)

rows = []  # Initialiser une liste vide pour stocker la représentation binaire de chaque ligne de la matrice

# Lire chaque ligne restante de l'entrée standard (input utilisateur ou fichier redirigé)
for line in sys.stdin:  # Boucle sur chaque ligne restante
    # Enlève les espaces finaux et scinde la ligne (éventuellement séparée par des espaces)
    b = ''.join(line.rstrip().split())  # On retire les espaces et colle tous les caractères ensemble
    # Convertit la chaîne binaire en entier. Par exemple, "101" devient 5.
    rows.append(int(b, base=2))  # 'int(b, base=2)' gère la conversion de binaire à entier

independent_row = 0  # Sert à compter le nombre de lignes indépendantes dans la matrice (rang de la matrice)

# Nous allons effectuer une variante du "Gaussian Elimination" (méthode d'élimination de Gauss) binaire,
# c'est-à-dire transformer la matrice pour isoler un maximum de lignes indépendantes (rang).
while rows:  # Tant qu'il reste des lignes (non nulles)
    x = max(rows)  # Prendre la ligne avec la plus grande valeur binaire (plus à gauche)
    if x == 0:     # Si c'est 0, toutes les lignes restantes sont nulles : on arrête
        break
    independent_row += 1  # Incrémente le compteur de rang, car x est une nouvelle ligne indépendante
    y = 1 << (x.bit_length() - 1)  # Trouve la position du bit le plus à gauche dans x (un masque binaire)
    # Pour chaque ligne r différente de x,
    # - si r partage ce bit à 1 avec x : 'r & y' vrai => r ^= x (xor bit-à-bit, simule la soustraction dans GF(2))
    # - si r ne partage pas ce bit : on garde r tel quel
    # Ceci élimine le bit principal de x de toutes les autres lignes, "descendant" la matrice vers une forme échelonnée.
    rows = [r ^ x if r & y else r for r in rows if r != x]  # Mise à jour de la liste des lignes

# Une fois les opérations effectuées, 'independent_row' contient le rang (le nombre de lignes non nulles restantes)

# Calcul du résultat final selon la formule mathématique suivante :
# (Nombre total de sélections de lignes et colonnes possibles avec au moins une ligne indépendante sélectionnée)
# divisée par 2 (parité).
# pow(2, n + m - 1, MOD) : toutes les façons de choisir lignes et colonnes pour faire des sous-ensembles sauf pour la moitié des cas d'intérêt.
# pow(2, n + m - independent_row - 1, MOD) : cas où aucune ligne indépendante n'est sélectionnée (à retirer).
# Le modulo garde le résultat borné pour éviter les débordements.

ans = (pow(2, n + m - 1, MOD) - pow(2, n + m - independent_row - 1, MOD)) % MOD  # Calcul détaillé ci-dessus

print(ans)  # Affiche la réponse finale