# Demander à l'utilisateur d'entrer un nombre entier et stocker cette valeur dans la variable d
# Cette variable 'd' représente le nombre de cas ou d'itérations qui vont suivre
d = int(input())

# Démarrer une boucle 'for' dont la variable d'itération est 'i'
# Cette boucle va s'exécuter autant de fois que la valeur de 'd'
for i in range(d):
    # Demander à l'utilisateur d'entrer quatre entiers séparés par des espaces
    # Les quatre valeurs entrées sont placées dans la variable temporaire sous forme de string
    # 'input()' lit l'entrée utilisateur. 'split()' divise la chaîne selon les espaces
    # 'map(int, ...)' convertit chaque élément de la liste obtenue en entier
    # Les quatre valeurs sont ensuite assignées, dans l'ordre, aux variables X, Y, W, H
    X, Y, W, H = map(int, input().split())
    
    # Initialiser une variable 'count' avec la valeur zéro
    # Cette variable va servir à compter combien de points se situent dans la zone définie par X, Y, W, H
    count = 0
    
    # Demander à l'utilisateur d'entrer un entier supplémentaire qui correspond au nombre de points à tester
    # La valeur entrée est convertie en entier et stockée dans la variable 'n'
    n = int(input())
    
    # Démarrer une seconde boucle 'for' dont la variable d'itération est 'j'
    # Cette boucle va s'exécuter exactement 'n' fois, une fois par point à tester
    for j in range(n):
        # À chaque itération, demander à l'utilisateur d'entrer deux entiers séparés par des espaces
        # Ces entiers représentent les coordonnées du point en abscisse (x) et ordonnée (y)
        # L'entrée est divisée puis convertie en entiers avec 'map(int, ...)', puis assignée à x et y
        x, y = map(int, input().split())
        
        # Vérifier si le point (x, y) est inclus dans le rectangle défini par le coin supérieur gauche (X, Y) 
        # et d'une largeur W et hauteur H. On suppose que le rectangle comprend ses bords.
        # Condition : x doit être supérieur ou égal à X ET inférieur ou égal à X+W
        #             y doit être supérieur ou égal à Y ET inférieur ou égal à Y+H
        if X <= x <= X + W and Y <= y <= Y + H:
            # Si la condition est vraie, alors le point est à l'intérieur ou sur le bord du rectangle
            # On incrémente le compteur 'count' de 1 en utilisant l'opérateur +=
            count += 1
    
    # Après avoir testé tous les points pour ce cas, afficher la valeur du compteur 'count'
    print(count)