from itertools import product  # Importe la fonction 'product' du module 'itertools', qui permet de générer des produits cartésiens d'itérables.

# Utilisation de la fonction 'input' pour lire une ligne depuis l'entrée standard (habituellement le clavier).
# La fonction 'split()' convertit cette chaîne en une liste de sous-chaînes séparées par des espaces.
# La fonction 'map(int, ...)' convertit chaque sous-chaîne en un entier.
# Le résultat est unpacké dans les variables N et M.
N, M = map(int, input().split())

# Création d'une liste 'ABC' qui va contenir N sous-listes, chacune contenant trois entiers.
# On utilise une liste en compréhension pour itérer N fois (i prend les valeurs de 0 à N-1).
# À chaque itération, on lit une ligne, on la découpe en sous-chaînes, on convertit chaque sous-chaîne en un entier, puis on place le résultat dans la sous-liste correspondante.
ABC = [list(map(int, input().split())) for i in range(N)]

# Initialisation de la variable 'ans' à zéro.
# Cette variable servira à garder la valeur maximale trouvée au fil des traitements suivants.
ans = 0

# La boucle suivante utilise 'product' pour générer toutes les combinaisons possibles de signes (-1 et 1) appliqués aux trois coordonnées (x, y, z).
# 'repeat=3' signifie que pour chaque dimension (x, y, z), on considère -1 et 1, soit 2*2*2=8 possibilités au total.
for a, b, c in product([-1, 1], repeat=3):
    # Initialisation d'une liste vide 'score' qui servira à stocker des valeurs calculées pour chaque objet de la liste ABC.
    score = []
    # Pour chaque sous-liste [x, y, z] dans la liste 'ABC', on va appliquer les signes (a, b, c).
    for x, y, z in ABC:
        # On calcule la combinaison pondérée x*a + y*b + z*c pour cet objet.
        # Ceci applique le signe choisi à chaque coordonnée et effectue la somme.
        valeur = x * a + y * b + z * c
        # On ajoute cette valeur (calculée ci-dessus) à la liste 'score'.
        score.append(valeur)
    # On trie la liste 'score' en ordre décroissant pour obtenir les plus grandes valeurs en premier.
    score.sort(reverse=True)
    # On fait la somme des M premiers éléments de la liste 'score' (qui sont les plus grands après le tri).
    somme = sum(score[:M])
    # On met à jour 'ans' pour qu'il garde la plus grande valeur de 'ans' et 'somme'.
    ans = max(ans, somme)

# On affiche la valeur de 'ans', c'est-à-dire la somme maximale trouvée selon les critères du problème.
print(ans)