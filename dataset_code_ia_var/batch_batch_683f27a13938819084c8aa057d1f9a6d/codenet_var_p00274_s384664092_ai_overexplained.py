# Démarre une boucle infinie. Cela signifie que le code à l'intérieur de cette boucle s'exécutera encore et encore, sauf si une instruction explicite provoque la sortie de la boucle (comme "break").
while True :
    # Demande à l'utilisateur d'entrer une valeur sur la console. La fonction input() lit la totalité de la ligne saisie par l'utilisateur.
    # Par défaut, input() retourne une chaîne de caractères (str), donc on transforme ce résultat avec la fonction int() pour le convertir en entier.
    n = int(input())
    
    # Vérifie si la valeur saisie par l'utilisateur (contenue dans la variable n) est égale à 0.
    # Si c'est le cas :
    if n == 0 :
        # L'instruction break provoque la sortie immédiate de la boucle la plus proche (ici, le while True).
        break
    
    # Demande à nouveau à l'utilisateur de saisir une ligne de texte. Cette fois, on attend une suite de nombres séparés par des espaces.
    # input() retourne donc une chaîne, par exemple : "5 0 1 2"
    # La méthode split() sans argument découpe cette chaîne sur les espaces, retournant une liste de sous-chaînes par exemple ['5', '0', '1', '2']
    # map(int, ...) applique la fonction int (conversion en entier) à chaque élément de la liste précédente, retournant ainsi un itérable de nombres entiers.
    # La fonction list() convertit enfin cet itérable en liste d'entiers, par exemple : [5, 0, 1, 2]
    s = list(map(int, input().split()))
    
    # La fonction max() retourne la plus grande valeur dans la séquence s. Ici, on vérifie si tous les éléments de la liste sont inférieurs à 2.
    # Si c'est le cas, c'est-à-dire aucun élément supérieur ou égal à 2, la condition max(s) < 2 sera vraie.
    if max(s) < 2 :
        # Si la condition précédente est vraie, on affiche la chaîne 'NA' sur la console avec la fonction print().
        print('NA')
    else :
        # Si la condition max(s) < 2 est fausse (donc si au moins un nombre dans la liste est supérieur ou égal à 2), on entre dans ce bloc.
        # La méthode count(0) sur la liste s retourne le nombre de fois où la valeur 0 appraît dans la liste.
        t = s.count(0)
        # Calcule la différence entre le nombre total d'éléments n et le nombre de zéros t, ajoute 1 à ce résultat,
        # puis affiche ce nombre sur la console. Le calcul est donc : (nombre total d'éléments - nombre de zéros) + 1
        print(n - t + 1)