def read_input():
    """
    Lit les entrées depuis la console.

    Demande à l'utilisateur d'entrer :
    - Le nombre d'éléments n
    - Une liste d'entiers v de taille n
    - Une liste d'entiers c de taille n

    Returns:
        tuple: Un tuple (n, v, c) où :
            n (int) : Le nombre d'éléments
            v (list of int): La première liste d'entiers
            c (list of int): La seconde liste d'entiers
    """
    n = int(input())  # Lire le nombre d'éléments
    v = list(map(int, input().split()))  # Lire la première liste d'entiers
    c = list(map(int, input().split()))  # Lire la seconde liste d'entiers
    return n, v, c

def calculate_positive_score(n, v, c):
    """
    Calcule la somme des différences positives entre les éléments correspondants de deux listes.

    Pour chaque index i de 0 à n-1, calcule score = v[i] - c[i].
    Si score est supérieur à 0, l'ajoute au résultat final.

    Args:
        n (int): Le nombre d'éléments dans les listes.
        v (list of int): La première liste d'entiers.
        c (list of int): La seconde liste d'entiers.

    Returns:
        int: La somme de toutes les différences positives (v[i] - c[i]) pour lesquelles cette différence est strictement positive.
    """
    result = 0  # Variable pour stocker la somme finale
    for i in range(n):
        score = v[i] - c[i]  # Calcul de la différence pour l'élément i
        if score > 0:
            result += score  # Ajouter si la différence est positive
    return result

def main():
    """
    Fonction principale qui orchestre la lecture des entrées, 
    le calcul et l'affichage du résultat.
    """
    n, v, c = read_input()  # Lecture des entrées utilisateur
    result = calculate_positive_score(n, v, c)  # Calcul du résultat
    print(result)  # Affichage du résultat

if __name__ == "__main__":
    main()