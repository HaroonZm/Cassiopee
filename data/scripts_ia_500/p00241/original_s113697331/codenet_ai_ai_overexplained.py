# Début d'une boucle infinie qui continuera à s'exécuter jusqu'à rencontre d'une condition de sortie explicite
while True:
    # Demande à l'utilisateur de saisir une valeur, la fonction input() récupère une chaîne de caractères
    # int() convertit cette chaîne en un entier
    n = int(input())
    
    # Condition pour sortir de la boucle infinie : si la valeur saisie est 0
    # 'break' termine immédiatement la boucle
    if n == 0:
        break
    
    # Boucle qui s'exécute n fois, où n est le nombre que l'utilisateur a saisi précédemment
    # range(n) crée une séquence de nombres allant de 0 à n-1
    for i in range(n):
        # Lecture d'une ligne de saisie contenant plusieurs nombres séparés par des espaces
        # input().split() découpe cette chaîne en une liste de sous-chaînes
        # map(int, ...) applique la fonction int à chaque élément de la liste, convertissant chaque sous-chaîne en entier
        # on affecte ensuite ces entiers aux variables x1, y1, z1, w1, x2, y2, z2, w2 dans cet ordre
        x1, y1, z1, w1, x2, y2, z2, w2 = map(int, input().split())
        
        # Calcul des composantes résultantes selon des formules spécifiques (probablement multiplication de quaternions)
        # Chaque parenthèse correspond à l'expression pour une composante finale (x, y, z, w)
        
        # Première composante calculée : (x1*x2 - y1*y2 - z1*z2 - w1*w2)
        composante_x = (x1 * x2 - y1 * y2 - z1 * z2 - w1 * w2)
        # Seconde composante calculée : (x1*y2 + x2*y1 + z1*w2 - z2*w1)
        composante_y = (x1 * y2 + x2 * y1 + z1 * w2 - z2 * w1)
        # Troisième composante calculée : (x1*z2 - y1*w2 + x2*z1 + y2*w1)
        composante_z = (x1 * z2 - y1 * w2 + x2 * z1 + y2 * w1)
        # Quatrième composante calculée : (x1*w2 + y1*z2 - y2*z1 + x2*w1)
        composante_w = (x1 * w2 + y1 * z2 - y2 * z1 + x2 * w1)
        
        # Affichage des quatre composantes calculées sur la même ligne, séparées par des espaces par défaut
        # print() convertit automatiquement les entiers en chaînes pour l'affichage
        print(composante_x, composante_y, composante_z, composante_w)