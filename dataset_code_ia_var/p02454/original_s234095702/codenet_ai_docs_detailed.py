import sys
import bisect

def process_queries():
    """
    Lit un tableau d'entiers, le nombre de requêtes, puis applique, pour chaque requête,
    les fonctions de recherche bisect_left et bisect_right sur le tableau.
    
    Entrée :
        - Première ligne ignorée (non utilisée)
        - Deuxième ligne : liste d'entiers séparés par des espaces
        - Troisième ligne : nombre de requêtes (entier)
        - Puis pour chaque requête : une ligne contenant un entier
        
    Affiche pour chaque requête : "<left> <right>" où
        - left est l'indice d'insertion possible en gardant le tableau trié (bisect_left)
        - right est l'indice d'insertion à droite (bisect_right)
    """

    input()  # Lecture de la première ligne (non utilisée dans le code)
    arr = list(map(int, input().split()))  # Lecture du tableau d'entiers
    nq = int(input())  # Lecture du nombre de requêtes

    # Lecture des lignes suivantes depuis l'entrée standard, une pour chaque requête
    lines = sys.stdin.readlines()
    # Initialisation de la liste de réponses
    ans = [None] * nq

    # Traitement de chaque requête
    for i in range(nq):
        q = int(lines[i])  # Extraction du nombre à traiter
        # Calcul des indices d'insertion avec bisect_left et bisect_right
        left = bisect.bisect_left(arr, q)
        right = bisect.bisect_right(arr, q)
        # Formatage de la réponse sous la forme "left right"
        ans[i] = '{} {}'.format(left, right)

    # Affichage de toutes les réponses, une par ligne
    print('\n'.join(ans))

# Lancement du programme principal
if __name__ == "__main__":
    process_queries()