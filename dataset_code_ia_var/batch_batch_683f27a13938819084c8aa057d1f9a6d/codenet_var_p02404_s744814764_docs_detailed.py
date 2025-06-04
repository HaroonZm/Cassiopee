def draw_rectangles():
    """
    Dessine des rectangles creux à partir des dimensions données, jusqu'à ce que l'entrée soit '0 0'.

    Pour chaque paire H et W lue sur l'entrée standard :
        - Affiche un rectangle de H lignes par W colonnes.
        - Les bords du rectangle sont composés de '#'.
        - L'intérieur du rectangle (si H > 2 et W > 2) est rempli de '.'.
        - Après chaque rectangle, une ligne vide est imprimée.
        - Le programme s'arrête lorsque '0 0' est saisi.
    """
    while True:
        # Lit les dimensions du rectangle depuis l'entrée utilisateur
        H, W = map(int, input().split())
        
        # Condition d'arrêt : si les deux valeurs sont 0, sortir de la boucle principale
        if H == 0 and W == 0:
            break

        # Boucle sur chaque ligne du rectangle
        for i in range(H):
            # Boucle sur chaque colonne du rectangle
            for j in range(W):
                # Vérifie si le point courant est à l'intérieur, pas sur les bords
                if 0 < i < H - 1 and 0 < j < W - 1:
                    # Affiche un point pour le cœur du rectangle, sans retour à la ligne
                    print('.', end="")
                else:
                    # Affiche un dièse pour le bord du rectangle, sans retour à la ligne
                    print('#', end="")
            # Fin de la ligne : on passe à la suivante
            print('')
        # Ligne vide après chaque rectangle pour séparer les affichages
        print('')

# Appel de la fonction principale pour lancer le programme
draw_rectangles()