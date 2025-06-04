from sys import stdin

def read_input():
    """
    Lit une seule ligne de l'entrée standard, enlève les espaces de fin, puis divise la ligne en trois éléments distincts.
    Retourne :
        tuple : trois chaînes extraites de l'entrée standard.
    """
    values = stdin.readline().rstrip().split()
    # Décompacte la liste en trois variables distinctes
    return values[0], values[1], values[2]

def check_sequence(word1, word2, word3):
    """
    Vérifie si le dernier caractère de word1 est le même que le premier caractère de word2
    ET si le dernier caractère de word2 est le même que le premier caractère de word3.

    Args:
        word1 (str): Premier mot.
        word2 (str): Deuxième mot.
        word3 (str): Troisième mot.

    Returns:
        bool: True si la condition est remplie, False sinon.
    """
    return word1[-1] == word2[0] and word2[-1] == word3[0]

def main():
    """
    Fonction principale qui gère la lecture de l'entrée, appelle la fonction de vérification,
    puis affiche 'YES' si la séquence répond aux critères, 'NO' sinon.
    """
    a, b, c = read_input()
    if check_sequence(a, b, c):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()