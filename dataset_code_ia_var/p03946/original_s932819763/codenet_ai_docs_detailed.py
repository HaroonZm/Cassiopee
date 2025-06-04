from collections import Counter

def main():
    """
    Fonction principale qui lit les entrées, prépare des listes intermédiaires
    et affiche une valeur basée sur les manipulations d'une séquence d'entiers.

    Le traitement inclut :
    1. Construction d'un suffixe maximum de la liste d'entrée.
    2. Calcul des différences entre ce suffixe et les valeurs de la liste.
    3. Comptage et affichage de la fréquence de la différence maximale.
    """

    # Lecture des deux premiers entiers N (taille de la liste) et T (non utilisé ici)
    N, T = map(int, raw_input().split())

    # Lecture de la liste A de N entiers
    A = map(int, raw_input().split())

    # Construction d'une liste A_r où A_r[i] = max(A[i:])
    A_r = [None for _ in range(N)]  # Initialisation de la liste de suffixe maximum
    n = 0  # Variable pour stocker le maximum courant
    # On parcourt A de la fin vers le début pour remplir A_r
    for i in range(N - 1, -1, -1):
        n = max(A[i], n)
        A_r[i] = n

    # Calcul des différences entre le suffixe maximum (décalé de 1) et la liste A
    B = []
    for i in range(N - 1):
        B.append(A_r[i + 1] - A[i])

    # Comptage de la fréquence de chaque différence dans B
    C = Counter(B)

    # Affichage du nombre d'occurrences de la différence maximale dans B
    print C[max(B)]

if __name__ == "__main__":
    main()