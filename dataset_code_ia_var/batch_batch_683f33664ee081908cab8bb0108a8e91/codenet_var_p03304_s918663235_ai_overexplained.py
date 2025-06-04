# Importation du module numpy, couramment utilisé pour le calcul numérique et la manipulation de tableaux multidimensionnels, bien que dans ce code il n'est pas utilisé explicitement
import numpy as np

# Importation du module collections avec l'alias 'col'; il s'agit d'un module fournissant des types de données de conteneurs spécialisés.
# Cependant, ici, il n'est pas utilisé non plus, mais reste souvent pratique dans d'autres contextes.
import collections as col

# Importation du module math qui offre des fonctions mathématiques de base telles que sqrt, sin, log, etc.
# Dans ce script, il n'est actuellement pas utilisé, mais il est maintenu pour potentielle utilisation.
import math

# Lecture de trois entiers séparés par des espaces depuis l'entrée standard (input utilisateur).
# La méthode 'input()' lit une ligne de texte; 'split()' sépare cette ligne en une liste de chaînes selon les espaces.
# 'map(int, ...)' convertit chaque chaîne de la liste en un entier.
# Enfin, les trois valeurs sont affectées aux variables n, m et d, respectivement.
n, m, d = map(int, input().split())

# Initialisation de la variable 'ans' avec la valeur flottante 0.0.
# Cela servira à stocker le résultat de calcul, qui sera potentiellement modifié plus loin.
ans = 0.0

# Vérification de la condition selon laquelle d est égal à zéro à l'aide d'une instruction if.
if d == 0:
    # Si 'd' est zéro, alors le résultat 'ans' est calculé comme le quotient du nombre (m - 1) et de n.
    # (m - 1) signifie que l'on considère toutes les valeurs jusqu'à (m - 1) inclus, excluant m.
    # Le résultat est converti en nombre flottant en raison de la division.
    ans = (m - 1)/n
else:
    # Sinon (c'est-à-dire si 'd' n'est pas égal à zéro), on effectue un autre calcul.
    # On multiplie 2.0 (un flottant avec valeur 2), par (n - d), qui représente la différence entre n et d,
    # multiplié par (m - 1), puis on divise le tout par n au carré (n * n).
    # Ce calcul pourrait représenter une probabilité ou un comptage, selon le contexte spécifique du problème.
    ans = 2.0 * (n - d) * (m - 1) / n / n

# Les deux lignes suivantes, précédées de '#', sont des commentaires et donc inactives.
# Elles semblent montrer une variante du calcul selon les valeurs de 'd' mais n'influencent pas l'exécution du code.
# if d == 0:
#     ans = (n - 1)*(m - 1)/n/n
# else:
#     ans = (n - 1)*(m - 1)/n/n/n * 2.0 * (n - d) * (m - 1)

# Affichage sur la sortie standard de la valeur finale calculée et stockée dans 'ans'.
# La fonction 'print()' affiche la valeur et saute à la ligne suivante automatiquement.
print(ans)