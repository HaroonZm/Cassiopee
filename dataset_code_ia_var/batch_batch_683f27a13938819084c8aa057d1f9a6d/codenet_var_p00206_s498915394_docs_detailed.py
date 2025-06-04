import sys

def read_input_line():
    """
    Lit une ligne de l'entrée standard via sys.stdin et retourne une liste d'entiers.

    Returns:
        list: Liste d'entiers extraits de la ligne entrée.
    """
    return list(map(int, sys.stdin.readline().split()))

def process_year(L):
    """
    Traite douze mois d'économies et de dépenses et détermine à quel mois les économies sont supérieures
    ou égales à la valeur cible L.

    Args:
        L (int): Objectif d'épargne à atteindre.

    Comportement:
        - Lit 12 paires de valeurs représentant les économies mensuelles (M) et les dépenses mensuelles (N).
        - Pour chaque mois, additionne le gain net aux économies.
        - Si la somme des économies atteint ou dépasse L à un certain mois, affiche ce mois (indice 1-based).
        - Si la somme n'est jamais atteinte, affiche 'NA'.
    """
    savings = 0  # Économies cumulées
    # Lecture des 12 paires (M, N) représentant chaque mois
    monthly_data = [read_input_line() for _ in range(12)]
    for i, (M, N) in enumerate(monthly_data, start=1):
        savings += M - N  # Met à jour les économies à chaque mois
        if savings >= L:
            print(i)  # Affiche le mois atteint (indice 1-based)
            break
    else:
        print("NA")  # Jamais atteint dans les 12 mois

def main():
    """
    Fonction principale qui gère la boucle de lecture des cibles et de traitement des années.

    - Lit la cible d'épargne L pour chaque cas.
    - Termine lorsque L == 0.
    - Sinon, traite chaque année via process_year.
    """
    while True:
        try:
            L = int(input())
        except EOFError:
            break  # Fin de l'entrée
        if L == 0:
            break  # Terminaison du programme
        process_year(L)

if __name__ == "__main__":
    main()