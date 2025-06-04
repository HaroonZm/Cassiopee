# Le programme commence par lire l'entrée :
# 'open(0)' ouvre le flux d'entrée standard (stdin)
# 'map(int, open(0))' applique la fonction int à chaque ligne lue de stdin
# en convertissant chaque ligne en entier.
N, *E = map(int, open(0))  # N est le premier nombre, E est la liste des nombres suivants

# On initialise deux variables :
a, c = 1, 0  # 'a' est initialisé à 1, il sert d'accumulateur du résultat, 'c' sera un compteur

# On va préparer une liste de tuples pour la suite de la logique.
# Elle contient, pour chaque valeur de E avec son index :
#  - le nombre 'e' de E 
#  - un indicateur 'd' qui vaut 1 si l'index i < N, sinon -1.
# La compréhension de listes suivante le réalise :
# - 'enumerate(E)' associe à chaque élément de E son index i
# - '2*(i<N)-1' produit 1 si i < N (car 2*True - 1 = 2 - 1 = 1), sinon -1.
# - On regroupe chaque (e, d) dans un tuple, aboutissant à une liste.
pairs = [(e, 2 * (i < N) - 1) for i, e in enumerate(E)]  # Pour chaque E, calcule (e, d)

# On trie cette liste de tuples selon la valeur de 'e' croissant,
# cela veut dire qu'on va parcourir les évènements dans l'ordre croissant de 'e'.
for _, d in sorted(pairs):  # On ignore la valeur 'e' en assignant à '_', on n'utilise que 'd'
    # À chaque étape :
    # On vérifie si c * d < 0 :
    #  - Si c était positif et d est négatif (ou inversement), le produit est négatif (<0)
    #  - Cela désigne un changement de signe de 'c' si on ajoute 'd' à 'c'.
    if c * d < 0:
        # Si ce changement se produit, alors :
        # On multiplie 'a' par la valeur absolue de 'c'
        # Puis on prend le résultat modulo 10**9 + 7 (pour éviter les débordements)
        a = abs(a * c) % (10**9 + 7)
    # On incrémente 'c' par 'd'
    c += d

# Lorsque toutes les itérations sont terminées, on affiche la valeur finale de 'a'.
print(a)  # Affiche le résultat final