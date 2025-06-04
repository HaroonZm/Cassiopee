import sys  # Importe le module sys qui fournit l'accès à certaines variables et fonctions propres à l'interpréteur Python

# Redéfinit la fonction input pour utiliser sys.stdin.readline, 
# ce qui permet de lire une ligne depuis l'entrée standard (clavier, fichier, etc.)
# Cela peut être plus rapide que la fonction input() classique pour de grands volumes de données.
input = sys.stdin.readline

# Modifie la limite de récursion de Python (le nombre de fois qu'une fonction peut s'appeler elle-même)
# La valeur ici est 10 puissance 7, soit 10 millions, ce qui est très élevé.
# Cela peut être utile pour les programmes qui utilisent beaucoup de récursion pour éviter l'erreur "maximum recursion depth exceeded".
sys.setrecursionlimit(10 ** 7)

# Importe la fonction gcd (greatest common divisor, c'est-à-dire le plus grand commun diviseur)
# depuis le module fractions (NB : dans les versions récentes de Python, on devrait utiliser math.gcd).
# Cela permet de calculer le PGCD de deux nombres entiers, c'est-à-dire le plus grand entier qui divise à la fois les deux nombres.
from fractions import gcd

# Lit une ligne depuis l'entrée standard, la découpe (split) en éléments séparés par des espaces,
# puis transforme chaque élément en entier grâce à map(int, ...).
# Les quatre valeurs sont ensuite affectées respectivement aux variables A, B, C, et D, grâce à l'affectation multiple.
A, B, C, D = map(int, input().split())

# Calcule la différence absolue entre A et C et l'affecte à la variable dx.
# abs(x) retourne la valeur absolue de x, c'est-à-dire la distance à zéro sans tenir compte du signe.
# Cela signifie que dx sera toujours positif ou nul.
dx = abs(A - C)

# Même chose que ci-dessus, mais cette fois entre B et D. La valeur absolue est stockée dans dy.
dy = abs(B - D)

# Calcule le plus grand commun diviseur (gcd) entre dx et dy.
# Cela permet de déterminer la plus grande valeur entière qui divise à la fois dx et dy sans reste.
g = gcd(dx, dy)

# Calcule la valeur finale appelée answer.
# Cela correspond à la somme de dx et dy, à laquelle on retire g.
# L'expression "(dx + dy)" additionne les distances absolues sur les axes x et y,
# puis on retranche le pgcd des deux distances pour obtenir le résultat souhaité.
answer = (dx + dy) - g

# Affiche le résultat final, c'est-à-dire la valeur de la variable answer, sur la sortie standard (généralement l'écran).
print(answer)