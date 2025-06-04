import bisect  # On importe le module bisect qui permet d'effectuer des recherches binaires dans des listes triées.

# On lit l'entrée standard. La fonction input() lit une ligne depuis le clavier.
# On découpe la ligne en morceaux (split()), on convertit chaque morceau en entier (map(int, ...)),
# puis on assigne les valeurs respectivement à n, Q, L et R.
n, Q, L, R = map(int, input().split())

# On lit la ligne suivante depuis l'entrée standard, la découpe en morceaux,
# transforme chaque morceau en entier, puis range ces entiers dans une liste appelée 'a'.
a = list(map(int, input().split()))

# On trie la liste 'a' en ordre croissant.
a.sort()

# On prépare une liste vide 'p' pour stocker les Q requêtes, qui vont chacune être un tuple de quatre entiers.
p = []
for i in range(Q):  # On répète Q fois, une fois pour chaque requête.
    # On lit une ligne, on convertit tous ses éléments en entiers, puis on place les 4 dans un tuple.
    # Le tuple est ensuite ajouté à la liste 'p'.
    p.append(tuple(map(int, input().split())))

# On définit une fonction f qui prend un paramètre z.
def f(z):
    # La fonction parcours chaque requête dans la liste 'p'.
    for q, x, s, t in p:
        # Si le premier élément (q) de la requête vaut 1 :
        if q == 1:
            # Si la valeur courante z est supérieure ou égale à x :
            if z >= x:
                # On remplace z par t multiplié par (z + s).
                z = t * (z + s)
        else:
            # Si q vaut autre chose que 1 (donc ici forcément 2, vu le contexte) :
            # On vérifie si z est inférieur ou égal à x :
            if z <= x:
                # Si z - s est strictement négatif :
                if z - s < 0:
                    # On prend la valeur absolue de (z-s), on la divise entière par t, puis on ajoute un signe négatif.
                    # Cela équivaut à un arrondi par défaut pour les valeurs négatives.
                    z = -(abs(z - s) // t)
                else:
                    # Sinon (z-s est positif ou nul) : on effectue une division entière par t.
                    z = (z - s) // t
    # À la fin de toutes les requêtes, on retourne la valeur finale de z.
    return z

# Pour faire une recherche binaire, on définit deux bornes : 'ng' (négatif, ici le maximum possible)
# et 'ok' qui sera initialement à -ng.
ng = pow(2, 63)  # Calcul 2 puissance 63, c'est un grand nombre pour servir de borne supérieure.
ok = -ng         # La borne inférieure, négatif de ng.

# On effectue 100 itérations de recherche binaire pour trouver la plus grande valeur ok
# telle que f(ok) <= R.
for i in range(100):
    # On calcule la valeur du milieu entre ok et ng, division entière.
    mid = (ok + ng) // 2
    # Si f(mid) est inférieur ou égal à R, on peut descendre ok vers mid (on accepte cette valeur).
    if f(mid) <= R:
        ok = mid
    else:
        # Sinon, on doit monter ng vers mid (on rejette mid).
        ng = mid

right = ok  # À la fin, 'right' contient le plus grand ok validant la condition.

# On procède pareil pour 'left', mais cette fois pour trouver la plus petite valeur ok
# telle que f(ok) >= L.
ok = pow(2, 63)  # On remet ok à la borne positive maximale possible.
ng = -ok         # ng reprend la grande borne négative.

for i in range(100):  # On répète la recherche binaire 100 fois.
    mid = (ok + ng) // 2  # Même principe : on prend le milieu.
    if f(mid) >= L:  # Si f(mid) est supérieur ou égal à L, c'est une valeur acceptable.
        ok = mid
    else:
        ng = mid

left = ok  # À la fin, left est la borne uniforme minimale qui passe le critère.

# On effectue une recherche dans la liste 'a' (qui est triée) pour déterminer combien d'éléments de 'a'
# appartiennent à l'intervalle [left, right] inclusivement.

# bisect_left trouve la première position dans 'a' où 'left' pourrait être inséré
# pour maintenir l'ordre trié (c'est la borne inférieure incluse).
k1 = bisect.bisect_left(a, left)

# bisect_right trouve la toute première position où 'right' + 1 serait inséré :
# en pratique, ça donne la "borne supérieure exclusive", donc tous les nombres <= right.
k2 = bisect.bisect_right(a, right)

# La différence des deux indices donne le nombre d'éléments dans 'a' qui sont entre left et right inclus.
print(k2 - k1)  # On affiche le résultat final.