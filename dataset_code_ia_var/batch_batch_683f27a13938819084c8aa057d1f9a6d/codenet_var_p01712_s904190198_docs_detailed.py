def read_input():
    """
    Lit les valeurs d'entrée standard :
    - Le premier input contient trois entiers séparés par des espaces : n, W, H
        - n : nombre d'éléments
        - W : largeur (entier)
        - H : hauteur (entier)
    - Les lignes suivantes contiennent trois entiers chacune pour chaque élément :
        - x, y : coordonnées
        - w : rayon ou taille
    Retourne :
        n (int): nombre d'éléments
        W (int): largeur totale
        H (int): hauteur totale
        X (list de tuples): liste de tuples (x, y, w)
    """
    n, W, H = [int(i) for i in input().split()]
    X = [[int(i) for i in input().split()] for _ in range(n)]
    return n, W, H, X

def apply_imos_algorithm(X, W, H):
    """
    Met en œuvre l'algorithme Imos (ou différence de tableaux) pour couvrir
    les intervalles donnés par chaque élément de X sur les axes largeur (w) et hauteur (h).
    Arguments :
        X (list): liste d'éléments, chaque élément étant [x, y, w]
        W (int): largeur totale
        H (int): hauteur totale
    Retourne :
        imos_w (list): tableau de couverture cumulative sur la largeur
        imos_h (list): tableau de couverture cumulative sur la hauteur
    """
    # Initialisation des tableaux Imos (avec une marge de +2 pour éviter les débordements d'indice)
    imos_h = [0] * (H + 2)
    imos_w = [0] * (W + 2)

    # Application de l'algo Imos pour chaque centre (x, y) avec rayon w
    for x, y, w in X:
        # Couvrir l'intervalle vertical [y-w, y+w)
        imos_h[max(0, y - w)] += 1
        imos_h[min(H + 1, y + w)] -= 1
        # Couvrir l'intervalle horizontal [x-w, x+w)
        imos_w[max(0, x - w)] += 1
        imos_w[min(W + 1, x + w)] -= 1

    # Calculer les sommes cumulées sur les axes h et w pour obtenir la couverture effective
    for h in range(H):
        imos_h[h + 1] += imos_h[h]
    for w in range(W):
        imos_w[w + 1] += imos_w[w]

    return imos_w, imos_h

def check_full_coverage(imos_w, imos_h, W, H):
    """
    Vérifie si chaque unité de largeur et hauteur est couverte par au moins un élément.
    Arguments :
        imos_w (list): tableau de couverture cumulative sur la largeur
        imos_h (list): tableau de couverture cumulative sur la hauteur
        W (int): largeur totale
        H (int): hauteur totale
    Retourne :
        (bool, bool): (is_w, is_h)
            - is_w : True si tous les indices de 0 à W-1 en largeur sont couverts
            - is_h : True si tous les indices de 0 à H-1 en hauteur sont couverts
    """
    is_w = all(imos_w[w] >= 1 for w in range(W))
    is_h = all(imos_h[h] >= 1 for h in range(H))
    return is_w, is_h

def main():
    """
    Fonction principale du programme.
    Lit les entrées, applique l'algorithme Imos pour calculer la couverture,
    puis détermine si l'entièreté de la largeur ou de la hauteur est couverte.
    Affiche 'Yes' si c'est le cas, sinon 'No'.
    """
    # Lecture des données
    n, W, H, X = read_input()
    # Application de l'algo Imos
    imos_w, imos_h = apply_imos_algorithm(X, W, H)
    # Vérification de la couverture complète
    is_w, is_h = check_full_coverage(imos_w, imos_h, W, H)
    # Affichage du résultat
    if is_h or is_w:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()