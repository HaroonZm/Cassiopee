# Importe la classe Counter du module collections pour compter efficacement les éléments d'un itérable
from collections import Counter
# Importe la fonction accumulate du module itertools pour calculer la somme cumulative (préfixe) d'une séquence
from itertools import accumulate
# Importe le module sys, utilisé ici pour accéder à sys.stdin pour une lecture rapide des entrées
import sys

# Définit la borne supérieure M pour toutes les opérations suivantes (par exemple, limites des tableaux/supplémentaires)
M = 10**5 + 2  # 100002, ce qui couvrira tous les entiers jusqu'à 100000

# Initialise une liste 'prime' de taille M remplie de zéros.
# L'indice i de cette liste contiendra le plus petit facteur premier de i, ou zéro si encore non attribué.
prime = [0] * M

# Remplit le tableau prime pour tous les entiers de 2 jusqu'à M-1
for i in range(2, M):
    # Si prime[i] n'est pas zéro, cela signifie que i a déjà été identifié comme non premier (marqué dans une itération antérieure)
    if prime[i]:
        continue  # Passe à l'itération suivante
    # Ici, i est encore non marqué, donc il est premier.
    for j in range(i, M, i):
        # Boucle sur tous les multiples de i (c’est-à-dire i, 2i, 3i, ...)
        if not prime[j]:
            # Si ce multiple n'a pas encore été marqué, alors son plus petit facteur premier est i lui-même
            prime[j] = i

# Fonction pd (prime decomposition) : effectue la décomposition en facteurs premiers d'un entier x
def pd(x):
    # Crée un nouvel objet Counter, qui sera utilisé pour compter les puissances des facteurs premiers de x
    C = Counter()
    # Répète tant que x > 1 (c'est-à-dire tant qu'il reste des facteurs premiers à extraire)
    while x > 1:
        # Ajoute 1 à la multiplicité du plus petit facteur premier actuel de x
        C[prime[x]] += 1
        # Réduit x en le divisant par ce facteur premier (élimine ce facteur)
        x //= prime[x]
    # Retourne le Counter final, où chaque clé est un facteur premier et la valeur associée est sa puissance
    return C

# Fonction check : applique des règles pour décider si un entier x satisfait une certaine condition basée sur ses facteurs premiers
def check(x):
    # Extrait la décomposition en facteurs premiers sous forme de Counter
    C = pd(x)
    # Si x a plus de deux facteurs premiers distincts (quelle que soit leur puissance)
    if len(C) > 2:
        return True
    # Si x a exactement un seul facteur premier
    if len(C) == 1:
        # Si la puissance de ce facteur est au moins 4
        if list(C.values())[0] >= 4:
            return True
        return False  # Sinon, la condition n'est pas satisfaite
    # Si x a exactement 2 facteurs premiers, mais qu'ils apparaissent chacun avec une puissance 1
    if all(1 == a for a in C.values()):
        return False  # Condition spécifique qui rend le résultat False
    # Dans tous les autres cas (2 facteurs, mais au moins un avec puissance > 1)
    return True

# Réduit M de 1 pour que la plage des entiers considérés aille exactement jusqu'à 100001
M -= 1

# Construit une table booléenne où, pour chaque entier x de 2 à M-1, table[x] = True ou False selon 'check(x)'
# On commence par deux zéros [0, 0] pour table[0] et table[1], car 0 et 1 ne sont pas traités par la boucle de check(x)
table = [0, 0] + [check(x) for x in range(2, M)]

# Transforme table en une liste de sommes cumulées (préfixes)
# Pour chaque indice q, table[q] donnera le nombre total d'entiers n ≤ q qui satisfont la condition check(n)
table = list(accumulate(table))

# Boucle de traitement des requêtes utilisateur
# 'input()' lit le nombre de requêtes, converti en entier
for _ in range(int(input())):
    # Lit une ligne depuis l'entrée standard (ici sys.stdin.readline est utilisé pour accélérer la lecture sur de grandes entrées)
    q = int(sys.stdin.readline())
    # Affiche le nombre d'entiers n ≤ q qui satisfont la condition de check(n)
    print(table[q])