# Demande à l'utilisateur de saisir deux entiers séparés par un espace, puis extrait chacun d'eux.
# 'n' correspondra au nombre total d'éléments qui seront ajoutés à la liste 'l'.
# 'p' est un paramètre qui sera utilisé plus tard dans les calculs.
n, p = map(int, input().split())

# Initialisation d'une liste vide appelée 'l'.
# Cette liste stockera n sous-listes, chacune représentant une ligne d'entrée.
l = []

# Boucle for qui s'exécutera exactement 'n' fois, représentant chaque ligne d'entrée.
# 'i' commence à 0 et s'incrémente de 1 jusqu'à n-1.
for i in range(n):
    # Demande à l'utilisateur de saisir une ligne d'entiers séparés par un espace.
    # map(int, input().split()) convertit chaque élément entré en entier.
    # list() encapsule ce résultat en une liste Python.
    # La sous-liste ainsi obtenue est ajoutée à la liste principale 'l' via la méthode 'append'.
    l.append(list(map(int, input().split())))

# Trie la liste 'l' selon un critère donné par une fonction lambda (fonction anonyme).
# 'key' définit le critère de tri : pour chaque sous-liste 'x' de 'l',
# on calcule 'x[0] * (100-p) + x[1] * p', puis on le multiplie par -1.
# Cela signifie qu'on trie en fait par ordre décroissant selon ce calcul.
l.sort(key=lambda x: -(x[0] * (100 - p) + x[1] * p))

# Initialisation d'une variable entière 'z' à 0.
# Elle sera utilisée comme accumulateur pour une somme.
z = 0

# Une nouvelle boucle for qui recommence à 'i = 0' et itère jusqu'à 'i = n-1'.
# À chaque itération, on soustrait (à cause du signe '-') l'élément d'index 1 (c'est-à-dire le deuxième élément)
# de chaque sous-liste de 'l', multiplié par 'p', et on l'ajoute à 'z'.
for i in range(n):
    z += -l[i][1] * p

# On réinitialise la variable 'i' à 0.
i = 0

# Tant que la variable 'z' reste inférieure à 0 (c'est-à-dire négative),
# on continue la boucle suivante.
while z < 0:
    # À chaque tour de boucle, on ajoute à 'z' la valeur calculée à partir de la sous-liste d'indice i :
    # On multiplie le premier élément par (100-p), puis on ajoute le produit du deuxième élément par p.
    z += l[i][0] * (100 - p) + l[i][1] * p
    # On incrémente 'i' de 1 pour passer à la sous-liste suivante lors de la prochaine itération.
    i += 1

# Une fois que la boucle while se termine (c'est-à-dire lorsque z n'est plus négatif, donc z >= 0),
# on affiche la valeur actuelle de 'i' qui représente le nombre minimal de sous-listes
# nécessaires pour que la somme cumulée devienne non négative.
print(i)