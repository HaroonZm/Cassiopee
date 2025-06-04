# Lire la première ligne d'entrée, contenant n (le nombre de positions) et m (le nombre d'éléments)
# map(int, input().split()) lit l'entrée standard (input()), sépare la chaîne sur les espaces (split()),
# puis convertit chaque partie en entier (int). Cela renvoie un itérable de deux éléments
n, m = map(int, input().split())

# Lire la deuxième ligne d'entrée, contenant m entiers
# map(int, input().split()) convertit chaque valeur en entier, list(...) les empaquette dans une liste
a = list(map(int, input().split()))

# Initialiser la variable 'pre' avec la première valeur de la liste a.
# Ceci va représenter la position précédente lors de notre itération.
pre = a[0]

# Initialiser la variable 'd' à zéro. Celle-ci va garder la valeur la plus grande trouvée pendant la boucle.
# Plus précisément, d représentera l'écart maximum entre deux positions consécutives dans 'a'
d = 0

# Boucle for pour parcourir le reste des éléments dans la liste 'a', en commençant par le second élément (a[1:])
# 'x' va représenter chaque élément actuel dans la liste (excepté le premier élément déjà utilisé dans 'pre')
for x in a[1:]:
    # Calculer la différence entre l'élément courant 'x' et 'pre' (l'élément précédent)
    # 'max(d, x-pre)' va choisir la valeur maximale entre la valeur de 'd' déjà trouvée et celle nouvellement calculée (x-pre)
    d = max(d, x-pre)
    # Mettre à jour 'pre' pour qu'il reflète l'élément courant pour la prochaine itération
    pre = x

# Après la boucle, 'd' contient donc le plus grand écart entre deux positions consécutives de 'a'
# 'pre' contient la dernière valeur de 'a'

# Calculer le résultat complexe demandé :
# - n-pre : calculer l'écart entre la dernière position et la fin (le bord droit)
# - d >> 1 : fait un décalage à droite (division entière par 2), donc la moitié de la distance maximale entre deux personnes
# - a[0]-1 : position du premier élément moins 1, soit l'espace entre le bord gauche et la première personne
# - max(d>>1, a[0]-1) : prendre la moitié de la plus grande distance interne OU la distance entre le début et le premier élément, laquelle est la plus grande
# Enfin, on prend le plus grand entre n-pre (bord droit), ou la plus grande distance calculée précédemment
print(max(n-pre, max(d>>1, a[0]-1)))