# Demande à l'utilisateur de saisir un nombre entier et stocke la valeur dans la variable n.
# 'n' représente la taille des listes que nous allons créer plus loin.
n = int(input())

# Prend une ligne d'entrée, la découpe en éléments séparés par des espaces,
# convertit chaque élément en entier puis les place dans une liste appelée 'b'.
b = list(map(int, input().split()))

# Crée une liste 'ope' contenant n listes vides.
# Chaque sous-liste sera utilisée pour stocker des indices relatifs à des opérations spécifiques plus tard.
ope = [[] for i in range(n)]

# Prend la prochaine entrée utilisateur en tant que nombre entier 'Q'.
# 'Q' représente le nombre de requêtes ou d'opérations sur des intervalles que nous allons traiter.
Q = int(input())

# Boucle qui s'exécute Q fois pour recevoir les paires (l, r) représentant des intervalles (bornes inclusives 1-indexées).
for i in range(Q):
    # Prend une ligne d'entrée et décompose le contenu en deux entiers l et r.
    l, r = map(int, input().split())
    # Ajoute l-1 (décrément pour passer de l'indexation 1 à 0) à la liste corresponding à r-1 (idem) dans 'ope'.
    ope[r-1].append(l-1)

# Calcule combien de fois la valeur 0 apparaît dans la liste b
# et stocke le résultat dans la variable res.
res = b.count(0)

# Construit la liste 'Data' de taille n, contenant tous les éléments égaux à 1 si b[i]==0, sinon -1.
# On utilise l'expression (-1) ** ((b[i]==1)+1), soit (-1)**(2) quand b[i]==1 (donne 1), (-1)**(1) quand b[i]==0 (donne -1).
Data = [(-1) ** ((b[i] == 1) + 1) for i in range(n)]

# Transforme 'Data' en un tableau de sommes cumulées (prefix sums).
for i in range(1, n):
    # Pour chaque élément (autre que le premier), ajoute la valeur cumulée de l'élément précédent.
    Data[i] += Data[i-1]

# Préfixe la liste 'Data' d'un zéro pour des questions d'alignement d'indices.
Data = [0] + Data

# Trie chaque sous-liste 'ope[i]' du plus grand au plus petit 
# afin de traiter plus facilement certaines opérations ultérieures.
for i in range(n):
    ope[i].sort(reverse=True)

# --- Préparation de la structure de données de type segment tree ---

# Définit N comme la taille utilisée pour les opérations ultérieures sur ce segment tree.
N = n + 1

# Calcule la plus petite puissance de deux supérieure ou égale à N, pour la taille du segment tree.
# Le segment tree fonctionne plus efficacement si sa taille est une puissance de deux.
N0 = 2 ** (N - 1).bit_length()

# Crée la liste 'data' avec 2*N0 éléments initialisés à None.
# Cette liste représentera le segment tree, chaque élément pourra contenir une paire (timestamp, value)
# ou None si aucune valeur n'est assignée.
data = [None] * (2 * N0)

# Définit une constante 'INF' comme étant un couple de très petites valeurs négatives
# utilisées comme valeurs initiales pour la comparaison.
INF = (-2 ** 31, -2 ** 31)

# Fonction pour mettre à jour le segment tree sur un intervalle [l, r) en assignant la valeur v
# ici, v est un tuple (timestamp, valeur)
def update(l, r, v):
    # Décale les indices de l'intervalle pour pointer sur le segment tree interne.
    L = l + N0
    R = r + N0
    # Boucle tant qu'il reste des éléments à mettre à jour.
    while L < R:
        # Si R est impair (fin d'intervalle non alignée), décrémente R,
        # puis traite l'élément R-1.
        if R & 1:
            R -= 1
            # Si data[R-1] existe déjà, prend le max entre la valeur existante et v,
            # sinon assigne la nouvelle valeur v.
            if data[R-1]:
                data[R-1] = max(v, data[R-1])
            else:
                data[R-1] = v
        # Si L est impair (début d'intervalle non alignée), traite L-1 puis incrémente L.
        if L & 1:
            if data[L-1]:
                data[L-1] = max(v, data[L-1])
            else:
                data[L-1] = v
            L += 1
        # Passe au niveau supérieur dans l'arbre.
        L >>= 1
        R >>= 1

# Fonction interne pour rechercher la valeur la plus récente (plus grand timestamp) affectée à la case k du segment tree.
def _query(k):
    # Décale l'index k pour pointer sur la feuille correspondante du segment tree.
    k += N0 - 1
    # Initialise la variable de retour s à INF, qui servira de valeur minimale.
    s = INF
    # Remonte l'arbre jusqu'à la racine.
    while k >= 0:
        # Si une valeur existe à ce niveau, prend le maximum entre s et la valeur présente.
        if data[k]:
            s = max(s, data[k])
        # Passe au parent de ce noeud dans le segment tree.
        k = (k - 1) // 2
    # Retourne la paire (timestamp, valeur) trouvée.
    return s

# Fonction utilisateur pour récupérer la valeur associée à la case k (ignore le timestamp).
def query(k):
    return _query(k)[1]

# Initialise le segment tree en effectuant une première mise à jour pour chaque position de 0 à n inclus.
for i in range(n + 1):
    # La valeur assignée est (-(Data[i]), -(Data[i]))
    # On prend l'opposé car on veut affecter les plus grands timestamps en premier.
    update(i, i + 1, (-Data[i], -Data[i]))

# Si la première case de ope contient au moins un élément (donc il existe une opération concernant tout débutant à 1),
# on effectue une mise à jour supplémentaire spécifique entre 1 et 2 (sur l'élément d'indice 1).
if ope[0]:
    update(1, 2, (0, 0))

# Boucle sur toutes les positions de 1 à n-1 pour effectuer les différentes opérations de mise à jour.
for i in range(1, n):
    # Récupère la valeur courante à la position i dans le segment tree.
    val = query(i)
    # Met à jour la position i+1 avec la valeur ajustée en fonction des valeurs cumulées Data.
    update(i + 1, i + 2, (val + Data[i] - Data[i + 1], val + Data[i] - Data[i + 1]))
    # Pour chaque début d'intervalle l dans la liste ope[i] (ce sont les indices l liés à la borne droite i),
    # on propage la valeur trouvée à la case l+1 vers toutes les cases de l+1 à i+1 inclus.
    for l in ope[i]:
        val = query(l)
        update(l + 1, i + 2, (val, val))

# Affiche le résultat final : soustrait de n la somme du nombre de zéros (stockés dans res),
# la valeur finale à la dernière position du segment tree (query(n)),
# et la dernière valeur de Data (somme cumulée).
print(n - (res + query(n) + Data[n]))