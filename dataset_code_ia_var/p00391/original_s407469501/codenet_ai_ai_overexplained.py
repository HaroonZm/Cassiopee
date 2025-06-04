import sys  # Importe le module sys qui permet d'accéder à certains objets utilisés ou maintenus par l'interpréteur Python, ici pour utiliser sys.stdin
import heapq  # Importe le module heapq qui permet d'utiliser les files de priorité, aussi appelées tas (heap en anglais)

# On lit trois lignes de l'entrée standard (sys.stdin).
# Pour chaque ligne, on effectue les opérations suivantes :
#  - On lit la ligne avec sys.stdin.readline(), qui renverra une chaîne de caractères terminée par un retour à la ligne.
#  - On découpe la chaîne en éléments séparés par un espace grâce à .split().
#  - Pour chaque sous-chaine (élément) obtenue :
#     - On vérifie que cet élément n'est pas '0' (chaîne représentant le chiffre zéro).
#     - Si ce n'est pas '0', on convertit cet élément en entier avec int(e), puis on multiplie par -1 (pour inverser le signe) afin de stocker sa valeur opposée.
#  - À la fin, pour chaque ligne, on obtient une liste de nombres entiers négatifs (ou positifs, selon la valeur initiale).
#  - On effectue cette opération trois fois, stockant chaque liste résultante dans _, a, q respectivement.
_, a, q = [[-int(e) for e in sys.stdin.readline().split() if e != '0'] for _ in [0]*3]

# On transforme la liste q en un tas (heap), structure permettant d'extraire rapidement la plus petite valeur.
# heapq.heapify() convertit la liste q en tas en temps linéaire.
heapq.heapify(q)

# On parcourt chaque élément e dans la liste a (qui sont des entiers négatifs ou positifs selon l'entrée).
for e in a:
    t = []  # On initialise une liste vide t qui va temporairement contenir des éléments à remettre dans le tas.

    # On crée une boucle qui va se répéter -e fois (puisque e est négatif, -e est positif).
    # L'expression [0]*-e crée une liste contenant -e zéros, et la boucle for _ in [0]*-e parcourt cette liste.
    for _ in [0]*-e:
        # Si la liste représentée par le tas q est vide (aucun élément), on affiche 0 puis on arrête brutalement l'exécution du script par exit().
        if not q:
            print(0)
            exit()
        # Si le plus petit élément du tas n'est pas égal à -1,
        # alors on ajoute 1 à sa valeur (q[0]+1),
        # puis on l'insère dans la liste temporaire t en la fin de liste avec .heappush().
        # On note ici que heapq.heappush(t, x) ajoute un élément dans t et maintient la propriété de tas de t.
        if q[0] != -1:
            heapq.heappush(t, q[0]+1)
        # Ensuite, on enlève le plus petit élément du tas q avec heapq.heappop(q).
        # Cette opération retire et renvoie le plus petit élément du tas, c'est-à-dire l'élément à l'indice 0.
        heapq.heappop(q)

    # Après la fin de la boucle interne, on remet tous les éléments de t dans le tas q.
    # Ceci est fait avec une boucle while tant qu'il y a des éléments dans t :
    while t:
        # On prend le plus petit élément de t (car c'est un tas également, même si souvent il contient peu d'éléments),
        # et on l'insère dans q afin de maintenir la propriété de tas.
        heapq.heappush(q, t[0])
        # On retire également cet élément de t avec heapq.heappop(t).
        heapq.heappop(t)

# Après avoir traité tous les éléments de la liste a, on examine la liste q.
# Si q est vide (tous ses éléments ont été consommés/retirés), alors not q est vrai (True, car une liste vide est évaluée comme False).
# On convertit ce booléen (not q) en entier avec int().
# True devient 1 et False devient 0.
# Ainsi, on affiche 1 si q est vide, sinon 0.
print(int(not q))