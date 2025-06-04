# Demander à l'utilisateur d'entrer deux entiers (hauteur h et largeur w) séparés par un espace.
# La fonction input() permet de saisir des données au clavier. split() découpe la chaîne en une liste de chaînes séparées selon les espaces.
# map(int, ...) applique la fonction int à chaque élément de la liste résultante, transformant chaque élément en entier.
# Enfin, on affecte les deux premiers éléments à h et w.
h, w = map(int, input().split())

# On va ensuite lire une matrice carrée 10x10 représentant certains coûts, nommée ici c.
# On utilise une compréhension de liste (un concept Python permettant de construire des listes en une ligne).
# Pour chaque valeur de i de 0 à 9 (range(10)), on lit une ligne de 10 entiers saisis sur une même ligne.
# Ces 10 entiers sont convertis en entiers (avec map(int, ...)), puis transformés en liste.
# On obtient au final une liste de 10 listes de 10 entiers.
c = [list(map(int, input().split())) for i in range(10)]

# Maintenant, on applique algorithme de Floyd-Warshall pour calculer toutes les distances minimales entre chaque paire (i, j) de la matrice c.
# Floyd-Warshall trouve les plus courts chemins entre tous les couples de sommets dans un graphe pondéré.
# On va boucler trois fois : pour chaque sommet intermédiaire k, chaque départ i, chaque arrivée j.
for i in range(10):  # Pour chaque sommet de départ i parmi les 10 sommets possibles (numérotés de 0 à 9)
    for j in range(10):  # Pour chaque sommet d'arrivée j parmi les 10 sommets possibles
        for k in range(10):  # On teste chaque sommet intermédiaire k possible de 0 à 9
            # On compare la valeur actuelle du coût pour aller de i à j (c[i][j])
            # avec le coût pour aller de i à k, puis de k à j (c[i][k] + c[k][j])
            # Si passer par k est moins cher, on met à jour c[i][j]
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

# On répète une autre phase similaire, mais l'ordre des k est inversé (on fait 9-k au lieu de k)
for i in range(10):  # Pour chaque sommet de départ
    for j in range(10):  # Pour chaque sommet d'arrivée
        for k in range(10):  # On utilise 9-k pour parcourir k de 9 à 0
            # Encore une fois, on compare le coût direct à travers i->j
            # avec le coût via le sommet 9-k, c'est-à-dire le parcours inversé sur k
            c[i][j] = min(c[i][j], c[i][9 - k] + c[9 - k][j])

# Une nouvelle application de Floyd-Warshall (la redondance peut servir à la convergence des valeurs selon le problème)
for i in range(10):  # Encore, pour chaque sommet de départ
    for j in range(10):  # Pour chaque sommet d'arrivée
        for k in range(10):  # Pour chaque intermédiaire k de 0 à 9
            # On assure que c[i][j] est le minimum entre le chemin direct c[i][j] et le chemin passant par k
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

# Maintenant, on prépare la liste l qui va contenir des valeurs lues depuis l'entrée utilisateur.
# Cette liste combine toutes les entrées, chacune étant une ligne de w entiers (pour chaque ligne, i dans range(h))
l = []
for i in range(h):  # Pour chaque ligne de la grille de hauteur h
    # On va lire une ligne qui contient w entiers (selon largeur w)
    # On utilise map(int, ...) pour transformer chaque élément en entier, puis list() pour obtenir une liste
    # On ajoute (avec extend) ces w valeurs à la liste l principale (extend concatène les listes)
    l.extend(list(map(int, input().split())))

# Initialisation d'un accumulateur x à 0. On va calculer une somme pondérée.
x = 0

# On va parcourir tous les chiffres de 0 à 9 (les indices possibles des valeurs dans l)
for i in range(10):
    # l.count(i) compte le nombre d'occurrences de la valeur i dans la liste l.
    # c[i][1] est le coût minimal pour transformer i en 1, déterminé auparavant grâce à Floyd-Warshall.
    # On multiplie le coût pour i->1 par le nombre de fois que i apparaît dans la grille.
    # On ajoute ce produit à x pour accumuler le coût total.
    x += c[i][1] * l.count(i)

# Enfin, on affiche la somme totale des coûts pour remplacer tous les chiffres de la grille par 1 selon les coûts optimisés.
print(x)