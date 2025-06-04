from heapq import heapify, heappop, heappush

# Lire toutes les entrées depuis l'entrée standard, les convertir en entiers et les mettre dans une liste
# map applique int à chaque valeur de open(0).read().split()
valeurs_entrees = list(map(int, open(0).read().split()))
# n est le premier entier, les autres sont dans a
n = valeurs_entrees[0]
a = valeurs_entrees[1:]

# Préparer la première file de priorité (min-heap) avec les n premiers éléments de a
# Cette file va contenir les scores des éléments de gauche
hq1 = [x for x in a[:n]]

# Préparer la seconde file de priorité (toujours un heap min) pour les éléments de droite
# On négative chaque valeur car on veut gérer un max-heap (heapq ne gère que min-heap)
# On prend les n derniers éléments de la liste (après les 2n premiers)
hq2 = [-x for x in a[n+n:]]

# Calculer la somme totale des éléments dans le premier heap; s'agit, au départ, de la somme des n premiers éléments
su1 = sum(hq1)

# Calcul de la somme totale des éléments négativés dans le second heap : on remet le signe positif
su2 = -sum(hq2)

# Initialiser deux listes pour retenir les valeurs successives de su1 et su2 lors des traitements
# On met la somme initiale comme premier élément
mem1 = [su1]
mem2 = [su2]

# Transformer nos listes en heaps valides selon l'algorithme du tas (heapify)
heapify(hq1)  # hq1 devient un min-heap classique
heapify(hq2)  # hq2 devient aussi un min-heap, mais comme les valeurs sont négatives, il agit comme un max-heap

# Traiter les n éléments du milieu (ceux entre les premiers n et les derniers n)
for x in a[n:n+n]:
    # Retirer le plus petit élément du premier heap (min-heap)
    y = heappop(hq1)
    # Si le nouvel élément x est supérieur à ce plus petit élément
    if x > y:
        # On met x dans le heap, à la place du plus petit (pour avoir toujours les n plus grands possibles)
        heappush(hq1, x)
        # Mettre à jour la somme en ajoutant la valeur gagnée (x) et en retirant la plus petite (y)
        su1 += x - y
    else:
        # Si x n'est pas plus grand, on remet y dans le heap (pas de changement)
        heappush(hq1, y)
    # Enregistrer la somme actuelle dans mem1
    mem1.append(su1)

# Traiter les mêmes n éléments du milieu, mais en partant de la fin (pour faire l'autre sens)
for x in reversed(a[n:n+n]):
    # On retire le plus petit élément du heap, mais comme les valeurs sont négatives, on inverse le signe pour récupérer la valeur originale
    y = -heappop(hq2)
    # Si x est inférieur à ce maximum (toujours en considérant le côté droit), il peut prendre la place dans le heap
    if x < y:
        # On place -x pour maintenir la convention max-heap
        heappush(hq2, -x)
        # Met à jour la somme en retirant la valeur remplacée (y) et ajoutant la nouvelle (x)
        su2 -= y - x
    else:
        # Sinon, on remet y dans le heap (en négatif)
        heappush(hq2, -y)
    # On stocke la somme actuelle dans mem2
    mem2.append(su2)

# À la fin, on veut calculer, pour chaque possible position de coupe, la différence maximale
# entre sum_max_gauche (mem1) et sum_min_droite (mem2, inversé pour aligner l'ordre)
# zip permet d'itérer sur les éléments en parallèle
# On calcule la différence et prend le maximum de toutes les possibilités
print(max(f - b for f, b in zip(mem1, mem2[::-1])))