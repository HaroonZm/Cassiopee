# On lit trois entiers depuis une seule ligne d'entrée utilisateur, séparés par des espaces.
# Les trois valeurs sont assignées respectivement à n, m, t.
# La fonction map applique int à chaque élément découpé dans l'entrée.
n, m, t = map(int, input().split())

# On initialise une variable d à 0 pour stocker un compteur cumulatif.
d = 0

# On lit une deuxième ligne d'entrée que l'on découpe avec split, et on convertit chaque morceau en int pour former une liste.
a = [int(i) for i in input().split()]

# b représente la borne inférieure du segment courant, initialisée à la première valeur moins m.
b = a[0] - m

# c représente la borne supérieure courante, initialisée à la première valeur plus m.
c = a[0] + m

# On parcourt tous les éléments de la liste a à partir du deuxième (indice 1) jusqu'au dernier (indice n-1).
for i in range(1, n):
    # Si l'élément courant a[i] est supérieur à c+m, cela veut dire qu'il y a un écart supérieur à m
    # entre la borne supérieure du segment précédent et la borne inférieure du nouveau segment.
    if a[i] > c + m:
        # On ajoute à d la longueur du segment précédent, qui est c-b.
        d += c - b
        # On commence un nouveau segment : b devient a[i]-m.
        b = a[i] - m
    # Dans tous les cas, on met à jour la borne supérieure du segment courant pour qu'elle soit a[i]+m.
    c = a[i] + m

# Après la boucle, il peut rester un segment à prendre en compte.
# Si la borne supérieure c est strictement inférieure à t, on ajoute la longueur c-b à d.
if c < t:
    d += c - b
# Sinon, cela veut dire que c dépasse ou atteint t, donc le segment s'arrête à t (et non à c).
else:
    d += t - b

# On affiche t-d, qui représente le complément de la somme des segments cumulés d par rapport à t.
print(t - d)