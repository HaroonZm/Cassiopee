# On commence par initialiser une liste 'c' de 6 éléments, tous identiques, chaque élément étant une liste [0, 0]. 
# En Python, multiplier une liste crée plusieurs références vers la même liste, donc ici chaque sous-liste pointe vers le même objet [0, 0].
c = [[0, 0]] * 6

# On utilise une boucle for pour itérer sur les entiers de 0 à 5 (inclus), c'est-à-dire 6 itérations pour remplir la liste 'c'.
for i in range(6):
    # On lit une ligne de l'entrée utilisateur, on sépare cette ligne en deux entiers grâce à split(), 
    # puis on transforme chaque morceau de texte en entier via map(int, ...).
    # La fonction sorted() met ces deux entiers dans l'ordre croissant et retourne une nouvelle liste [a, b] avec a <= b.
    a, b = sorted(map(int, input().split()))
    # On remplace la i-ème sous-liste dans 'c' par la liste [a, b] calculée juste avant.
    c[i] = [a, b]

# On trie la liste 'c' en place selon l'ordre lexicographique : d'abord sur le premier élément de chaque sous-liste, puis sur le second.
c.sort()

# On commence une boucle qui va de l'indice 0 à 4 (inclus) par pas de 2, c'est-à-dire i prendra les valeurs 0, 2, 4.
for i in range(0, 6, 2):
    # À chaque itération, on compare le i-ème sous-liste à la suivante (i+1)-ème sous-liste.
    # Si elles sont différentes, cela signifie qu'au moins une paire n'est pas identique.
    if c[i] != c[i+1]:
        # On affiche 'no' pour signaler que la condition d'appariement n'est pas satisfaite.
        print('no')
        # On utilise break pour sortir immédiatement de la boucle, car il ne sert à rien de continuer.
        break
# Si la boucle for n'a jamais rencontré la commande break, le bloc else associé à la boucle for s'exécute (c'est une particularité de Python).
else:
    # On doit vérifier si les trois paires obtenues peuvent former un pavé rectangle.
    # Le tableau c trié contient normalement trois couples répétés deux fois chaque.
    # Les conditions suivantes vérifient :
    # - que le premier élément de la première paire est égal au premier élément de la deuxième paire.
    # - que le deuxième élément de la première paire est égal au premier élément de la troisième paire.
    # - que le deuxième élément de la deuxième paire est égal au deuxième élément de la troisième paire.
    # Si toutes ces conditions sont vraies, cela veut dire que les trois côtés peuvent former un parallélépipède rectangle.
    # L'expression c[0][0]==c[2][0] and c[0][1]==c[4][0] and c[2][1]==c[4][1] retourne True ou False.
    # On l'utilise comme indice pour une liste ['no', 'yes'] : 
    # - Si l'expression vaut True (c'est-à-dire égal à 1), on affiche 'yes'.
    # - Si l'expression vaut False (donc égal à 0), on affiche 'no'.
    print(['no', 'yes'][c[0][0] == c[2][0] and c[0][1] == c[4][0] and c[2][1] == c[4][1]])