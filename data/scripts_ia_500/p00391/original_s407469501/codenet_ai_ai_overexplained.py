import sys  # Importation du module 'sys' pour accéder aux entrées/sorties standard et autres fonctionnalités système
import heapq  # Importation du module 'heapq' qui permet de manipuler une file de priorité (tas binaire)

# Lecture et transformation des données d'entrée :
# Nous allons lire trois lignes depuis l'entrée standard (sys.stdin.readline()),
# puis pour chaque ligne, convertir chaque élément en int en inversant son signe (-int(e)),
# mais uniquement si cet élément n'est pas la chaîne '0' (filtrage des '0').
# Le résultat est une liste de listes contenant ces entiers négatifs.
# L'underscore '_' est utilisé pour ignorer la première liste,
# puis 'a' et 'q' récupèrent respectivement la deuxième et troisième liste correspondantes à ces transformations.
_, a, q = [[-int(e) for e in sys.stdin.readline().split() if e != '0'] for _ in [0] * 3]

# Transformation de la liste 'q' en un tas binaire (heap)
# Un tas binaire permet d'accéder efficacement à l'élément minimum (ici, le plus petit entier négatif).
heapq.heapify(q)

# Pour chaque élément 'e' dans la liste 'a', on effectue un traitement suivant
for e in a:
    t = []  # Initialisation d'une liste temporaire 't', qui servira de tas temporaire

    # Boucle exécutée '-e' fois (car 'e' est négatif, on inverse le signe ici)
    # Le but est d'effectuer un certain nombre d'opérations sur le tas 'q'
    for _ in [0] * -e:
        # Si le tas 'q' est vide (aucun élément), cela signifie que l'opération est impossible
        # On affiche alors 0 puis on termine immédiatement le programme avec exit()
        if not q:
            print(0)
            exit()

        # Si le premier élément du tas 'q' (le plus petit élément) n'est pas égal à -1,
        # on ajoute dans le tas temporaire 't' cet élément augmenté de 1 (c'est-à-dire moins négatif, donc +1)
        # heapq.heappush ajoute un élément dans la structure en maintenant l'ordre du tas.
        if q[0] != -1:
            heapq.heappush(t, q[0] + 1)

        # Suppression de l'élément minimum du tas 'q' avec heappop (retire et retourne le plus petit élément du tas)
        heapq.heappop(q)

    # Après avoir traité '-e' éléments, on remet les éléments du tas temporaire 't' dans 'q'
    # Tant que 't' contient des éléments:
    while t:
        # On déplace l'élément minimum de 't' vers 'q' en le poussant d'abord dans 'q'
        heapq.heappush(q, t[0])
        # Puis on le retire de 't' pour avancer dans la liste 't' jusqu'à la vider
        heapq.heappop(t)

# Après avoir traité tous les éléments de 'a', on affiche :
# int(not q) 
# Le 'not q' est True si 'q' est vide (pas d'éléments restants), sinon False
# int(True) vaut 1 et int(False) vaut 0
# Donc ce print affichera 1 si 'q' est vide, sinon 0
print(int(not q))