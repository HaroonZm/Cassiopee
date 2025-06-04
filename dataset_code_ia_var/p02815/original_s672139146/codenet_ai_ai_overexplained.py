# Demande à l'utilisateur d'entrer une valeur entière, puis la stocke dans la variable N.
# input() prend l'entrée standard de l'utilisateur, int() convertit la chaîne en nombre entier.
N = int(input())

# Demande à l'utilisateur de saisir une liste de nombres séparés par des espaces.
# map(int, ...) applique la conversion int à chaque élément de la liste obtenue par input().split().
# list(...) convertit l'itérable map en une liste.
# sorted(..., reverse=True) trie la liste par ordre décroissant.
# La liste triée est stockée dans la variable C.
C = sorted(list(map(int, input().split())), reverse=True)

# Définit une constante 'mod' qui sera utilisée pour calculer des résultats modulo 10**9 + 7,
# ce qui est une grande valeur première souvent utilisée pour éviter les dépassements lors de gros calculs.
mod = 10**9 + 7

# Définition d'une fonction mpow(x, n) qui va calculer (x ** n) modulo 'mod' d'une manière efficace
# utilisant l'exponentiation rapide binaire, plus rapide que d'utiliser x ** n directement.
def mpow(x, n):
    num = 1  # Initialise la variable 'num' à 1, qui sera utilisée pour accumuler le résultat.
    while n > 0:  # Tant que l'exposant n n'est pas nul.
        if n & 1:  # Vérifie si le bit de poids faible de n est égal à 1 (c'est-à-dire si n est impair).
            # Si oui, multiplie num par x et applique l'opération modulo 'mod'.
            num = num * x % mod
        # Met à jour la valeur de x en x * x modulo 'mod' pour la prochaine itération.
        x = x * x % mod
        # Décale tous les bits de n vers la droite d'une position (équivalent à n = n // 2).
        n = n >> 1
    # Retourne le résultat final de la puissance modulaire.
    return num

# Initialise une variable 'count' à 0. Cette variable va servir à accumuler un certain calcul lors de la boucle suivante.
count = 0

# Boucle sur les éléments de la liste C, en utilisant enumerate pour obtenir à la fois l'index (i) et la valeur (c).
# Le second argument de enumerate (c'est-à-dire '2') fait en sorte que le comptage des indices commence à 2 au lieu de 0.
for i, c in enumerate(C, 2):
    # Ajoute à 'count' la valeur de l'élément c multipliée par son index i (i partant de 2).
    count += c * (i)
    # Applique l'opération modulo 'mod' à 'count' après chaque ajout pour éviter les débordements.
    count %= mod

# Calcule le résultat final à afficher :
# - Multiplie 'count' par mpow(2, N-1) (résultat de 2 exposant (N-1) modulo mod).
# - Multiplie encore par mpow(2, N-1), donc au total : count * (2^(N-1)) * (2^(N-1)) % mod.
# - Applique l'opération modulo 'mod' pour rester dans la plage des valeurs possibles.
# - Enfin, affiche le résultat avec print().
print(count * mpow(2, N-1) * mpow(2, N-1) % mod)