from math import log10
from bisect import bisect_left

def preprocess_intervals(n, intervals):
    """
    Calcule les préfixes de log des probabilités modifiées pour une liste d'intervalles.
    
    Args:
        n (int): Nombre d'intervalles.
        intervals (list of lists): Liste des intervalles [position, valeur], la longueur doit être n.
    
    Returns:
        list: Liste de préfixe commençant par [0, 0] pour facilité de traitement.
              Chaque élément est [position, prefix_sum_log_value].
    """
    # Ajout d'un point initial pour simplifier le traitement des bornes
    l = [[0, 0]] + intervals
    # Remplacement des valeurs 'valeur' par log10(1 - valeur/10)
    for i in range(1, n + 1):
        l[i][1] = log10(1 - l[i][1] / 10)
    # Calcul du préfixe de la somme des logs
    for i in range(n):
        l[i + 1][1] += l[i][1]
    return l

def query_probability(l, a, b):
    """
    Évalue la probabilité pour un intervalle [a, b), basé sur les préfixes calculés.
    
    Args:
        l (list): Liste des préfixes, où chaque élément est [position, prefix_sum_log_value].
        a (int): Début de l'intervalle (inclus).
        b (int): Fin de l'intervalle (exclu).
    
    Returns:
        float: Probabilité calculée sur l'intervalle [a, b).
    """
    # Recherche les indices correspondant à a et b avec bisect_left
    i = bisect_left(l, [a, 0]) - 1
    j = bisect_left(l, [b, 0]) - 1
    # Récupère la différence de préfixes dans la plage [a, b)
    p = l[j][1] - l[i][1] + 9  # Décalage par +9 pour normalisation (spécifique à la logique métier)
    return 10 ** p

def main():
    """
    Fonction principale. Prépare les données, effectue les requêtes et affiche les résultats.
    """
    # Lecture du nombre d'intervalles à traiter
    n = int(input())
    # Lecture des intervalles (position, valeur), en entrée utilisateur
    intervals = [list(map(int, input().split())) for _ in range(n)]
    # Prétraitement des intervalles
    l = preprocess_intervals(n, intervals)
    # Nombre de requêtes à traiter
    q = int(input())
    for _ in range(q):
        # Lecture des bornes de la requête
        a, b = map(int, input().split())
        # Calcul et affichage du résultat de la requête
        print(query_probability(l, a, b))

if __name__ == "__main__":
    main()