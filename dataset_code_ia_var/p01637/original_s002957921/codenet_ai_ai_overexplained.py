# Définition de la fonction f avec trois paramètres a, b, c
def f(a, b, c):
    # Calcul : multiplie a et b, puis vérifie si le résultat est inférieur à 100 fois c
    # 'a*b' fait la multiplication des deux premiers arguments
    # '100*c' multiplie le troisième argument par 100
    # '<' vérifie si le produit de 'a' et 'b' est strictement inférieur au résultat de '100*c'
    # La fonction retourne True si l'inégalité est vérifiée, sinon False
    return a * b < 100 * c

# Lecture de l'entrée utilisateur
# 'input()' lit une ligne entrée par l'utilisateur sous la forme d'une chaîne de caractères
# 'split()' coupe la chaîne en une liste de sous-chaînes divisées par des espaces
# 'map(int, ...)' convertit chaque sous-chaîne de la liste en un entier
# 'm, rd, rr, cd, cr = ...' affecte ces cinq entiers respectivement aux variables m, rd, rr, cd, cr
m, rd, rr, cd, cr = map(int, input().split())

# Calcul de la variable ex :
# On veut calculer le nombre minimal d'essais nécessaires pour satisfaire à une certaine condition pour 'cd' et 'rd'
# 'cd * 100' multiplie la variable cd par 100
# '//' effectue une division entière, qui donne le quotient sans la partie décimale
# 'cd * 100 // rd' donne le nombre d'essais ex, c'est-à-dire combien de fois on peut faire 'rd' dans 'cd*100'
ex = cd * 100 // rd

# Vérification si le résultat ne satisfait pas encore la condition souhaitée
# Appel de la fonction f avec les arguments (ex, rd, cd)
# Si f(ex, rd, cd) renvoie True, cela signifie que la condition n'est pas remplie
# Dans ce cas, on augmente ex de 1 pour s'assurer que la condition soit justement satisfaite
if f(ex, rd, cd):
    # Ajout de 1 à ex si la condition n'est pas remplie
    ex += 1

# Calcul de la variable ey :
# Même principe que pour ex, mais appliqué à 'cr' et 'rr'
# On veut le nombre minimal d'essais pour 'cr' et 'rr'
ey = cr * 100 // rr

# Vérification de la condition pour ey, rr, cr
# Si la fonction f(ey, rr, cr) renvoie True, la condition n'est pas remplie
# Dans ce cas, on ajoute 1 à ey pour garantir la satisfaction
if f(ey, rr, cr):
    ey += 1

# Calcul du résultat final
# 'm - ex - ey' calcule la quantité restante après soustraction de ex et ey à m
# 'if m - ex - ey >= 0 else -1' vérifie si le résultat est positif ou nul
# Si oui, on affiche ce résultat, sinon, on affiche -1 pour signaler une condition d'échec
print(m - ex - ey if m - ex - ey >= 0 else -1)