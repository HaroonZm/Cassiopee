# Problème résumé :
# On doit produire un graphe G=(V,E) (avec N ≤ 40) où la différence entre la taille de la plus grande
# indépendance (A(G)) et l'espérance de la taille de l'ensemble noir produit par l'algorithme aléatoire de Jiro (E(G))
# est maximale. Le graphe est non orienté, avec les contraintes d'adjacence décrites.
#
# Approche :
# Ce problème étant difficile (NP-difficile), la consigne est de construire un contre-exemple où le
# gap A(G)-E(G) est grand.
# 
# Rappel sur l'algorithme de Jiro:
# - Chaque sommet reçoit un numéro unique aléatoire entre 1 et N.
# - On colore en noir tous les sommets qui ont un numéro plus petit que tous leurs voisins.
# - Les sommets isolés (sans voisins) sont aussi noirs.
# 
# Forte intuition : 
# Le graphe "étoile" (un centre connecté à tous les autres sommets feuilles, qui ne sont pas reliés entre eux)
# est un cas intéressant pour ce problème :
# - Maximum independent set A(G) = N-1 (on peut prendre toutes les feuilles)
# - L'espérance E(G) est la probabilité que la racine ait le numéro le plus petit (alors racine noire seulement) 
#   ou que chaque feuille ait le plus petit par rapport au centre.
# Analyse:
# - Le centre devient noir si son numéro est plus petit que tous les autres (prob = 1/N)
# - La feuille i devient noir si son numéro est plus petit que celle du centre (prob = 1/2)
# Donc :
# E(G) = P(centre noir) * 1 + P(centre blanc) * (nombre de feuilles noires espérées)
#      = (1/N)*1 + ( (N-1)/N ) * ( (N-1)*1/2 ) = 1/N + (N-1)/N * (N-1)/2
#      = 1/N + (N-1)^2/(2N)
# A(G) = N-1
# Calculons la différence (N-1) - E(G),
# Pour N = 40, elle est significative.
#
# Nous allons donc générer ce graphe étoile avec N=40.

def output_star_graph(n=40):
    # Création d'une matrice n x n remplie de 'N'
    # s[i][i] = 'N' (pas de boucle)
    s = [['N']*n for _ in range(n)]
    
    # Le sommet 0 est le centre
    # On met des arêtes entre le centre et tous les autres sommets
    for i in range(1, n):
        s[0][i] = 'Y'
        s[i][0] = 'Y'
    
    # Sortie
    print(n)
    for i in range(n):
        print(''.join(s[i]))

output_star_graph()