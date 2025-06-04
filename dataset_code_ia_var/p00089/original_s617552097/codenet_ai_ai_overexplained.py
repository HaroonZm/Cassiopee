import sys  # Importe le module sys qui permet d'accéder à certains objets utilisés ou maintenus par l'interpréteur Python (comme sys.stdin pour l'entrée standard)

# Lit l'ensemble des lignes envoyées sur l'entrée standard (généralement l'utilisateur tape ou on redirige un fichier)
# sys.stdin est un itérable qui donne chaque ligne en entrée l'une après l'autre, sous forme de chaîne de caractères (str)
# Utilisation d'une compréhension de liste pour transformer chaque ligne
# Pour chaque ligne : 
#    - supprime le caractère de fin de ligne (non explicitement ici, OK si format parfait)
#    - divise la chaîne en morceaux en découpant sur la virgule (split(','))
#    - applique la conversion en int à chaque morceau (map(int, ...))
#    - transforme le map (itérable) en liste pour obtenir une liste d'entiers correspondant à une "ligne" du triangle
# Donc s : liste de listes d'entiers, chaque sous-liste est une ligne du triangle
s = [list(map(int, e.split(','))) for e in sys.stdin]

# Boucle à partir de la deuxième ligne (indice 1) jusqu'à la dernière ligne de s (le triangle), inclusivement
for i in range(1, len(s)):
    # k est le nombre d'éléments sur la ligne courante i
    k = len(s[i])
    # Pour chaque colonne (élément) de la ligne courante, on va essayer de trouver le "meilleur chemin"
    for j in range(k):
        # Pour chaque élément à la colonne j, on veut regarder les éléments possibles au-dessus
        # On doit gérer le cas où la ligne précédente a moins d'éléments que la ligne actuelle
        # Soustraction de 1 à j seulement si la ligne précédente est plus courte : (k > len(s[i-1])) est un booléen True(=1) ou False(=0)
        t = j - (k > len(s[i-1]))
        # s[i][j] = valeur actuelle
        # On va accéder à la sous-liste s[i-1][...] qui contient le/les éléments précédents adjacents sur la ligne au-dessus
        # (j>0) est True(=1) si on n'est pas sur le 1er élément ; t*(j>0) est donc 0 ou t
        # t+2 marque la borne de fin d'intervalle
        # On prend le maximum des valeurs "adjacentes" de la ligne précédente (peut être une ou deux valeurs)
        # Ajoute ce maximum à la valeur courante
        s[i][j] += max(s[i-1][t*(j > 0):t + 2])

# Après avoir fini toutes les lignes, la dernière ligne s[-1] contient les sommes maximales
# Affiche ces valeurs sur une seule ligne, séparées par des espaces
print(*s[-1])  # Le * permet de "dépaqueter" la liste, donc chaque élément de la liste devient un argument séparé pour print(), il y aura des espaces automatiquement entre eux