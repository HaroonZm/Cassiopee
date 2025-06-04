from numpy import *  # Importe toutes les fonctions du module numpy dans l'espace de noms courant, ici principalement pour ses types de données et opérations de tableau
from scipy.sparse import *  # Importe toutes les fonctions du module scipy.sparse, utilisé pour représenter des matrices creuses (sparse matrices) efficacement

def main():  # Déclaration de la fonction principale du programme

    # f représentera la fonction Floyd-Warshall, qui calcule les plus courts chemins entre tous les couples de sommets d'un graphe pondéré
    f = csgraph.floyd_warshall

    # Lecture de toute l'entrée depuis stdin. 'open(0)' ouvre le descripteur de fichier 0, qui correspond à l'entrée standard (stdin).
    # 'read()' lit tout d'un coup. 'split()' sépare la chaîne selon les espaces et retours à la ligne.
    # On convertit le tout en un tableau numpy d'entiers 32 bits avec 'int32'.
    t = int32(open(0).read().split())

    # Assignation des 3 premiers nombres lus à n, m, l. 'n' est probablement le nombre de sommets du graphe,
    # 'm' le nombre d'arêtes, et 'l' une limite quelconque (ici, une limite sur la longueur des chemins)
    n, m, l = t[:3]

    # La variable 't' reçoit le reste du tableau, excluant les trois premiers entiers, pour traiter le reste des données (arêtes + requêtes)
    t = t[3:]

    # On multiplie m par 3 car chaque arête du graphe est probablement codée sur 3 entiers (sommet départ, sommet arrivée, poids)
    m *= 3

    # Construction d'une matrice creuse (sparse), qui sera le graphe pondéré à traiter :
    # - Les 'données' de la matrice sont t[2:m:3] c'est-à-dire les poids des arêtes
    # - Les 'lignes' sont les indices des sommets de départ t[:m:3]
    # - Les 'colonnes' sont les indices des sommets d'arrivée t[1:m:3]
    # - La forme de la matrice est (n+1, n+1), on ajoute 1 car, dans certains cas, les indices sont numérotés à partir de 0
    matrix = csr_matrix((t[2:m:3], (t[:m:3], t[1:m:3])), (n+1, n+1))

    # Première application de l'algorithme de Floyd-Warshall pour obtenir toutes les distances minimales entre tous les couples de sommets
    fw1 = f(matrix, 0)  # '0' ici indique probablement que les distances ne sont pas dirigées

    # On compare les distances obtenues à la limite l, en générant une matrice booléenne : Vrai si longueur <= l, Faux sinon
    within_limit = fw1 <= l

    # On réapplique Floyd-Warshall sur la matrice booléenne (type cast possible implicite) pour propager l'information
    # Cela construira, pour chaque couple de sommets, le nombre minimal d'étapes nécessaires pour atteindre un sommet en utilisant uniquement des arêtes de longueur maximum l
    fw2 = f(within_limit)

    # Pour chaque requête, on extrait les indices source et cible à partir du tableau t :
    # - t[m+1::2] = à partir de l'indice m+1, un sur deux, ce sont les indices source des requêtes
    # - t[m+2::2] = à partir de l'indice m+2, un sur deux, ce sont les indices cible des requêtes
    src_indices = t[m+1::2]
    dst_indices = t[m+2::2]

    # On extrait, pour chaque requête, la valeur correspondante (plus court chemin en nombre de "sauts" de <= l) dans la matrice de résultats fw2
    results = fw2[src_indices, dst_indices]

    # On "clip" les résultats pour qu'ils soient au minimum 0 et au maximum n (pour éviter des valeurs aberrantes comme l'infini)
    results_clipped = clip(results, 0, n)

    # On convertit les résultats en entiers (ils sont probablement des floats, ou valeurs spéciales)
    results_int = results_clipped.astype(int)

    # On calcule (résultat % n) - 1 pour chaque élément.
    # Cela peut servir à renvoyer -1 en cas d'inaccessibilité (infinis) ou à normaliser les réponses selon les besoins du problème.
    final_results = (results_int % n) - 1

    # On convertit chaque résultat en chaîne de caractères pour affichage
    # 'map(str, ...)' applique str à chaque élément
    # 'join' rassemble les lignes avec des sauts de ligne
    output = '\n'.join(map(str, final_results))

    # Affiche le résultat final à l'entrée standard
    print(output)

# Exécution de la fonction principale
main()