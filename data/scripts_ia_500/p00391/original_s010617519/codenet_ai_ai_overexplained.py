import sys  # Importe le module sys qui permet d'interagir avec l'interpréteur Python notamment pour la gestion des entrées/sorties
import heapq  # Importe le module heapq qui fournit des fonctions pour manipuler des tas (heaps), structures de données optimisées pour récupérer rapidement l'élément minimum

# Lecture des entrées standard (stdin), on récupère 3 lignes
# Pour chaque ligne, on scinde la chaîne en une liste de chaînes sur les espaces
# Puis on convertit uniquement les éléments différents de '0' en entiers négatifs
# Le résultat est une liste de 3 listes, dont nous extrayons la deuxième et la troisième dans a et q
_, a, q = [[-int(e) for e in sys.stdin.readline().split() if e != '0'] for _ in [0]*3]

# Transformation de la liste q en un tas (min-heap), pour permettre des opérations efficaces
heapq.heapify(q)

# Pour chaque élément e dans la liste a...
for e in a:
    t = []  # Initialisation d'une liste temporaire vide qui va stocker certains éléments modifiés de q
    # On itère -e fois (puisque e est négatif, -e est positif) pour autant de répétitions que la valeur absolue de e
    for _ in [0]*-e:
        # Si le tas q est vide, cela signifie qu'on ne peut plus extraire d'éléments, on affiche 0 et termine le programme
        if not q:
            print(0)
            exit()
        # On regarde l'élément minimum dans q sans le retirer : q[0] est le plus petit élément du tas
        # Si cet élément n'est pas égal à -1, on ajoute dans la liste temporaire la valeur q[0]+1 via heappush
        # L'opération q[0]+1 revient à augmenter la valeur négative en la rendant moins négative (donc +1)
        if q[0] != -1:
            heapq.heappush(t, q[0] + 1)
        # On retire l'élément minimum du tas q avec heappop
        heapq.heappop(q)
    # Une fois la boucle intérieure terminée, on remet tous les éléments de la liste temporaire t dans le tas q
    # Pour cela, tant que t n'est pas vide, on insère l'élément minimum de t dans q et le supprime de t
    # Note: bien que ce soit un peu inefficace, on utilise t comme un autre tas pour garder l'ordre
    while t:
        heapq.heappush(q, t[0])  # Ajoute le plus petit élément de t dans q
        heapq.heappop(t)         # Supprime le plus petit élément de t

# Après avoir traité tous les éléments de a, on affiche 1 si q est vide, sinon 0
# int(not q) évalue à 1 si q est une liste vide (False évalué en booléen), sinon 0
print(int(not q))