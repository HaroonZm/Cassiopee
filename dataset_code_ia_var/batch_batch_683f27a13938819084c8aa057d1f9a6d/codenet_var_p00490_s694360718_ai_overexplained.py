# Lire l'entrée standard (le fichier correspondant à l'entrée 0) et la découper selon les espaces
# map(int, ...) convertit chaque string issue du split en entier
# L'opérateur * permet d'affecter la suite des éléments restants à la liste D
N, A, B, C, *D = map(int, open(0).read().split())

# On trie la liste D dans l'ordre décroissant (reverse=1 est équivalent à reverse=True)
# Ceci place les valeurs les plus grandes au début de D afin d'en profiter dans l'ordre optimal
D.sort(reverse=1)

# On initialise la variable ans, qui représentera notre résultat final maximal
# C // A effectue une division entière (par exemple, 7 // 2 donnera 3)
# ans est ainsi la valeur maximale possible sans utilisation d'éléments de D
ans = C // A

# On initialise la variable s à 0
# s servira à stocker la somme cumulée des i plus grands éléments de D
s = 0

# La boucle for parcourt les indices de 0 à N - 1
# range(N) génère une séquence d'entiers de 0 jusqu'à (N-1)
for i in range(N):
    # On ajoute la valeur D[i] (l'élément le plus grand restant) à la somme cumulée s
    s += D[i]
    # On calcule une nouvelle valeur potentielle de ans avec les i+1 premiers suppléments de D
    # Le dénominateur est A augmenté de (i + 1) fois B (i+1 suppléments choisis)
    # Le numérateur est C augmenté de la somme des i+1 meilleurs D
    # On effectue à nouveau une division entière (//)
    # max(ans, ...) met à jour ans uniquement si le nouveau calcul est plus grand
    ans = max(ans, (C + s) // (A + (i + 1) * B))

# Enfin, on affiche la valeur maximale trouvée
print(ans)