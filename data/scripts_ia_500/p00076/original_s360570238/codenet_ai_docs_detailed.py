from math import pi, cos, sin, atan2

def process_points():
    """
    Lit un nombre entier 'n' depuis l'entrée standard, représentant le nombre de segment à traiter.
    Pour chaque valeur saisie (excepté -1 qui arrête le programme), calcule la position finale
    d'un point après avoir ajouté des vecteurs unitaires tournant à chaque étape de 90 degrés.

    Le processus est le suivant :
    - Commencer à la coordonnée initiale (1.0, 0.0) avec un angle initial de 0 radians.
    - Pour chaque segment restant (n-1 fois), tourner l'angle de 90 degrés (pi/2 radians),
      puis ajouter le vecteur défini par cet angle aux coordonnées actuelles.
    - Après chaque addition, recalcule l'angle effectif du vecteur final (x, y) pour la prochaine rotation.
    - Affiche les coordonnées finales x et y arrondies à deux décimales.

    Le programme continue à lire des nombres tant que n != -1.
    """
    while True:
        n = int(input())  # Lecture de l'entier n
        if n == -1:
            # Condition de sortie : si n est égal à -1, terminer la boucle
            break
        
        n -= 1  # On réduit n car le point initial compte déjà comme un segment
        
        ang = 0.0  # Initialisation de l'angle en radians
        x = 1.0    # Coordonnée initiale en x
        y = 0.0    # Coordonnée initiale en y
        
        # Pour chaque segment restant, calculer la nouvelle position et mettre à jour l'angle
        for _ in range(n):
            ang += pi / 2  # On ajoute 90 degrés (pi/2 radians) à l'angle
            x += cos(ang)  # Ajout de la composante x du segment suivant
            y += sin(ang)  # Ajout de la composante y du segment suivant
            ang = atan2(y, x)  # Mise à jour de l'angle selon la position finale actuelle
        
        # Affichage des coordonnées x et y formatées avec deux décimales
        print("{:.2f}".format(x))
        print("{:.2f}".format(y))

# Appel de la fonction principale pour démarrer le traitement
process_points()