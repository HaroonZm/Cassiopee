# Nous allons commencer par lire une ligne de l'entrée utilisateur.
# Cette ligne contiendra plusieurs nombres séparés par des espaces.
# La fonction input() lit une ligne en tant que chaîne de caractères.
# split() sépare cette chaîne en une liste de sous-chaînes, découpées selon les espaces.
# map(int, ...) applique la fonction int à chaque élément de la liste, convertissant chaque sous-chaîne en un entier.
# L'affectation multiple 'a, b, c, d = ...' place chaque valeur convertie dans la variable correspondante.
a, b, c, d = map(int, input().split())

# Ici, nous définissons une fonction anonyme (lambda) pour calculer le PGCD (Plus Grand Commun Diviseur).
# La syntaxe est 'lambda paramètres : valeur de retour'.
# La fonction gcd prend deux entiers a et b.
# Si a est divisible par b (c'est-à-dire si le reste de la division euclidienne a % b == 0),
# alors le PGCD est tout simplement b (la condition 'if a % b else b').
# Sinon (si 'a % b' n'est pas nul), la fonction gcd appelle récursivement elle-même,
# mais cette fois avec les paramètres b et a % b, ce qui correspond à l'algorithme d'Euclide.
gcd = lambda a, b: gcd(b, a % b) if a % b else b

# Définition d'une fonction nommée en japonais (数学は最強也), ce qui signifie ici "Les mathématiques sont les plus fortes".
# Cette fonction prend deux paramètres entiers : a et b.
def 数学は最強也(a, b):
    # Calculer le PGCD des deux valeurs a et b en appelant la fonction gcd définie plus haut.
    q = gcd(a, b)
    # La ligne suivante calcule une valeur basée sur le PGCD.
    # On divise chacun des paramètres a et b par q (leur PGCD),
    # ce qui donne le nombre de "pas" horizontaux et verticaux réduits à leur fraction irréductible.
    # On additionne (a // q) et (b // q - 1),
    # puis on multiplie le résultat par q pour obtenir la valeur finale que retourne la fonction.
    # (a // q) donne combien de fois q "rentre" dans a.
    # (b // q - 1) fait de même pour b, puis enlève 1 à cette quantité.
    # Le résultat de l’addition est multiplié par q pour revenir à l’échelle initiale.
    return q * ((a // q) + (b // q - 1))

# Nous imprimons le résultat de la fonction 数学は最強也 appliquée à deux valeurs calculées à partir des entrées d'origine :
# abs(a - c) calcule la valeur absolue de la différence entre a et c.
# abs(b - d) calcule la valeur absolue de la différence entre b et d.
# Ceci assure d'obtenir toujours une distance positive ou nulle entre a et c, ainsi qu'entre b et d.
# La fonction print affiche le résultat à l'écran sous forme de chaîne de caractères.
print(数学は最強也(abs(a - c), abs(b - d)))