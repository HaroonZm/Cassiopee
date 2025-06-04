import sys  # Importe le module système pour pouvoir utiliser sys.exit et définir la limite de récursion

# Définit la limite maximale de la profondeur de la récursion.
# Cela signifie que la fonction récursive peut être appelée jusqu'à 10^6 fois avant de déclencher une erreur.
sys.setrecursionlimit(10**6)

# Récupère le nombre entier n depuis l'entrée standard (l'utilisateur ou un fichier d'entrée).
# input() lit une ligne sous forme de chaîne, int() convertit cette chaîne en nombre entier.
n = int(input())

# Prend la ligne suivante de l'entrée standard, la découpe en morceaux grâce à split() (qui utilise l'espace par défaut),
# puis map() convertit chaque morceau en entier via int(). Enfin, list() forme cette séquence en une liste d'entiers.
p = list(map(int, input().split()))

# Crée une liste de listes vide pour enregistrer les enfants de chaque nœud dans l'arbre. 
# Pour chaque nœud, c[i] est la liste des enfants de ce nœud.
c = [[] for _ in range(n)]

# Crée une liste is_leaf de valeurs True, indiquant que chaque nœud est initialement supposé être une feuille.
is_leaf = [True for _ in range(n)]

# Parcourt tous les indices des nœuds (de 0 à n-1 inclusive)
for i in range(n):
    # Les indices dans p sont probablement 1-indexés (commencent à 1) donc on enlève 1 pour le rendre 0-indexé
    p[i] -= 1

    # Ajoute le nœud courant (i) à la liste des enfants de son parent dans c.
    # Cela construit l'arbre sous forme de liste d'adjacence.
    c[p[i]].append(i)

    # Déclare que le parent de ce nœud (p[i]) n'est pas une feuille (c'est donc un nœud interne)
    is_leaf[p[i]] = False

# Vérifie si le nombre total de feuilles dans l'arbre est zéro
if sum(is_leaf) == 0:
    # Si aucun nœud n'est une feuille

    # Si le nombre total de nœuds est pair (divisible par 2), le problème est considéré possible
    if n % 2 == 0:
        print("POSSIBLE")
    else:
        # Sinon, on affiche "IMPOSSIBLE"
        print("IMPOSSIBLE")
    # Quitte immédiatement le programme (aucun code sous-jacent ne sera exécuté)
    sys.exit()

# Cherche le premier nœud qui est une feuille (is_leaf[i] == True) et mémorise son indice dans cur
for i in range(n):
    if is_leaf[i]:
        cur = i
        break  # On arrête dès qu'on en trouve une

# Déclare un ensemble visited_set contenant juste la feuille trouvée (début du parcours de la boucle)
visited_set = {cur}

# Déclare une liste visited_list pour suivre l'ordre de visite, initialisée avec la feuille
visited_list = [cur]

# Boucle pour suivre la chaîne des parents jusqu'à trouver un cycle (un nœud déjà visité)
while p[cur] not in visited_set:
    # Ajoute le parent courant à la liste et à l'ensemble des visités
    visited_list.append(p[cur])
    visited_set.add(p[cur])

    # Continue à remonter dans l'arbre en allant de cur à son parent
    cur = p[cur]

# À la fin de cette boucle, cur pointe sur un nœud dont le parent est déjà visité : c'est une boucle
root = p[cur]  # Le début de la boucle, qu'on appelle root par la suite

# Prépare une liste grundy initialisée à -1 (signifie valeur non calculée)
# grundy[i] représentera la valeur de Grundy du nœud i, pour la théorie des jeux (Nimbers)
grundy = [-1 for _ in range(n)]

# Prépare une liste de sets vides pour chaque nœud, afin de stocker les valeurs de Grundy de ses enfants
g_set = [set() for _ in range(n)]

# Définit une fonction récursive dfs (parcours en profondeur) pour calculer les valeurs de Grundy
def dfs(x):
    # Initialise la valeur de retour res à 0 (la plus petite valeur possible pour un mex)
    res = 0

    # Parcourt tous les enfants du nœud x
    for v in c[x]:
        # Applique récursivement dfs sur l'enfant v (calcul de la valeur de Grundy pour v)
        dfs(v)
        # Ajoute la valeur de Grundy de l'enfant à l'ensemble associé au nœud x
        g_set[x].add(grundy[v])

    # Cherche la plus petite valeur entière non présente dans g_set[x] (mex, minimum excluded value)
    # Si res appartient déjà à l'ensemble, on l'incrémente pour trouver la suivante
    while res in g_set[x]:
        res += 1
    # La valeur de Grundy de x est ce mex
    grundy[x] = res
    return res  # Retourne la valeur pour appel éventuel

# Crée une liste loop de booléens (indiquant si le nœud fait partie de la boucle)
loop = [False for _ in range(n)]

# Marque le début de la boucle comme faisant partie de la boucle
loop[root] = True

# Commence à la fin de la visited_list pour remonter jusqu'à root
ind = len(visited_list) - 1

# Remonte la liste jusqu'à ce qu'on rencontre le nœud root, en marquant chaque nœud comme étant dans la boucle
while visited_list[ind] != root:
    loop[visited_list[ind]] = True
    ind -= 1  # Recule dans la liste

# Pour chaque nœud du graphe (de 0 à n-1 inclus)
for i in range(n):
    # Si ce nœud est dans la boucle
    if loop[i]:
        # Pour chacun de ses enfants
        for x in c[i]:
            # Si l'enfant n'est pas dans la boucle (un sous-arbre "hors-cercle")
            if not loop[x]:
                # Calcule la valeur de Grundy du sous-arbre
                dfs(x)
                # Ajoute cette valeur à l'ensemble Grundy du nœud dans la boucle
                g_set[i].add(grundy[x])

# Prépare une liste cand pour stocker les deux premières valeurs mex disponibles au niveau du root
cand = []

# Initialise num à 0 avant de chercher le mex
num = 0

# Incrémente num tant qu'il fait partie des valeurs Grundy des enfants de la racine
while num in g_set[root]:
    num += 1
# Ajoute ce mex comme première valeur candidate
cand.append(num)
num += 1
# Trouve à nouveau une deuxième valeur mex à partir de la suivante possible
while num in g_set[root]:
    num += 1
cand.append(num)  # Ajoute la deuxième valeur candidate

# Pour chacune des deux valeurs candidates trouvées
for x in cand:
    cur = root
    grundy[root] = x  # Attribue la valeur candidate à la racine

    # Exécute une boucle pour propager la valeur Grundy dans la boucle
    while True:
        num = 0  # Initialise num à 0 pour rechercher un mex
        # Incrémente num tant qu'il est soit dans l'ensemble des valeurs des enfants du parent,
        # soit égal à la valeur courante pour éviter de refaire la même
        while num in g_set[p[cur]] or num == grundy[cur]:
            num += 1
        grundy[p[cur]] = num  # Attribue cette valeur au parent

        if p[cur] == root:
            break  # Si on a fait le tour de la boucle, on arrête
        cur = p[cur]  # Avance le long de la boucle

    # Si après propagation, la racine possède toujours la valeur candidate, c'est possible
    if grundy[root] == x:
        #print(grundy)  # (ligne commentée : affiche les valeurs de Grundy)
        print("POSSIBLE")  # Affiche que c'est réalisable
        sys.exit()  # Arrête le programme car on a trouvé une réponse

# Si aucune des possibilités testées ne marche, alors c'est impossible
print("IMPOSSIBLE")  # Affiche l'impossibilité