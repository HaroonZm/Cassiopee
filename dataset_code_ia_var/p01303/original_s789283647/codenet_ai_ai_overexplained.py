# La première ligne du code ci-dessous nous demande d'exécuter une boucle for un certain nombre de fois
# 'input()' lit une entrée de l'utilisateur depuis le clavier et retourne une chaîne qui est ensuite convertie en entier grâce à la fonction implicite de Python 2
# 'range(input())' crée une séquence de nombres de 0 jusqu'à l'entier fourni (non inclus), ce qui permet de répéter les instructions suivantes ce nombre de fois
for i in range(input()):
    # Ici, on lit une ligne de l'utilisateur, représentant quatre entiers séparés par des espaces
    # 'raw_input()' lit une ligne d'entrée sous forme de chaîne de caractères (chaîne brute, non pré-évaluée)
    # '.split()' divise cette chaîne en une liste de sous-chaînes selon les espaces trouvés
    # 'map(int, ...)' applique la fonction int à chaque élément de la liste, transformant chaque sous-chaîne en entier
    # Finalement, les 4 entiers sont respectivement assignés aux variables X, Y, W, H
    X, Y, W, H = map(int, raw_input().split())
    
    # Initialisation d'un compteur à zéro.
    # Le compteur 'cnt' servira à compter combien de points se trouvent à l'intérieur (ou au bord) du rectangle
    cnt = 0
    
    # On lit ensuite un nouvel entier de l'utilisateur, qui va correspondre au nombre de points à considérer
    N = input()
    
    # Nous entrons maintenant dans une seconde boucle for afin de lire et traiter chaque point individuellement
    # Cette boucle va itérer 'N' fois, soit une fois par point à analyser
    for i in range(N):
        # Ici, on lit encore une fois une ligne contenant deux entiers séparés par un espace par point
        # On utilise la même logique que précédemment: on divise la ligne en sous-chaînes puis on convertit en entiers
        x, y = map(int, raw_input().split())
        
        # Nous vérifions à présent si le point (x, y) se situe à l'intérieur ou sur le bord du rectangle défini par (X, Y, W, H)
        # X <= x <= X + W vérifie si la coordonnée x du point est comprise (ou égale) entre la limite gauche (X) et la limite droite (X + W) du rectangle
        # Y <= y <= Y + H vérifie si la coordonnée y du point est comprise (ou égale) entre la limite inférieure (Y) et la limite supérieure (Y + H) du rectangle
        # Les deux conditions doivent être vérifiées simultanément, c'est pourquoi on utilise l'opérateur 'and'
        if (X <= x <= X + W) and (Y <= y <= Y + H):
            # Si la condition est vraie, on incrémente le compteur de 1 avec l'opérateur += qui ajoute 1 à la valeur actuelle de cnt
            cnt += 1
    
    # Une fois que tous les points ont été analysés pour un jeu de données (données d'une itération de la boucle externe),
    # on affiche le nombre total de points qui sont à l'intérieur ou sur le bord du rectangle
    print cnt