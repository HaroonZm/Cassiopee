# Demander à l'utilisateur de saisir un entier qui sera stocké dans la variable n
n = int(input())  # n : nombre d'éléments dans la séquence
# Lire une ligne de nombres séparés par des espaces, la convertir en liste d'entiers, puis y ajouter un zéro à la fin
a = list(map(int, input().split())) + [0]  # Liste contenant les éléments a et un zéro en dernière position
# Lire la seconde ligne de nombres, la convertir en liste d'entiers, puis y ajouter aussi un zéro
b = list(map(int, input().split())) + [0]  # Liste contenant les éléments b et un zéro en dernière position

# Boucle sur chaque indice de 0 à n-1 inclus
for i in range(n):
    # Pour l'élément d'indice n (le dernier, ajouté avant), on applique un XOR avec les éléments précédents de a
    a[n] ^= a[i]  # a[n] = a[n] XOR a[i] (inversion de bits, utile pour propriétés sur la parité des collections)
    b[n] ^= b[i]  # b[n] = b[n] XOR b[i] (même logique pour b)

# Créer deux nouvelles listes na et nb correspondant aux versions triées des listes a et b
na = sorted(a)  # Trie la liste a par ordre croissant (nouvelle liste)
nb = sorted(b)  # Trie la liste b par ordre croissant (nouvelle liste)
# Vérifie si les deux listes triées sont différentes
if na != nb:
    print("-1")  # Si elles sont différentes, il n'est pas possible de transformer a en b, donc affiche -1
    exit()       # Quitte immédiatement le programme

# Crée un dictionnaire vide pour la structure d'ensemble disjoint (Union-Find)
f = dict()

# Déclare une fonction permettant de trouver le "représentant" (racine) d'un élément x dans l'ensemble
def find(x):
    # Si x pointe vers lui-même dans le dictionnaire f, alors il est le représentant de son ensemble
    if f[x] == x:
        return x  # Retourne x comme racine
    else:
        # Si ce n'est pas le cas, cherche récursivement le représentant de f[x]
        # En même temps, optimise la structure pour pointer directement vers la racine (compression de chemin)
        f[x] = find(f[x])
        return f[x]

# Initialise la variable ans qui servira à compter le nombre d'opérations nécessaires
ans = 0

# Parcoure tous les indices de 0 à n-1
for i in range(n):
    # Si les éléments a[i] et b[i] sont différents à la même position
    if a[i] != b[i]:
        # On initialise f[a[i]] pour qu'il pointe vers lui-même, créant ainsi son propre ensemble
        f[a[i]] = a[i]

# Pour l'élément ajouté à la fin de la liste, on l'initialise également dans le dictionnaire f
f[a[n]] = a[n]

# À nouveau, on parcourt tous les indices de 0 à n-1 inclus
for i in range(n):
    # Si les éléments a[i] et b[i] diffèrent
    if a[i] != b[i]:
        ans += 1        # On augmente le compteur car il faudra au moins une opération de plus
        # On effectue l'union : on lie l'ensemble contenant b[i] à l'ensemble contenant a[i]
        f[find(b[i])] = find(a[i])

# Parcourt tous les éléments présents comme clés dans le dictionnaire f
for i in f:
    # Si i est toujours le représentant (racine) de son propre ensemble
    if i == f[i]:
        ans += 1        # On incrémente le nombre d'opérations car chaque ensemble racine représente une composante distincte

# On affiche le résultat final, diminué de 1 (l'algorithme, selon la structure, demande de soustraire 1 à la fin)
print(ans - 1)  # Affiche le nombre minimum d'opérations nécessaires pour transformer a en b