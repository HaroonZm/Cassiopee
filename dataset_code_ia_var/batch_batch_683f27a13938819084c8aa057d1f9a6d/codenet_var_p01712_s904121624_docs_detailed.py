def parse_input():
    """
    Lit les entrées de l'utilisateur pour obtenir les paramètres du problème et les zones de couverture Wi-Fi.
    
    Returns:
        tuple:
            N (int): nombre de points d'accès Wi-Fi
            W (int): largeur de la zone
            H (int): hauteur de la zone
            access_points (list of tuples): la liste des points d'accès,
                chaque tuple contient (x, y, w) :
                    x (int): position sur l'axe X
                    y (int): position sur l'axe Y
                    w (int): rayon de couverture
    """
    # Lire les premiers paramètres de l'entrée standard
    N, W, H = [int(x) for x in input().split()]
    access_points = []
    # Lire les N points d'accès
    for _ in range(N):
        x, y, w = [int(x) for x in input().split()]
        access_points.append((x, y, w))
    return N, W, H, access_points

def build_coverage_maps(W, H, access_points):
    """
    Crée deux cartes de couverture (une pour X, une pour Y) représentant la couverture Wi-Fi.
    
    Args:
        W (int): largeur de la zone
        H (int): hauteur de la zone
        access_points (list of tuples): liste des points d'accès (x, y, w)
        
    Returns:
        tuple:
            map_x (list): couverture Wi-Fi selon l'axe X
            map_y (list): couverture Wi-Fi selon l'axe Y
    """
    # Initialisation des zones de couverture pour chaque colonne et ligne
    map_x = [0] * W  # index: colonne, valeur: intervalle max de couverture vers la droite à partir de ce point
    map_y = [0] * H  # index: ligne, valeur: intervalle max de couverture vers le bas à partir de ce point

    for x, y, w in access_points:
        # Calculer la portée sur l'axe X
        start_x = max(0, x - w)
        reach_x = x + w - start_x  # Distance couverte à partir de start_x
        map_x[start_x] = max(map_x[start_x], reach_x)

        # Calculer la portée sur l'axe Y
        start_y = max(0, y - w)
        reach_y = y + w - start_y  # Distance couverte à partir de start_y
        map_y[start_y] = max(map_y[start_y], reach_y)
    return map_x, map_y

def check_wifi(wifi):
    """
    Vérifie si l'ensemble de la zone peut être couverte par des intervalles Wi-Fi continue.
    Algorithme proche du problème du « Jump Game »: à chaque position, on vérifie jusqu'où on peut aller.
    
    Args:
        wifi (list): liste représentant la couverture depuis chaque point.
    
    Returns:
        bool: True si la zone entière (jusqu'à len(wifi)) est couverte, False sinon.
    """
    max_reach = 0  # La portée actuelle atteignable
    end = len(wifi)  # Fin de la zone

    for i, interval in enumerate(wifi):
        # Si l'intervalle depuis 'i' augmente la portée
        if interval and i + interval > max_reach:
            max_reach = i + interval

        # Si on a déjà couvert toute la zone
        if max_reach >= end:
            return True

        # Si la position actuelle est encore couverte, on continue
        if i < max_reach:
            continue

        # Si on tombe sur une position non couverte, impossible de continuer
        return False

    # Si la boucle se termine sans tout couvrir, retour Faux
    return False

def main():
    """
    Fonction principale pour l'exécution du programme.
    """
    # Lire et traiter les entrées
    N, W, H, access_points = parse_input()
    
    # Construire les cartes de couverture pour X et Y
    map_x, map_y = build_coverage_maps(W, H, access_points)
    
    # Vérifier si l'une des deux directions (X ou Y) est totalement couverte
    if check_wifi(map_x) or check_wifi(map_y):
        print('Yes')
    else:
        print('No')

# Lancer le programme principal
main()