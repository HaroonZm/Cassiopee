import sys

def calculate_maximum_cells(h, w):
    """
    Calcule le nombre maximal de cellules pouvant être choisies dans une grille h x w,
    de telle sorte qu'aucune paire choisie ne soit adjacente verticalement ou horizontalement.
    
    Si l'une des deux dimensions est 1, le résultat est toujours 1.
    Sinon, la méthode utilise la division euclidienne pour compter les cases non adjacentes.
    
    Paramètres:
        h (int): nombre de lignes de la grille.
        w (int): nombre de colonnes de la grille.
        
    Retourne:
        int: le nombre maximal de cases pouvant être choisies.
    """
    # Cas particulier : si la grille n'a qu'une ligne ou qu'une colonne, il n'y a qu'un seul choix possible
    if h == 1 or w == 1:
        return 1

    # Si la grille a plus d'une ligne et colonne,
    # on place le maximum de cases de manière qu'aucun deux ne soient adjacentes
    # Une stratégie efficace est de considérer une alternance de cases (damier)
    ans = (h // 2) * w  # On choisit une ligne sur deux (complètement)
    
    # Si le nombre de lignes est impair, il reste une ligne à traiter
    if h % 2 != 0:
        # Pour la dernière ligne :
        if w % 2 != 0:
            # Si le nombre de colonnes est impair, on peut choisir un peu plus de la moitié des colonnes
            ans += (w // 2) + 1
        else:
            # Si le nombre de colonnes est pair, on choisit la moitié des colonnes de la dernière ligne
            ans += w // 2

    return int(ans)

def main():
    """
    Fonction principale qui lit l'entrée, appelle la fonction de calcul et affiche le résultat.
    """
    # Lecture des dimensions de la grille en entrée standard
    h, w = map(int, input().split())
    
    # Calcul du nombre maximal de cases sélectionnables
    result = calculate_maximum_cells(h, w)
    
    # Affichage du résultat
    print(result)

if __name__ == "__main__":
    main()