# Importation du module 'fractions' qui fournit des opérations mathématiques pour les fractions.
from fractions import gcd  # La fonction gcd calcule le plus grand commun diviseur de deux nombres entiers.
# Remarque : dans les versions récentes de Python, il est préférable d'utiliser math.gcd, car fractions.gcd est obsolète.

# Définition d'une fonction pour calculer le plus petit commun multiple (LCM) de deux entiers x et y.
def lcm_base(x, y):
    # Multiplie x et y ensemble, puis divise par leur PGCD (Greatest Common Divisor) pour obtenir le PPCM (Least Common Multiple)
    # L'opération // effectue une division entière.
    return (x * y) // gcd(x, y)

# Définition d'une fonction pour calculer le PPCM de plusieurs entiers stockés dans un itérable appelé 'numbers'.
def lcm(numbers):
    t = 1  # Initialise la valeur du PPCM à 1 au début.
    for n in numbers:  # Itère à travers chaque élément 'n' de la liste 'numbers'.
        t = lcm_base(t, n)  # Met à jour la valeur de 't' avec le PPCM actuel et le prochain nombre de la liste.
    return t  # Renvoie le PPCM de tous les nombres.

# Lit l'entrée utilisateur et la convertit en entier. Représente le nombre d'éléments dans la liste A.
N = int(input())  # input() lit une ligne en tant que chaîne de caractères ; int() convertit cette chaîne en entier.

# Lit une deuxième ligne d'entrée, la divise en morceaux (split()) et convertit chaque morceau en entier.
A = [int(x) for x in input().split()]  # Utilise une compréhension de liste pour traiter chaque élément séparé par un espace.

# Définit une variable 'mod' avec la valeur 10^9 + 7, un nombre premier fréquemment utilisé pour prendre des modulo dans les problèmes de programmation.
mod = 10 ** 9 + 7  # Cela évite les débordements d'entiers lors de calculs avec de grands nombres.

ans = 0  # Initialise la variable de réponse à 0. Elle contiendra le résultat final.

# Calcule le PPCM de tous les éléments de la liste 'A' et le stocke dans 't'.
t = lcm(A)

# Met à jour la valeur de 't' en prenant son reste modulo 'mod'.
t %= mod  # Évite que 't' ne dépasse la valeur du module.

# Boucle pour traiter chaque élément de la liste A à l'aide de son indice.
for i in range(N):
    # Calcule la somme modulo 'mod' en ajoutant, pour chaque élément, t multiplié par l'inverse multiplicatif de A[i].
    # pow(A[i], mod-2, mod) est l'inverse multiplicatif de A[i] modulo mod (utilise le petit théorème de Fermat car mod est premier).
    # La multiplication est faite sous modulo mod pour garder la valeur sous une limite raisonnable et pour la correction mathématique.
    ans = (ans + t * pow(A[i], mod - 2, mod)) % mod  # Ajoute la contribution de l'élément courant au résultat.

# Affiche la valeur finale calculée dans 'ans'.
print(ans)  # print() affiche une sortie à l'utilisateur.