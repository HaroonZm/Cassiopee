def distance(star, position):
    """
    Calcule la distance euclidienne entre deux points dans un espace à 3 dimensions.

    Parameters:
        star (list or tuple of float): Coordonnées (x, y, z) du premier point.
        position (list or tuple of float): Coordonnées (x, y, z) du second point.

    Returns:
        float: Distance euclidienne entre les deux points.
    """
    # Calcule la somme des carrés des différences de chaque coordonnée, puis prend la racine carrée
    return sum([(a - b)**2 for a, b in zip(star, position)])**0.5

def difference(star, position):
    """
    Calcule la différence coordonnée à coordonnée entre deux points.

    Parameters:
        star (list or tuple of float): Coordonnées (x, y, z) du premier point.
        position (list or tuple of float): Coordonnées (x, y, z) du second point.

    Returns:
        list of float: Liste des différences entre chaque coordonnée.
    """
    # Retourne la soustraction de chaque coordonnée individuellement
    return [(a - b) for a, b in zip(star, position)]

while True:
    # Lecture du nombre d'étoiles pour le cas de test courant
    n = int(input())
    if n == 0:
        # Sort de la boucle principale si aucun cas à traiter
        break
    
    # Lecture des coordonnées des n étoiles (chaque ligne contient 3 flottants)
    stars = [list(map(float, input().split())) for i in range(n)]
    
    # Calcul du barycentre (position moyenne) initial de toutes les étoiles
    position = [
        sum([s[i] for s in stars]) / len(stars)  # Moyenne pour x, y, puis z
        for i in range(3)
    ]
    
    move_rate = 1  # Facteur d'apprentissage pour ajuster la position
    
    # Exécute l'algorithme principal pendant 3000 itérations pour approcher la solution optimale
    for i in range(3000):
        if i % 100 == 0:
            # Réduit le taux de déplacement tous les 100 pas pour affiner la précision
            move_rate /= 2
        
        index = 0       # Index de l'étoile la plus éloignée du barycentre courant
        dis_max = 0     # Valeur maximale de cette distance
        
        # Recherche de l'étoile la plus éloignée de la position courante
        for j, star in enumerate(stars):
            dis = distance(star, position)
            if dis_max < dis:
                dis_max = dis
                index = j
        
        # Calcul du vecteur de déplacement (de la position actuelle vers l'étoile la plus éloignée)
        diff = difference(stars[index], position)
        
        # Met à jour la position courante en se rapprochant de l'étoile la plus éloignée
        position = [
            position[i] + diff[i] * move_rate
            for i in range(3)
        ]

    # Affiche la distance maximale trouvée, formatée à 5 décimales
    print(format(dis_max, ".5f"))