# Cette fonction inpl() lit une ligne de l'entrée standard, la découpe en morceaux en utilisant les espaces comme séparateurs,
# puis convertit chaque morceau en un entier, créant ainsi une liste d'entiers qu'elle retourne.
def inpl():
    return [int(i) for i in input().split()]

# On lit deux entiers depuis l'entrée standard à l'aide de inpl(), et on les stocke dans les variables N et K.
N, K = inpl()

# On lit la liste des entiers depuis l'entrée standard à l'aide de inpl(), et on la stocke dans la variable a.
a = inpl()

# On crée une nouvelle liste b. Pour chaque élément i de la liste a,
# si i est strictement positif (>0), on ajoute i à b; sinon, on ajoute 0.
# Ainsi, b contient les valeurs positives de a (et zéro aux autres positions).
b = [i if i > 0 else 0 for i in a]

# On crée une nouvelle liste c. Pour chaque élément i de la liste a,
# si i est strictement négatif (<0), on ajoute i à c; sinon, on ajoute 0.
# Ainsi, c contient les valeurs négatives de a (et zéro aux autres positions).
c = [i if i < 0 else 0 for i in a]

# On crée la liste d de taille N-K+1, initialisée avec des zéros.
# Ceci sera utilisé pour stocker, pour chaque sous-intervalle continu de taille K dans a,
# la somme des éléments négatifs (donc la somme des valeurs correspondantes dans c) dans ce sous-intervalle.
d = [0 for _ in range(N - K + 1)]

# On calcule la somme des K premiers éléments de c (c'est-à-dire, la somme des valeurs négatives dans les K premiers éléments de a),
# et on assigne cette somme à d[0], le premier élément de la liste d.
d[0] = sum(c[:K])

# On crée la liste e de taille N-K+1, initialisée avec des zéros.
# Ceci sera utilisé pour stocker, pour chaque sous-intervalle continu de taille K dans a,
# la somme des éléments positifs (donc la somme des valeurs correspondantes dans b) dans ce sous-intervalle.
e = [0 for _ in range(N - K + 1)]

# On calcule la somme des K premiers éléments de b (c'est-à-dire, la somme des valeurs positives dans les K premiers éléments de a),
# et on assigne cette somme à e[0], le premier élément de la liste e.
e[0] = sum(b[:K])

# Pour chaque position possible i de 0 à N-K-1, on effectue une itération :
for i in range(N - K):
    # On met à jour d[i + 1] pour obtenir la somme des valeurs négatives dans le sous-tableau de taille K commençant à l'indice i+1.
    # Pour cela, on retire c[i] de l'ancienne somme (élément qui "sort" de la fenêtre) et on ajoute c[i+K] (élément qui "entre" dans la fenêtre).
    d[i + 1] = d[i] - c[i] + c[i + K]
    # De la même façon, on met à jour e[i+1] pour la somme des valeurs positives dans la nouvelle fenêtre :
    # on retire b[i], on ajoute b[i+K].
    e[i + 1] = e[i] - b[i] + b[i + K]

# On considère trois valeurs pour le résultat final :
# 1. 0 (au cas où toutes les autres options donneraient des nombres négatifs, car on veut au moins zéro)
# 2. sum(b) + max(d) : 
#    sum(b) est la somme totale de toutes les valeurs positives dans a.
#    max(d) est la valeur maximale de somme des éléments négatifs sur un intervalle de taille K.
#    Cette formule correspond au cas où, dans un certain segment de taille K, on change tous les éléments négatifs en positifs (ou on ignore les négatifs).
# 3. sum(b) - min(e) :
#    Ici, min(e) est la plus petite somme des valeurs positives sur un segment de taille K : donc en retirant cette somme du total, 
#    on considère le cas où on enlève les plus gros positifs situés sur un segment de taille K.
# On prend le maximum de ces trois valeurs, qui donne le meilleur score selon les règles implicites du problème.
print(max(
    0,
    sum(b) + max(d),
    sum(b) - min(e)
))