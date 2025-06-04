# Boucle infinie, le programme continue de tourner jusqu'à ce qu'on le quitte explicitement
while True:
    # Demande à l'utilisateur une entrée composée de trois entiers séparés par des espaces, puis les assigne à n, w, et h
    n, w, h = map(int, input().split())
    
    # Si la largeur (w) est égale à zéro, cela signifie qu'on veut arrêter le programme donc on sort de la boucle
    if w == 0:
        break  # sort de la boucle while et donc arrête le programme
    
    # Création d'une liste ls contenant une sous-liste avec les valeurs initiales de largeur et hauteur
    # La liste ls va contenir les rectangles (ou morceaux restants) sous forme [largeur, hauteur]
    ls = [[w, h]]
    
    # On va répéter le processus n fois, une fois pour chaque découpe spécifiée dans les entrées suivantes
    for i in range(n):
        # Récupère la position (p) du morceau à découper et la distance (s) pour déterminer où le couper
        p, s = map(int, input().split())
        # Correction de l'indice de découpe (passage de base 1 à base 0, car ls utilise les indices comme en C)
        p -= 1
        
        # Récupère la largeur et la hauteur du morceau à découper depuis ls à l'indice p
        pw, ph = ls[p]
        
        # Détermine si la coupe se passe sur le côté supérieur/inférieur (horizontale) ou latéral (verticale)
        if s % (pw + ph) < pw:
            # Si le reste de la division de s par (pw + ph) est inférieur à pw, la coupe est effectuée horizontalement
            # s est normalisé au périmètre du rectangle (pw + ph)
            s %= (pw + ph)
            # Crée deux nouveaux morceaux après la coupe horizontale
            # Le min et le max permettent de définir la largeur de chaque nouveau morceau
            ls.extend([
                [min(s, pw - s), ph],  # Premier morceau : largeur min(s, pw - s), hauteur identique
                [max(s, pw - s), ph]   # Deuxième morceau : largeur max(s, pw - s), hauteur identique
            ])
        else:
            # Sinon la coupe est effectuée verticalement
            # Ajuste s en retirant pw pour ignorer la partie supérieure déjà couverte
            s = (s - pw) % (ph + pw)
            # Crée deux nouveaux morceaux après la coupe verticale
            # Le min et le max servent à séparer la hauteur des nouveaux rectangles
            ls.extend([
                [pw, min(s, ph - s)],  # Premier morceau : largeur identique, hauteur min(s, ph - s)
                [pw, max(s, ph - s)]   # Deuxième morceau : largeur identique, hauteur max(s, ph - s)
            ])
        
        # Supprime de ls l'ancien morceau (celui qui vient d'être découpé)
        ls.pop(p)
    
    # Calcul de l'aire de chaque morceau restant dans ls (largeur * hauteur)
    ans = [hi * wi for wi, hi in ls]
    
    # Trie la liste des aires obtenues dans l'ordre croissant pour faciliter la lecture
    ans.sort()
    
    # Affiche les aires triées, séparées par un espace, sur la même ligne
    print(' '.join(map(str, ans)))  # convertit chaque entier en chaîne, puis les joint avec des espaces