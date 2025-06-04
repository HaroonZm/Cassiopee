import sys                          # Le module sys fournit un accès direct à certaines variables et fonctions liées à l'interpréteur Python.
from collections import Counter, defaultdict  # Importe la classe Counter (compte les occurrences d’éléments) et defaultdict (dictionnaire avec valeurs par défaut).

INF = float('inf')                  # Affecte à la variable INF la valeur de l’infini flottant, utilisé souvent pour l’initialisation de comparaisons.
MOD = 10 ** 9 + 7                   # Définit une constante MOD à 1 000 000 007, couramment utilisée pour la prise de reste afin d’éviter les débordements.

# Définition d’une fonction LI (List Input), qui lit une ligne depuis l’entrée standard, la découpe selon les espaces,
# puis convertit chaque morceau en entier, et renvoie la liste des entiers obtenus.
def LI():
    return [int(x) for x in sys.stdin.readline().split()]

# Définition d’une fonction LI_ qui fait la même chose que LI, mais soustrait 1 à chaque entier lu,
# utilisé typiquement pour gérer des indices commençant à 1 dans l’entrée, mais à 0 en Python.
def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

# Définition d’une fonction LS (List String) qui lit une ligne de texte depuis l’entrée,
# la découpe selon les espaces, et retourne la liste de chaînes ainsi formées.
def LS():
    return sys.stdin.readline().split()

# Définition d’une fonction II (Integer Input), qui lit simplement une ligne depuis l’entrée standard
# et la convertit directement en un entier, puis le retourne.
def II():
    return int(sys.stdin.readline())

# Définition d’une fonction SI (String Input) qui utilise simplement la fonction input() pour lire une ligne de texte.
def SI():
    return input()

n = II()                            # Lit un entier depuis l’entrée standard et le stocke dans la variable n.

a, b = LI()                         # Lit deux entiers depuis la prochaine ligne de l’entrée et les stocke respectivement dans a et b.

m = II()                            # Lit un nouvel entier, m, qui sera utilisé comme nombre d’itérations ou nombre d’éléments à traiter.

D = defaultdict(int)                # Crée un dictionnaire spécial où toute clé absente renverra 0 par défaut.

# Démarre une boucle qui s’exécutera m fois, allant de 0 à m-1 (c’est-à-dire m itérations exactement).
for i in range(m):
    x, y, z = LI()                  # Lit trois entiers depuis la ligne courante de l’entrée ; les stocke dans x, y, et z respectivement.
    y -= 1                          # Décrémente y de 1, pour convertir un indice 1-based en 0-based pour le traitement Python.
    z -= 1                          # Même opération pour z.
    # Si y se trouve déjà comme une clé dans le dictionnaire D, tmp_y prendra la valeur D[y] (c’est-à-dire la valeur associée à y dans D).
    # Sinon (si y n’a jamais été utilisé avant), tmp_y prend la valeur calculée par la formule a + b * y.
    tmp_y = D[y] if y in D.keys() else a + b * y
    # De même pour z : on récupère D[z] si z existe comme clé, sinon la valeur par défaut calculée.
    tmp_z = D[z] if z in D.keys() else a + b * z
    # Si x vaut 0 (c’est-à-dire si la condition est vraie), alors on affecte la valeur tmp_y à la clé z dans le dictionnaire D.
    if x == 0:
        D[z] = tmp_y

    # Quel que soit x, on affecte la valeur tmp_z à la clé y dans D (mise à jour directe).
    D[y] = tmp_z

k = II()                            # Lit un entier depuis l’entrée et le stocke dans la variable k.
k -= 1                              # Décrémente k de 1 pour passer en index 0-based.

# Affiche la valeur correspondant à la clé k dans D si elle existe.
# Sinon (si k n’a jamais été défini/écrasé dans D lors de la boucle),
# affiche la valeur par défaut calculée par la formule a + b * k.
print(D[k] if k in D.keys() else a + b * k)