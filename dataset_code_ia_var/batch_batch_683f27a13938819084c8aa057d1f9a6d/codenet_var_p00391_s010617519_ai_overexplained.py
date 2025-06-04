import sys  # On importe le module sys qui permet d'accéder à certains objets utilisés ou maintenus par l'interpréteur, ici pour lire l'entrée standard (stdin)
import heapq  # On importe le module heapq, qui fournit une implémentation de la structure de données heap (file de priorité), ici pour manipuler une file de priorité min

# Lecture de trois lignes d'entrée à partir de l'entrée standard. 
# Pour chacune des trois lignes, on lit la ligne, on la découpe en morceaux (split),
# puis on convertit chaque élément en entier négatif tant que cet élément n'est pas la chaîne "0".
# La compréhension de liste produit trois sous-listes contenant ces entiers négatifs, affectés respectivement à _, a et q.
# L'utilisation de la variable '_' ici indique que la première liste n'est pas utilisée par la suite.
_, a, q = [
    [
        -int(e)  # On convertit chaque élément en entier, on le négativise (pour obtenir un max-heap lors de l'usage ultérieur de heapq)
        for e in sys.stdin.readline().split()  # On lit la ligne et on découpe chaque mot/nombre sur les espaces
        if e != '0'  # On ignore les éléments qui valent '0'
    ]
    for _ in [0] * 3  # On répète l'opération trois fois pour lire trois lignes d'entrée
]

# On transforme la liste q en un heap (une file de priorité)
heapq.heapify(q)  # Cela réorganise la liste q pour en faire un 'heap' utilisable avec heapq,
# qui sera par défaut un min-heap en Python. Ici, on a stocké les valeurs négatives pour simuler un max-heap.

# On parcourt chacun des éléments e de la liste a
for e in a:
    # On crée une liste temporaire vide qui va servir à stocker certains éléments
    t = []
    # On exécute une boucle autant de fois que la valeur absolue de e (puisque e est négatif)
    for _ in [0] * -e:
        # Si la liste 'q' est vide (donc s'il n'y a plus d'éléments dans le heap),
        # on affiche '0' puis on termine immédiatement le programme avec exit()
        if not q:
            print(0)
            exit()
        # Si le plus petit élément du heap (qui correspond au plus grand initial, vu le signe)
        # n'est pas égal à -1 (= 1 à l'origine avant la conversion), alors...
        if q[0] != -1:
            # On ajoute à la liste temporaire t la valeur q[0] + 1.
            # Cela correspond à décrémenter l'entier original (puisque stocké sous forme négative)
            heapq.heappush(t, q[0] + 1)
        # On retire la racine du heap q, c'est-à-dire le plus petit élément (valeur la plus grande initialement)
        heapq.heappop(q)
    # Après la boucle, s'il y a des éléments temporaires dans t, 
    # on les réinsère dans le heap q, un par un, en utilisant heappush pour maintenir la propriété du heap.
    while t:
        # On ajoute le premier élément de t dans q
        heapq.heappush(q, t[0])
        # Puis on retire cet élément de t en supprimant le premier élément
        heapq.heappop(t)
# Après avoir traité tous les éléments de a, 
# on affiche le résultat qui est 1 si 'q' est vide (donc toutes les opérations ont réussi), 0 sinon
# 'not q' est True si q est vide, et False sinon, donc int(not q) donne 1 ou 0
print(int(not q))