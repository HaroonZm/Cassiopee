# Demande à l'utilisateur d'entrer deux entiers séparés par un espace
# "input()" lit une ligne du terminal, "split()" sépare la ligne en deux parties selon l'espace
# "map(int, ...)" convertit chaque partie en entier
n, p = map(int, input().split())

# Initialise une liste vide pour stocker les paires d'entiers
# On utilise une compréhension de liste pour répéter l'opération "n" fois
# À chaque itération, on lit une ligne, on la découpe, on convertit chaque morceau en entier puis on forme un tuple (w, b)
# On regroupe tous ces tuples dans une liste appelée "e"
e = [tuple(map(int, input().split())) for _ in range(n)]
# À ce stade, "e" est une liste de n tuples. Chaque tuple représente deux entiers (w, b)

# On prépare une liste où chaque élément est la valeur calculée à partir d'un tuple (w, b)
# Pour chaque élément de la liste e, donc chaque tuple (w, b),
# on calcule: (100 - p) * w + p * b
# Le résultat de cette expression est collecté dans une nouvelle liste temporaire par compréhension génératrice
# On trie cette liste de valeurs par ordre décroissant grâce à "sorted(..., reverse=True)"
# Puis on stocke le résultat trié dans la variable e2
e2 = sorted(((100 - p) * w + p * b for w, b in e), reverse=True)

# On calcule une somme initiale appelée "rest"
# On parcourt tous les tuples (w, b) de la liste e
# On extrait seulement le deuxième élément "b" dans chaque tuple
# On fait la somme totale de tous les "b" puis on multiplie ce nombre par "p"
# La variable "rest" va servir à suivre une quantité qu'on essaiera de réduire jusqu'à 0 plus loin
rest = p * sum(b for _, b in e)

# On initialise une variable compteur "cur" à zéro. Elle servira à compter le nombre d'itérations réalisées plus loin.
cur = 0

# On entre dans une boucle "while" qui continue tant que deux conditions sont vraies :
# 1) "rest" est strictement supérieur à zéro (donc il reste quelque chose à soustraire)
# 2) "cur" (le compteur courant) est strictement inférieur à n (on reste dans les limites de la liste)
while rest > 0 and cur < n:
    # À chaque itération, on soustrait la valeur e2[cur] à "rest"
    # Cela fait diminuer la valeur de "rest"
    rest -= e2[cur]
    # On incrémente "cur" de 1, pour passer à l'élément suivant de la liste
    cur += 1

# Quand la boucle se termine (soit rest <= 0 soit cur >= n),
# on affiche la dernière valeur de "cur" ainsi obtenue
# "print(cur)" affiche le résultat à l'écran
print(cur)