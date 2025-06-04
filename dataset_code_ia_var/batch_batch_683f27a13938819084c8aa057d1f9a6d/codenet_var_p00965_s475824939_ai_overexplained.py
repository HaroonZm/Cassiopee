# Demander à l'utilisateur d'entrer une valeur entière, puis convertir l'entrée en int et la stocker dans la variable 'n'
# Cela représente le nombre de paires d'entiers qui devront ensuite être saisies et traitées
n = int(input())

# Créer une liste de listes nommée 'ab', où chaque sous-liste correspond à une paire (a, b)
# Pour chaque itération dans la plage (n), on lit une ligne de l'entrée utilisateur, on la découpe en entiers,
# puis on convertit chacun de ces entiers en utilisant map(int, ...), on regroupe le tout dans une liste, et on l'ajoute à 'ab'
ab = [list(map(int, input().split())) for _ in range(n)]

# Initialiser deux variables à 0 : 'pol1' et 'pol2'
# Ces variables serviront à stocker des valeurs maximales calculées plus tard dans le code
pol1 = 0
pol2 = 0

# Créer une liste bidimensionnelle 'ft' de taille 100000 x 2, initialisée avec des zéros
# Chaque élément 'ft[i]' est une liste de 2 zéros [0, 0]
# Cette structure est utilisée pour compter certaines occurrences associées aux numéros dans les paires (a, b)
ft = [[0] * 2 for _ in range(100000)] 

# Pour chaque sous-liste 'i' dans 'ab' (qui sont des paires [a, b]),
# Incrémenter le premier élément dans 'ft' à l'indice (a-1) (premier élément de la paire), colonne 0
# Incrémenter le second élément dans 'ft' à l'indice (b-1) (deuxième élément de la paire), colonne 1
# Cela permet de compter combien de fois chaque nombre apparaît respectivement comme "a" et comme "b"
for i in ab:
    # Comme les listes sont indexées à partir de 0 mais les entrées sont probablement à partir de 1, on soustrait 1
    ft[i[0] - 1][0] += 1
    ft[i[1] - 1][1] += 1

# Créer une nouvelle liste bidimensionnelle 'ftsum' de taille 100000 x 2, initialisée à zéro
# Cette structure permettra de stocker les sommes cumulées pour chaque colonne de 'ft'
ftsum = [[0] * 2 for _ in range(100000)]

# Initialiser pour la première ligne (indice 0) la somme cumulée égale à la valeur de 'ft[0][0]'
# Cela démarre l'accumulation pour la première colonne
ftsum[0][0] = ft[0][0]

# Boucler sur toute la longueur de 'ft' à partir de l'indice 1 jusqu'à la fin
for i in range(1, len(ft)):
    # Pour la colonne 0 : Somme cumulée jusqu'à l'index courant = somme cumulée précédente + valeur actuelle de 'ft'
    ftsum[i][0] = ftsum[i-1][0] + ft[i][0]
    # Pour la colonne 1 : Idem mais sur la deuxième colonne
    ftsum[i][1] = ftsum[i-1][1] + ft[i][1]

# Calculer la valeur maximale de (somme cumulée de la première colonne - somme cumulée de la deuxième colonne)
# pour chaque index jusqu'à len(ft)-2
# Initialise une boucle de 0 à len(ft)-2 (parce que range s'arrête avant len(ft)-1)
for i in range(len(ft)-1):
    # Pour chaque index, calculer la différence entre le nombre cumulé d'apparitions comme "a"
    # et comme "b" jusqu'à cet index, puis mettre à jour 'pol2' si ce résultat est plus grand
    pol2 = max(pol2, ftsum[i][0] - ftsum[i][1])

# Pour chaque paire (f, t) dans la liste 'ab'
for f, t in ab:
    # Réduction de 1 pour obtenir des indices de liste corrects
    f = f-1
    t = t-1
    # Calculer la somme cumulée d'apparitions comme "a" jusqu'à l'index t-1
    temp = ftsum[t-1][0]
    # Si 'f' n'est pas le tout premier indice,
    # soustraire du résultat la somme cumulée d'apparitions comme "b" jusqu'à l'indice 'f'
    # excluant donc toute la partie de 'ftsum' liée à l'intervalle avant 'f'
    if f != 0:
        temp -= ftsum[f][1]
    # Prendre la valeur maximale absolue pour 'pol1' entre sa valeur courante et celle calculée
    pol1 = max(pol1, temp)

# Afficher les deux résultats calculés, séparés par un espace, comme demandé par l'énoncé
print(pol1, pol2)