import sys
from bisect import bisect_left, bisect_right

def process_queries(array, queries):
    """
    Pour chaque requête contenant un entier q, calcule le nombre d'éléments dans 'array'
    strictement inférieurs à q et le nombre inférieur ou égal à q.
    
    Args:
        array (list of int): Liste triée d'entiers.
        queries (list of int): Liste des valeurs à requêter.
    
    Returns:
        list of str: Liste de chaînes formattées, chacune indiquant pour chaque q :
                     "nombre d'éléments < q" suivi de "nombre d'éléments ≤ q" (séparés par un espace).
    """
    results = []
    for q in queries:
        left = bisect_left(array, q)       # Place d'insertion à gauche (éléments < q)
        right = bisect_right(array, q)     # Place d'insertion à droite (éléments ≤ q)
        results.append(f"{left} {right}")
    return results

def read_int_list():
    """
    Lit une ligne de l'entrée standard, la découpe par espaces et convertit chaque élément en entier.

    Returns:
        list of int: La liste des entiers extraits de l'entrée.
    """
    return list(map(int, input().split()))

def main():
    """
    Fonction principale qui gère la lecture des entrées, l'exécution des requêtes et l'affichage des résultats.
    
    Entrées attendues :
        - Une première valeur (inutile ici, ignorée).
        - Une ligne contenant des entiers pour former le tableau de référence (doit être trié).
        - Un entier N : le nombre de requêtes.
        - N lignes suivantes, chacune contenant l'entier de la requête.
        
    Affiche :
        - Pour chaque requête, la réponse formatée "left right" sur une ligne.
    """
    input()  # On ignore la première entrée (souvent utilisée pour la taille, pas nécessaire ici)
    arr = read_int_list()
    nq = int(input())
    # Lit toutes les requêtes depuis l'entrée standard
    lines = sys.stdin.readlines()
    queries = [int(lines[i]) for i in range(nq)]
    
    responses = process_queries(arr, queries)
    print('\n'.join(responses))

if __name__ == '__main__':
    main()