import itertools

def read_bingo_card():
    """
    Lit du clavier 3 lignes représentant la carte de bingo 3x3.
    Chaque ligne contient 3 entiers séparés par des espaces.

    Returns:
        list: une liste 2D (3x3) d'entiers représentant la carte de bingo.
    """
    bingo_card = []
    for _ in range(3):
        # Lire une ligne d'entrée, la diviser et convertir chaque élément en entier
        row = [int(i) for i in input().split()]
        bingo_card.append(row)
    return bingo_card

def read_called_numbers():
    """
    Lit la liste des nombres appelés.

    L'utilisateur saisit d'abord un entier N (le nombre de lignes de saisie).
    Ensuite, N lignes d'entrées sont lues, chacune pouvant contenir plusieurs entiers,
    tous les nombres sont collectés dans une simple liste d'entiers.

    Returns:
        list: une liste d'entiers représentant les numéros appelés.
    """
    N = int(input())
    called_numbers = []
    # Lire N lignes, chaque ligne peut contenir plusieurs entiers
    for _ in range(N):
        numbers = input().split()
        called_numbers.extend(numbers)
    # Conversion en entiers
    called_numbers = list(map(int, called_numbers))
    return called_numbers

def mark_bingo_card(bingo_card, called_numbers):
    """
    Marque les numéros appelés sur la carte de bingo.

    Args:
        bingo_card (list): carte de bingo 3x3 comme liste de listes d'entiers.
        called_numbers (list): liste des numéros qui ont été appelés.

    Returns:
        list: une matrice 3x3 (liste de listes) contenant 1 si la case a été marquée, sinon 0.
    """
    marks = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if bingo_card[i][j] in called_numbers:
                marks[i][j] = 1
    return marks

def has_bingo(marks):
    """
    Vérifie s'il y a une ligne, colonne ou diagonale complètement marquée (Bingo).

    Args:
        marks (list): une matrice 3x3 indiquant les cases marquées (1) ou non (0).

    Returns:
        bool: True si un Bingo est détecté, sinon False.
    """
    # Vérifier chaque ligne
    for i in range(3):
        if sum(marks[i]) == 3:
            return True
    # Vérifier chaque colonne
    for j in range(3):
        if marks[0][j] + marks[1][j] + marks[2][j] == 3:
            return True
    # Vérifier la diagonale principale
    if marks[0][0] + marks[1][1] + marks[2][2] == 3:
        return True
    # Vérifier la diagonale secondaire
    if marks[0][2] + marks[1][1] + marks[2][0] == 3:
        return True
    return False

def main():
    """
    Fonction principale qui orchestre la saisie des données, le marquage et la détection du bingo.
    Affiche "Yes" si un Bingo est réalisé, "No" sinon.
    """
    # Lire la carte de bingo
    bingo_card = read_bingo_card()
    # Lire les numéros appelés
    called_numbers = read_called_numbers()
    # Marquer la carte selon les numéros appelés
    marks = mark_bingo_card(bingo_card, called_numbers)
    # Vérifier s'il y a un Bingo
    if has_bingo(marks):
        print("Yes")
    else:
        print("No")

# Exécution du programme principal
if __name__ == "__main__":
    main()