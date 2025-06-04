def input_parameters():
    """
    Lit les paramètres d'entrée depuis l'utilisateur.

    Retourne :
        N (int): Nombre de rects (formes, projecteurs, etc.).
        W (int): Largeur de la zone cible.
        H (int): Hauteur de la zone cible.
    """
    N, W, H = map(int, input().split())
    return N, W, H

def process_events(N, W, H):
    """
    Initialise et met à jour les tableaux de lignes et de colonnes selon les N projecteurs.
    
    Args:
        N (int): Nombre de projecteurs ou d'événements.
        W (int): Largeur de la zone cible.
        H (int): Hauteur de la zone cible.
        
    Retourne :
        row (list[int]): Tableau de longueur H+1, indiquant la couverture pour chaque ligne Y.
        col (list[int]): Tableau de longueur W+1, indiquant la couverture pour chaque colonne X.
    """
    # On initialise les compteurs de couverture à zéro pour chaque ligne et colonne
    row = [0] * (H + 1)
    col = [0] * (W + 1)
    
    # On lit et traite chaque projecteur (événement)
    for _ in range(N):
        x, y, w = map(int, input().split())
        # On applique le principe du "sweep line" : on incrémente/décrémente les bornes
        row[max(0, y - w)] += 1              # Incrémente la borne basse sur l'axe Y
        row[min(H, y + w)] -= 1              # Décrémente la borne haute sur l'axe Y
        col[max(0, x - w)] += 1              # Incrémente la borne basse sur l'axe X
        col[min(W, x + w)] -= 1              # Décrémente la borne haute sur l'axe X
    return row, col

def verify_full_coverage(arr, length):
    """
    Vérifie si tous les indices de l'array (avec préfixe) sont strictement positifs,
    c'est-à-dire chaque ligne/colonne est totalement couverte.

    Args:
        arr (list[int]): Tableau de couverture à vérifier.
        length (int): Nombre d'indices à vérifier (typiquement H pour lignes ou W pour colonnes).

    Retourne :
        flag (bool): True si chaque case 0...length-1 a une valeur strictement > 0.
    """
    flag = True
    # On calcule le préfixe cumulé, qui donne la quantité de couverture sur chaque ligne/colonne
    for i in range(length):
        arr[i + 1] += arr[i]
        if arr[i] <= 0:
            flag = False
    return flag

def main():
    """
    Fonction principale :
    - Lit les données d'entrée.
    - Instancie les tableaux de couverture pour lignes et colonnes.
    - Vérifie si au moins une des deux directions est totalement couverte par les zones de projection.
    - Affiche "Yes" si c'est le cas, sinon "No".
    """
    # Lecture des paramètres principaux
    N, W, H = input_parameters()
    # Pré-traitement des événements/projections
    row, col = process_events(N, W, H)
    # Vérification de la couverture complète sur les lignes (Y)
    if verify_full_coverage(row, H):
        print("Yes")
        return
    # Vérification de la couverture complète sur les colonnes (X)
    if verify_full_coverage(col, W):
        print("Yes")
    else:
        print("No")

# Démarrage du script principal
if __name__ == "__main__":
    main()