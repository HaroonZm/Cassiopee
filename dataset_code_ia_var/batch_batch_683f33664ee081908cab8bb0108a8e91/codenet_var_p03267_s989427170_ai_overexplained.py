# Demande à l'utilisateur de saisir un entier par le biais d'une entrée standard
# La fonction input() recueille une ligne saisie par l'utilisateur sous forme de chaîne de caractères.
# int() convertit cette chaîne en un entier. La valeur obtenue sera stockée dans la variable L.
L = int(input())

# Déclare une liste vide qui contiendra des tuples représentant les arêtes d'un graphe.
# Chaque élément ajouté à 'edges' sera une arête décrite par trois entiers (départ, arrivée, poids).
edges = []

# Initialise deux variables, p2 et N, à la valeur 1.
# p2 servira à conserver une puissance de 2 (initialement 2^0).
# N va indiquer le nombre actuel de sommets (noeuds) dans le graphe, en partant de 1.
p2 = 1
N = 1

# La chaîne de commentaire suivante décrit, dans une autre langue (japonais),
# qu'à chaque étape pour chaque puissance de 2, des arêtes multiples sont construites.
""" 2べきのとき多重辺
   0     0     0     0  ...
1 === 2 === 3 === 4 === 5 ...
   1     2     4     8  ...
"""

# Cette boucle ajoutera des arêtes correspondant aux puissances de 2 <= L.
# La boucle while continue tant que p2 * 2 (soit la prochaine puissance de 2) est inférieur ou égal à L.
while L >= p2 * 2:
    # Incrémente N de 1 à chaque itération, ce qui correspond à ajouter un nouveau sommet au graphe.
    N += 1
    # Multiplie p2 par 2 pour obtenir la prochaine puissance de 2.
    p2 *= 2
    # Ajoute une arête (N - 1, N, 0) : reliant le nœud précédent (N-1) au nœud courant (N) avec un poids 0.
    edges.append((N - 1, N, 0))
    # Ajoute également une arête (N - 1, N, 2**(N-2)), c'est-à-dire une arête parallèle avec un poids équivalent à la puissance de 2 correspondante.
    # 2**(N-2) : car N a été incrémenté, pour correspondre à la bonne puissance de 2 on utilise N-2 (exemple : pour N=2, poids=1 ; pour N=3, poids=2, etc.).
    edges.append((N - 1, N, 2 ** (N - 2)))

# Une fois la boucle terminée, p2 contient la plus grande puissance de 2 telle que p2 <= L.
# 'rest' est la quantité qu'il reste à atteindre pour L, soit L - p2.
rest = L - p2
# On crée une variable temporaire 'tmp' initialisée à p2.
# Elle permettra de calculer les poids pour construire le reste du chemin.
tmp = p2

# Cette boucle for parcourt les puissances de 2 de N vers 0, c'est-à-dire du sommet N jusqu'au sommet 0 inclus.
# range(N, -1, -1) produit les valeurs N, N-1, ..., 0 (en décrémentant de 1 à chaque étape).
for i in range(N, -1, -1):
    # (rest >> i) & 1 permet de vérifier si le i-ème bit de la variable resta est à 1.
    # Cela correspond à savoir si la puissance de 2^i doit être incluse pour atteindre la somme L.
    if (rest >> i) & 1:
        # Si ce bit est présent (égal à 1), on ajoute une arête du sommet i+1 vers N avec un poids égal à la valeur de 'tmp'.
        # Cela correspond à exploiter la route du sommet correspondant à la puissance de 2^i pour faire la somme vers L.
        edges.append((i + 1, N, tmp))
        # Ajoute la puissance de 2^i à tmp pour les prochaines arêtes éventuelles.
        tmp += 2 ** i

# Détermine le nombre total d'arêtes créées en prenant la longueur de la liste d'arêtes.
M = len(edges)

# Les contraintes sont telles que le nombre de sommets N doit être inférieur ou égal à 20 et le nombre d'arêtes M inférieur ou égal à 60 (selon le commentaire original).
# Ici, rien n'empêche cela mais une assertion aurait pu être utilisée pour vérifier.

# Affiche le nombre total de sommets N suivi du nombre total d'arêtes M sur une même ligne, séparés par un espace.
print(N, M)

# Pour chaque arête stockée dans la liste edges :
for edge in edges:
    # Décompacte le tuple 'edge' et affiche ses trois composantes sur une même ligne, séparées par des espaces.
    # L'étoile (*) permet d'étendre le tuple pour que chaque valeur soit un argument individuel pour print(), produisant ainsi 'départ arrivée poids'.
    print(*edge)