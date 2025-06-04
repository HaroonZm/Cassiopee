import math

def num_divisors_table(n):
    """
    Calcule le nombre de diviseurs pour chaque entier de 1 à n.

    Cette fonction utilise une méthode de crible pour déterminer, 
    pour chaque entier i compris entre 1 et n, le nombre total 
    de diviseurs de i. Elle retourne une liste où l'élément d'indice k 
    correspond au nombre de diviseurs de k (avec 0 pour l'indice 0, non utilisé).

    Args:
        n (int): La borne supérieure de la table (inclus).

    Returns:
        list[int]: Une liste de taille n+1 contenant le nombre de diviseurs pour chaque entier de 1 à n.
    """
    # Initialisation d'une liste de zéros, de taille n+1
    table = [0] * (n + 1)

    # Pour chaque entier i de 1 à n
    for i in range(1, n + 1):
        # Pour chaque multiple j de i entre i et n (inclus)
        # Incrémente le compteur de diviseurs pour j
        for j in range(i, n + 1, i):
            table[j] += 1

    # La table contenant le nombre de diviseurs pour chaque entier de 1 à n
    return table

def main():
    """
    Fonction principale qui lit un entier N depuis l'entrée, calcule la 
    somme demandée, puis l'affiche.

    La somme calculée est, pour tous les entiers i de 1 à N :
        Somme de i * (nombre de diviseurs de i)
    """
    # Lecture de l'entier N de l'entrée standard
    N = int(input())

    # Calcul de la table des diviseurs pour tous les entiers jusqu'à N
    cd_table = num_divisors_table(N)

    # Initialisation de la réponse
    ans = 0
    # Pour chaque i de 1 à N, ajouter i multiplié par son nombre de diviseurs
    for i in range(1, N + 1):
        ans += i * cd_table[i]

    # Affichage du résultat final
    print(ans)

if __name__ == "__main__":
    main()