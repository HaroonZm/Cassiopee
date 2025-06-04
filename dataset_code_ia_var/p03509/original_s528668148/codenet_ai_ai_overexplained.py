# Demander à l'utilisateur d'entrer deux entiers séparés par un espace :
# - n : le nombre d'éléments à traiter (nombre de lignes suivantes)
# - p : un entier qui sera utilisé dans les calculs suivants
n, p = map(int, input().split())

# Initialiser deux listes vides :
# - w sera utilisée pour stocker les valeurs ww de chaque entrée
# - b sera utilisée pour stocker les valeurs bb de chaque entrée
w, b = [], []

# Boucle répétée n fois (une fois pour chaque élément que nous devons lire)
for _ in range(n):
    # Lire deux entiers séparés (ww et bb) à partir de l'entrée utilisateur
    ww, bb = map(int, input().split())
    # Ajouter ww à la fin de la liste w
    w.append(ww)
    # Ajouter bb à la fin de la liste b
    b.append(bb)

# Initialiser une liste vide s qui va contenir certains scores calculés pour chaque élément
s = []

# Utiliser la fonction zip pour créer des paires de valeurs correspondantes de w et b.
# zip(w, b) retournera une séquence de tuples : (w[0], b[0]), (w[1], b[1]), etc.
for ww, bb in zip(w, b):
    # Calculer un score particulier en utilisant la formule donnée :
    # (100 - p) * ww + p * bb.
    # Cette formule combine ww et bb en fonction de la valeur de p.
    # Ajouter le résultat de ce calcul à la fin de la liste s.
    s.append((100 - p) * ww + p * bb)

# Trier la liste s en place dans l'ordre décroissant.
# Ceci signifie que le plus grand élément sera au début de la liste.
# La fonction sort modifie la liste s directement (en place).
s.sort(reverse=True)

# Calcul du score initial.
# sum(b) calcul la somme de tous les éléments dans la liste b (c-à-d tous les bb lus précédemment).
# On multiplie cette somme par p, puis on change son signe (donc score = -p * somme des b).
score = -sum(b) * p

# Initialiser un compteur à 0.
# Ce compteur va compter combien d'éléments on aura besoin pour rendre le score positif ou nul.
cnt = 0

# Tant que le score est strictement inférieur à 0,
# on exécutera les instructions à l'intérieur de la boucle while.
while score < 0:
    # Ajouter à score la valeur s[cnt], c'est-à-dire le cnt-ième plus grand score dans s.
    score += s[cnt]
    # Incrémenter le compteur cnt de 1.
    cnt += 1

# Afficher la valeur finale de cnt (le nombre minimal d'éléments pris pour rendre le score non-négatif).
print(cnt)

# (100-p)*w-p*b>=0
# Ce commentaire indique probablement la condition à vérifier/utiliser dans le contexte du problème.
# Cela signifie que, pour que le score individuel soit non-négatif, l'expression (100-p)*w-p*b doit être supérieure ou égale à zéro.