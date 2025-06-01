def main():
    # Cette fonction principale exécute le programme complet.
    # Elle ne prend aucun argument et ne retourne rien.
    
    # Boucle infinie pour traiter plusieurs jeux de données jusqu'à ce que l'entrée soit 0.
    while True:
        # Lecture d'un entier n depuis l'entrée standard via input()
        # input() renvoie une chaîne de caractères, on la convertit en entier avec int()
        n = int(input())
        
        # Si n est égal à 0, c'est le signal pour arrêter la boucle et terminer le programme.
        if not n:
            break
        
        # Initialisation d'une liste vide appelée ps pour stocker les points sous forme de tuples (x,y).
        ps = []
        
        # Initialisation d'un dictionnaire vide pour stocker les points comme clés.
        # Cela permettra un accès rapide checking la présence d'un point donné.
        dic = {}
        
        # Boucle pour lire n points, chaque point est une paire d'entiers (x, y).
        for i in range(n):
            # Lecture de deux entiers x et y séparés par un espace.
            # map() applique int() à chaque élément résultant du split().
            x, y = map(int, input().split())
            
            # Ajout du point (x, y) comme clé dans le dictionnaire dic avec une valeur arbitraire (1).
            # Cela sert à vérifier rapidement si un point donné existe.
            dic[(x, y)] = 1
            
            # Ajout du point (x, y) dans la liste ps pour stocker tous les points.
            ps.append((x, y))
        
        # Initialisation de la variable ans à zéro.
        # Cette variable va contenir la plus grande aire trouvée, initialement à zéro.
        ans = 0
        
        # Double boucle for imbriquée pour examiner toutes les paires de points possibles (y compris identiques).
        for i in range(n):
            for j in range(n):
                
                # Extraction des deux points p1 et p2 à partir de la liste ps.
                p1 = ps[i]
                p2 = ps[j]
                
                # Calcul du vecteur v = p2 - p1 en coordonnées x et y.
                vx = p2[0] - p1[0]  # Différence des coordonnées x
                vy = p2[1] - p1[1]  # Différence des coordonnées y
                
                # Le but est de vérifier l'existence de deux autres points formant un carré avec p1 et p2.
                # Les coordonnées des autres points sont obtenues en utilisant une rotation de 90 degrés
                # autour de chaque point du segment p1-p2, ce qui correspond à un vecteur perpendiculaire.
                # Le vecteur perpendiculaire au vecteur (vx, vy) est (vy, -vx).
                
                # Vérification si les points (p1.x + vy, p1.y - vx) et (p2.x + vy, p2.y - vx) existent dans dic.
                # Si c'est le cas, cela signifie que ces quatre points forment un carré.
                if (p1[0] + vy, p1[1] - vx) in dic and (p2[0] + vy, p2[1] - vx) in dic:
                    # Calcul de la longueur au carré du côté du carré, qui est vx^2 + vy^2.
                    # On met à jour ans avec la plus grande valeur trouvée.
                    ans = max(ans, vx ** 2 + vy ** 2)
        
        # Affichage de la plus grande aire (côté au carré) trouvée pour ce jeu de points.
        print(ans)

# Appel de la fonction principale pour démarrer le programme.
main()