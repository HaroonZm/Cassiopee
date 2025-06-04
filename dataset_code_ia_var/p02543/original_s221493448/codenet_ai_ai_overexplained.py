import sys  # Importe le module sys, qui fournit l'accès à certaines variables utilisées ou maintenues par l'interpréteur
readline = sys.stdin.readline  # Définit 'readline' comme un raccourci vers 'sys.stdin.readline', pour lire plus rapidement les entrées ligne par ligne

INF = 10**18 + 3  # Un nombre considéré comme "infiniment grand" pour ce problème afin d'éviter les dépassements de limites lors de comparaisons

N, K = map(int, input().split())  # Lit deux entiers de l'entrée standard ; N = nombre d'éléments dans la liste, K = la valeur de différence minimale souhaitée
X = list(map(int, readline().split())) + [INF]  # Lit une ligne d'entiers, les convertit en liste, puis ajoute 'INF' à la fin pour éviter des erreurs d'index hors bornes

left = [None] * N  # Crée une liste de taille N remplie de None pour stocker des couples utiles plus tard
r = 0  # Initialise un pointeur 'r' à 0 pour l'utiliser comme index de fenêtre glissante

# Pour chaque élément à l'indice i de la liste X, on cherche le plus grand indice r tel que X[r+1] - X[i] < K 
for i in range(N):
    while r < N and X[r+1] - X[i] < K:  # Déplace le pointeur 'r' tant que la différence reste strictement inférieure à K
        r += 1  # Incrémente r pour élargir la fenêtre
    left[i] = (r, i)  # Stocke un tuple (r, i) dans left à la position i. 'r' est le dernier index qui vérifie la condition, 'i' garde la trace de l'indice d'origine

left = [left]  # Place la liste 'left' dans une liste pour simuler des "niveaux" (utiles pour la technique du saut binaire plus tard)
nb = N.bit_length()  # nb = nombre de bits nécessaires pour représenter N; utilisé pour déterminer le nombre de niveaux de saut binaire

# Construction des niveaux de la table de saut binaire pour accélérer les requêtes ultérieures
for _ in range(nb):
    res = [None] * N  # Nouvelle liste de résultats pour le niveau courant
    for idx in range(N):
        r, i = left[-1][idx]  # Prend la dernière valeur (r, i) du niveau précédent pour 'idx'
        if r >= N - 1:  # Si le nouvel index dépasse le tableau, affecte une valeur hors limite
            res[idx] = (N, None)
        else:
            r1, i1 = left[-1][r+1]  # Cherche le résultat du prochain niveau pour r+1
            if r1 == N:
                res[idx] = (N, None)
            else:
                res[idx] = (r1, i + i1)  # Stocke le cumul des indices parcourus lors des sauts
    left.append(res)  # Ajoute ce nouveau niveau à la liste 'left'

# Construction équivalente que précédemment, mais cette fois pour sauter vers la gauche
right = [None] * N  # Même approche : liste de tuples
l = N - 1  # Initialise un pointeur 'l' à la fin du tableau

for i in range(N-1, -1, -1):  # On part de la fin du tableau vers le début
    while 0 < l and X[i] - X[l-1] < K:  # Tant que la différence reste inférieure à K, on réduit 'l'
        l -= 1
    right[i] = (l, i)  # Stocke le tuple (l, i) dans 'right'
right = [right]  # Place dans une structure à niveaux comme pour 'left'

# Construction des niveaux de saut binaire pour le côté gauche (right)
for _ in range(nb):
    res = [None] * N  # Nouvelle liste pour le niveau courant
    for idx in range(N):
        l, i = right[-1][idx]  # Prend la valeur précédente
        if l <= 0:  # Si on sort du tableau à gauche
            res[idx] = (-1, None)
        else:
            l1, i1 = right[-1][l-1]  # Prend la valeur du prochain niveau pour l-1
            if l1 == -1:
                res[idx] = (-1, None)
            else:
                res[idx] = (l1, i + i1)  # Stocke les informations cumulées
    right.append(res)  # Ajoute ce niveau à la structure

Q = int(readline())  # Lit un entier Q signifiant le nombre de requêtes
Ans = [None] * Q  # Initialise la liste des réponses, de longueur Q, remplie de None

# Pour chaque requête, on effectue les calculs nécessaires
for qu in range(Q):
    l, r = map(int, readline().split())  # Lit deux entiers correspondants à la requête (indices de la sous-séquence à traiter)
    l -= 1  # Convertit l'indice à une base 0 (commence à zéro)
    
    vn = l  # Initialise la variable 'vn' au point de départ de la fenêtre
    li = 0  # Accumulateur pour compter (ou sommer) lors du parcours vers la droite
    ml = 0  # Compteur pour le nombre de "sauts" effectués vers la droite
    for j in range(nb-1, -1, -1):  # Parcourt les niveaux de saut binaire du plus grand au plus petit
        vf, ix = left[j][vn]  # Récupère le résultat du niveau j à la position 'vn'
        if vf < r:  # Vérifie si le saut ne dépasse pas la frontière droite de la requête
            vn = vf + 1  # Avance 'vn' au prochain point juste après le saut
            li += ix  # Incrémente l'accumulateur des indices traversés (sert à compter le nombre total d'indices visités)
            ml += 1 << j  # Fait un saut de 2^j en termes de pas (car on utilise saut binaire)
        if vn >= r:  # Quand on a dépassé ou atteint la frontière, on stoppe les sauts
            break
    if vn < r:  # Si après les sauts on n'a pas fini, il reste un pas à faire pour compléter
        ml += 1
        li += vn  # On ajoute le dernier indice

    l -= 1  # Préparation pour le parcours en sens inverse, conversion vers base 0, ou ajustement pour indices
    r -= 1

    vn = r  # Cette fois on démarre du bord droit de l'intervalle
    ri = 0  # Accumulateur pour le parcours vers la gauche
    mr = 0  # Compteur de sauts vers la gauche
    for j in range(nb-1, -1, -1):  # Même logique que précédemment mais dans l'autre sens
        vf, ix = right[j][vn]  # Récupère le résultat du niveau j
        if l < vf:  # Si on ne dépasse pas la frontière gauche
            vn = vf - 1  # Recule de un après le saut
            ri += ix  # Incrémente la somme des indices
            mr += 1 << j  # Additionne les sauts (taille de saut binaire correspondant au niveau j)
        if vn <= l:  # Quand on a atteint ou dépassé la frontière, on s'arrête
            break
    if l < vn:  # Si on doit faire un dernier pas
        mr += 1
        ri += vn  # On ajoute le dernier indice parcouru

    Ans[qu] = ri - li + ml  # Calcule la réponse finale pour la requête courante (soustraction des indices cumulés, ajustée par ml)

# Après avoir traité toutes les requêtes, on affiche les réponses, chacune sur une ligne
print('\n'.join(map(str, Ans)))  # Transforme chaque élément de Ans en chaîne de caractères puis les affiche séparés par des retours à la ligne