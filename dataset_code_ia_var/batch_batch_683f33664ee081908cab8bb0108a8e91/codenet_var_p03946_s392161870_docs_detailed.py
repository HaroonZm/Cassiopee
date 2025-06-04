def compute_max_future_profits(N, T, A):
    """
    Calcule le nombre de jours pour lesquels la différence entre le prix maximal futur 
    et le prix actuel est à son maximum possible.

    Args:
        N (int): Le nombre de jours d'observation des prix.
        T (int): Le nombre de transactions permises (non utilisé dans ce code, mais peut l'être dans des variantes).
        A (list of int): Liste des prix pour chaque jour.

    Returns:
        int: Le nombre de jours pour lesquels le profit maximal peut être réalisé.
    """

    # Étape 1: Calcul du prix maximal futur pour chaque jour en parcourant la liste de la fin vers le début.
    # MAX[i] contiendra le meilleur prix de vente à partir du jour i et au-delà.
    MAX = [A[-1]]  # On commence avec le dernier prix comme maximum initial

    for i in range(N-2, -1, -1):  # Parcours de N-2 jusqu'à 0 (inclus)
        # On ajoute à chaque étape le plus grand entre le maximum courant et A[i]
        MAX.append(max(MAX[-1], A[i]))

    # MAX a été rempli en sens inverse, donc on inverse pour rétablir l'ordre des jours
    MAX = MAX[::-1]

    # Étape 2: Calcul de la différence entre le meilleur prix de vente futur et le prix actuel pour chaque jour
    SABUN = [MAX[i] - A[i] for i in range(N)]

    # Étape 3: On trouve la différence maximale parmi toutes les différences calculées
    MAXSA = max(SABUN)

    # Étape 4: On compte le nombre de jours où cette différence maximale est atteinte
    ANS = 0
    for i in range(N):
        if SABUN[i] == MAXSA:
            ANS += 1

    # Renvoie le nombre de jours permettant d'obtenir le profit maximal
    return ANS

def main():
    """
    Fonction principale : lit l'entrée, appelle la fonction de calcul et affiche le résultat.
    """

    # Lecture de l'entrée : N = nombre de jours, T = nombre de transactions (peut être ignoré ici)
    N, T = map(int, input().split())
    # Lecture des prix pour chaque jour, sous forme de liste d'entiers
    A = list(map(int, input().split()))

    # Calcul et affichage du nombre de jours avec profit maximal
    ans = compute_max_future_profits(N, T, A)
    print(ans)

if __name__ == "__main__":
    main()