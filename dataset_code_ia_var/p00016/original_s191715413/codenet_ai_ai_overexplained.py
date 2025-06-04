import math  # On importe le module math qui contient des fonctions mathématiques utiles, comme cosinus, sinus, et la constante pi.

nowx = 0  # On initialise la variable nowx à 0. Elle va stocker la position actuelle sur l'axe des abscisses (l'axe X).
nowy = 0  # On initialise la variable nowy à 0. Elle va stocker la position actuelle sur l'axe des ordonnées (l'axe Y).
nowa = 90  # On initialise la variable nowa à 90. Elle représente l'angle actuel en degrés. 90 degrés pointe vers le haut dans le repère trigonométrique standard.

while True:  # On démarre une boucle infinie. Elle va s'exécuter sans fin jusqu'à ce qu'une condition de sortie soit atteinte à l'intérieur de la boucle.
    # On demande à l'utilisateur de fournir une entrée. raw_input() lit une ligne depuis l'utilisateur sous forme de chaîne de caractères.
    # .split(',') sépare la chaîne obtenue en une liste selon le séparateur virgule ','
    # La compréhension de liste [int(i) for i in ...] transforme chaque élément de cette liste en un entier.
    (d, a) = [int(i) for i in raw_input().split(',')]  # On assigne les deux valeurs d et a obtenues à partir de l'entrée utilisateur.
    
    if (d == a == 0):  # Ceci est une condition pour terminer le programme. Si les deux valeurs d et a sont égales à 0 en même temps...
        print int(nowx)  # ...on affiche la valeur actuelle de nowx. int() convertit le résultat en entier (en supprimant la partie décimale).
        print int(nowy)  # ...on affiche la valeur actuelle de nowy, convertie en entier elle aussi.
        break  # Le mot-clé break permet de sortir immédiatement de la boucle while, même si la condition de boucle est toujours vraie.
    else:  # Si la condition de sortie n'est pas atteinte (les deux valeurs ne sont pas 0)...
        # On met à jour la coordonnée X actuelle, nowx.
        # math.cos() attend un angle en radians, donc on convertit nowa de degrés en radians.
        # Pour convertir des degrés en radians, on multiplie par pi et on divise par 180.
        # On multiplie le résultat du cosinus par d (la distance) pour obtenir la composante horizontale du déplacement.
        nowx += math.cos(nowa / 180.0 * math.pi) * d  # On augmente nowx du déplacement sur l'axe X.
        
        # On met à jour la coordonnée Y actuelle, nowy.
        # Ici aussi, on convertit l'angle nowa en radians puis on calcule le sinus.
        # Le sinus multiplié par d donne la composante verticale du déplacement.
        nowy += math.sin(nowa / 180.0 * math.pi) * d  # On augmente nowy du déplacement sur l'axe Y.
        
        # On met à jour l'angle nowa.
        # On retire à nowa la valeur a, ce qui correspond à une rotation dans le sens des aiguilles d'une montre.
        nowa -= a  # nowa est ainsi décrémenté pour changer la direction pour le prochain mouvement.