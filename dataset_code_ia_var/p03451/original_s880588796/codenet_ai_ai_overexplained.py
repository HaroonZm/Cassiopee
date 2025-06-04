import sys  # Ce module permet d'accéder à certaines variables et fonctions propres à l'interpréteur Python

# On lit une ligne depuis l'entrée standard (par exemple, le clavier ou un fichier)
# .readline() lit une seule ligne, incluant le caractère de saut de ligne '\n' à la fin
# int() convertit la chaîne de caractères obtenue en un entier
N = int(sys.stdin.readline())

# On crée une liste vide nommée xs qui servira à stocker les sommes cumulées.
xs = []

# On déclare la variable s et on lui affecte la valeur 0. Cette variable sera utilisée pour accumuler des sommes.
s = 0

# On lit une nouvelle ligne depuis l'entrée standard.
# .split() découpe la chaîne en morceaux (sous-chaînes), en séparant selon les espaces par défaut.
# map(int, ...) permet de convertir chaque sous-chaîne en entier.
# La boucle va itérer sur chaque entier x de cette liste.
for x in map(int, sys.stdin.readline().split()):
    # On ajoute la valeur de x à la variable s.
    # Cela permet d'obtenir la somme cumulée jusqu'ici.
    s += x
    # On ajoute la nouvelle valeur de s à la liste xs à l'aide de la méthode .append().
    xs.append(s)

# On remet la variable s à 0 pour l'utiliser dans la prochaine boucle.
s = 0

# On lit encore une ligne, on convertit chaque morceau en entier, et on les énumère pour obtenir aussi leur position (i).
# enumerate() renvoie pour chaque élément deux informations :
#   - son indice i (c'est-à-dire sa position dans la liste, en commençant à 0)
#   - sa valeur x.
for i, x in enumerate(map(int, sys.stdin.readline().split())):
    # Pour chaque élément :
    # - On prend la plus grande valeur entre la variable s actuelle et la valeur cumulative xs[i].
    #   Cela correspond à max(s, xs[i])
    # - On ajoute à cette valeur la valeur actuelle x
    # - On stocke le résultat dans la variable s, qui sert ainsi à mémoriser la solution intermédiaire optimale.
    s = max(s, xs[i]) + x

# On affiche le résultat final, c'est-à-dire la valeur calculée et stockée dans la variable s.
print(s)