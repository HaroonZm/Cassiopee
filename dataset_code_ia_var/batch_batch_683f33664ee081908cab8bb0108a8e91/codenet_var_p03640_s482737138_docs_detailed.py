from collections import deque

def fill_grid(h, w, n, a):
    """
    Remplit une grille de hauteur h et de largeur w selon les contraintes données.

    La grille est remplie ligne par ligne avec les nombres donnés dans la liste 'a'.
    Chaque nombre dans 'a' indique combien de fois le numéro correspondant à l'indice doit être inséré.
    Le sens de remplissage alterne à chaque ligne : gauche à droite puis droite à gauche, etc.

    Args:
        h (int): Nombre de lignes de la grille.
        w (int): Nombre de colonnes pour chaque ligne de la grille.
        n (int): Nombre de couleurs ou d'entiers distincts à remplir.
        a (list of int): Quantité d'apparitions pour chaque couleur/entier (taille n, indice 0 -> 1er entier).

    Returns:
        None: Imprime chaque ligne de la grille remplie.
    """
    # p représente la direction de remplissage : 1 (gauche à droite), -1 (droite à gauche)
    p = 1
    # d est une deque qui stocke temporairement les éléments de la ligne en cours de remplissage
    d = deque()
    # Parcours de chaque couleur/entier à placer
    for i in range(n):
        # Pour chaque répétition de la couleur/entier courant
        for j in range(a[i]):
            # Si la ligne en cours est pleine, on l'affiche et on prépare une nouvelle deque
            if len(d) == w:
                print(*d)
                d = deque()
                # On change la direction de remplissage pour la prochaine ligne
                p *= -1
            # Ajout du nouvel entier dans la deque selon la direction actuelle
            if p == 1:
                d.append(i + 1)
            elif p == -1:
                d.appendleft(i + 1)
    # Si la dernière ligne n'est pas complète mais doit être affichée
    if len(d) != 0:
        print(*d)

def main():
    """
    Fonction principale qui lit les paramètres d'entrée et appelle la fonction de remplissage de la grille.
    """
    # Lecture des dimensions de la grille
    h, w = map(int, input().split())
    # Lecture du nombre de couleurs/entiers
    n = int(input())
    # Lecture de la liste des quantités à placer
    a = list(map(int, input().split()))
    # Remplissage et affichage de la grille selon les règles
    fill_grid(h, w, n, a)

if __name__ == "__main__":
    main()