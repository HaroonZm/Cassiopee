"""
Ce programme construit une matrice de taille NxN selon un schéma récursif.
À chaque niveau de récursion, il partitionne un ensemble d'indices en deux sous-ensembles, et attribue à chaque paire (i, j) de deux sous-ensembles un niveau de profondeur, stocké dans une matrice A.
En fin de programme, il affiche la partie supérieure (hors diagonale) de cette matrice.
"""

def construire_matrice(N):
    """
    Construit une matrice NxN où A[i][j] indique le niveau de la première dissociation
    entre les indices i et j lors d'un partitionnement récursif par dichotomie.
    
    Args:
        N (int): La taille de la matrice carrée à construire.
    
    Returns:
        list[list[int]]: La matrice construite selon l'algorithme.
    """
    # Initialisation de la matrice avec des valeurs None
    matrice = [[None] * N for _ in range(N)]

    def partition_et_label(liste_indices, niveau):
        """
        Partitionne récursivement la liste des indices et assigne un niveau
        aux couples d'indices situés dans deux sous-listes différentes à chaque étape.

        Args:
            liste_indices (list[int]): Liste courante d'indices à partitionner.
            niveau (int): Niveau de récursion actuel à assigner aux couples inter-groupes.
        """
        # Si la sous-liste ne comprend qu'un seul élément, il n'y a plus rien à faire
        if len(liste_indices) == 1:
            return
        
        # Division en deux sous-listes (éléments pairs et impairs)
        sous_liste_0 = liste_indices[::2]
        sous_liste_1 = liste_indices[1::2]
        
        # Pour chaque paire d'indices appartenant à des sous-listes différentes,
        # on affecte le niveau dans la matrice (symétriquement)
        for i in sous_liste_0:
            for j in sous_liste_1:
                matrice[i][j] = niveau
                matrice[j][i] = niveau

        # Appels récursifs sur chaque sous-liste, en augmentant le niveau
        partition_et_label(sous_liste_0, niveau + 1)
        partition_et_label(sous_liste_1, niveau + 1)
    
    # Déclenchement de la récursion sur l'ensemble des indices
    partition_et_label(list(range(N)), 1)
    return matrice

def afficher_matrice_superieure(matrice):
    """
    Affiche la partie supérieure hors diagonale de la matrice fournie.
    Chaque ligne i affiche les éléments situés après la colonne i.

    Args:
        matrice (list[list[int]]): La matrice à afficher.
    """
    N = len(matrice)
    for i, ligne in enumerate(matrice[:-1]):
        # Affiche, pour la ligne i, les éléments de la colonne i+1 à la fin
        print(*ligne[i+1:])

def main():
    """
    Fonction principale du programme :
    - Récupère la taille N de la matrice
    - Construit la matrice
    - Affiche la portion utile de la matrice
    """
    # Lecture de l'entrée utilisateur (taille de la matrice)
    N = int(input())
    # Construction de la matrice
    matrice = construire_matrice(N)
    # Affichage du résultat
    afficher_matrice_superieure(matrice)

if __name__ == "__main__":
    main()