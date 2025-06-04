import sys  # Importe le module sys qui fournit l'accès à certaines variables et fonctions propres à l'interpréteur Python

# Définit des raccourcis pour la lecture sur l'entrée standard en mode "buffer". Cela permet de lire les entrées plus rapidement,
# particulièrement lorsque l'on traite de gros volumes de données ou que l'on participe à des concours de programmation compétitifs.

read = sys.stdin.buffer.read      # Lis tout le flux d'entrée sous forme binaire (bytes)
readline = sys.stdin.buffer.readline  # Lis une seule ligne depuis l'entrée standard en mode binaire
readlines = sys.stdin.buffer.readlines  # Lis toutes les lignes d'entrée à la fois en les stockant dans une liste

# Définit la limite maximale de récursion à une grande valeur (10**7, soit 10 millions)
# Cela permet d'éviter les erreurs de récursion maximale lorsque le code effectue des appels récursifs profonds
sys.setrecursionlimit(10 ** 7)

# Importe la fonction bisect_left du module bisect.
# Cette fonction permet de trouver l'indice où insérer un élément dans une liste triée afin de conserver l'ordre trié.
from bisect import bisect_left

# Importe la fonction accumulate du module itertools.
# Cette fonction renvoie un accumulateur (i.e., la somme cumulative ou une autre opération binaire) sur un iterable.
from itertools import accumulate

# Lis la première ligne d'entrée (qui est un nombre entier) et la convertit en un int, puis le stocke dans la variable n.
n = int(readline())

# Lis la deuxième ligne depuis l'entrée standard, la découpe en éléments (en utilisant split, qui sépare sur les espaces), 
# convertit chaque élément en int grâce à map, en fait une liste, puis la trie par ordre croissant.
# Résultat stocké dans la variable a.
a = sorted(list(map(int, readline().split())))

# Répète la même opération pour la troisième ligne, stockée dans la variable b.
b = sorted(list(map(int, readline().split())))

# Idem pour la quatrième ligne, stockée dans la variable c.
c = sorted(list(map(int, readline().split())))

# Initialise une liste de vérification ('check') de longueur n remplie de zéros.
# Cette liste va servir à stocker, pour chaque élément de b, le nombre d'éléments dans c qui lui sont strictement supérieurs.
check = [0] * n

# Initialise l'accumulateur pour la réponse finale à zéro.
ans = 0

# Parcourt tous les indices possibles de la liste b, c'est-à-dire de 0 à n-1.
for i in range(n):
    # Recherche l'indice dans c où l'on pourrait insérer b[i] pour garder c triée.
    # 'bisect_left' retourne le premier indice où b[i] pourrait être inséré sans violer l'ordre. 
    index = bisect_left(c, b[i])
    # Si index n'est pas à la fin du tableau c (c'est-à-dire s'il existe au moins un élément restant dans c)
    if index != n:
        # Si c[index] est exactement égal à b[i], cela signifie qu'il existe une ou plusieurs occurrences de b[i] dans c à cet indice ou plus loin.
        # Comme nous voulons seulement les éléments strictement supérieurs (`>`), nous cherchons l'indice du premier élément STRICTEMENT plus grand que b[i].
        if c[index] == b[i]:
            # On recherche donc l'indice où b[i]+1 pourrait être inséré, ce qui reviendra à ignorer toutes les occurrences de b[i] dans c.
            index = bisect_left(c, b[i] + 1)
    # Le nombre d'éléments dans c avec une valeur STRICTEMENT supérieure à b[i] est donc n - index.
    check[i] = n - index

# Calcule la liste des sommes cumulées (prefix sums) à partir de la liste check, mais on la renverse d'abord (check[::-1])
# Ceci est fait car dans la suite, on s'intéresse à des sous-tableaux à partir de la droite.
# On ajoute 0 au début de la liste cumulée afin d'aligner les indices plus aisément.
cumsum = [0] + list(accumulate(check[::-1]))

# Pour chaque élément aa dans la liste a (qui est triée), on va calculer combien il existe de couples (b, c) tels que:
# b est STRICTEMENT supérieur à aa, et pour ce b, comptez combien il y a de c STRICTEMENT supérieur à b.
for aa in a:
    # Cherche l'indice où aa pourrait être inséré dans b de manière ordonnée, i.e., l'indice du premier élément >= aa.
    index = bisect_left(b, aa)
    # Si ce n'est pas à la fin de b
    if index != n:
        # Si l'élément trouvé est égal à aa, il faut aller à la première valeur STRICTEMENT supérieure à aa dans b.
        if b[index] == aa:
            index = bisect_left(b, aa + 1)
    # Ajoute à la réponse le nombre de façons de choisir (b, c) pour ce aa.
    # Comme cumsum contient des préfix sums inversées, on récupère cumsum[n - index], soit la somme cumulée correspondant à tous les b restants.
    ans += cumsum[n - index]

# Affiche le résultat final: le nombre total de triplets (a, b, c) satisfaisant les conditions demandées.
print(ans)