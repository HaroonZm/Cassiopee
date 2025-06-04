from collections import deque

def process_operations(n):
    """
    Traite une série d'opérations sur une deque selon les commandes fournies.

    Paramètres :
        n (int): Le nombre d'opérations à effectuer.

    Remarques :
        Les opérations attendues sont sous la forme de chaînes d'entrée,
        chacune contenant une série d'instructions au format suivant :
        - "0 0 X" : Ajoute X en début de deque.
        - "0 1 X" : Ajoute X en fin de deque.
        - "1 Y"   : Affiche l'élément en position Y (base 0) de la deque.
        - "X 0"   : Retire l'élément en début de deque.
        - Autres  : Retire l'élément en fin de deque.
    """
    # Initialisation de la deque vide
    A = deque()

    # Boucle sur chaque opération
    for i in range(n):
        # Lecture d'une opération sous forme de chaîne, puis découpage en liste
        tmp = input().split()

        # Cas 1 : Ajout en tête ("0 0 X")
        if tmp[0] == "0" and tmp[1] == "0":
            # Ajoute l'élément tmp[2] au début de la deque
            A.appendleft(tmp[2])

        # Cas 2 : Ajout en fin ("0 1 X")
        elif tmp[0] == "0" and tmp[1] == "1":
            # Ajoute l'élément tmp[2] à la fin de la deque
            A.append(tmp[2])

        # Cas 3 : Affichage d'un élément à l'indice Y ("1 Y")
        elif tmp[0] == "1":
            # Affiche l'élément situé à l'indice tmp[1]
            print(A[int(tmp[1])])

        # Cas 4 : Retrait en tête ("X 0")
        elif tmp[1] == "0":
            # Retire l'élément en début de deque
            A.popleft()

        # Cas 5 : Retrait en fin (tous les autres cas)
        else:
            # Retire l'élément en fin de deque
            A.pop()

def main():
    """
    Point d'entrée du programme. Lit le nombre d'opérations à traiter,
    puis lance leur traitement.
    """
    # Lecture du nombre d'opérations à effectuer
    n = int(input())
    # Traitement des opérations sur la deque
    process_operations(n)

if __name__ == "__main__":
    main()