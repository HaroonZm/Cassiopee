# Boucle infinie qui permet de répéter indéfiniment les instructions suivantes jusqu'à ce qu'on rencontre une condition d'arrêt explicite
while True:
    # On demande à l'utilisateur de saisir une valeur qui sera convertie en nombre entier et stockée dans la variable 'n'
    # input() récupère une chaîne de caractères entrée par l'utilisateur
    # int() convertit cette chaîne en un entier, ce qui est nécessaire pour pouvoir utiliser 'n' dans une boucle for
    n = int(input())
    
    # Condition qui vérifie si la variable 'n' est égale à 0
    # Si c'est le cas, cela signifie qu'on souhaite arrêter la boucle infinie
    # La commande 'break' interrompt immédiatement la boucle while en cours
    if n == 0:
        break
    
    # Boucle 'for' qui va s'exécuter 'n' fois, de 0 jusqu'à n-1
    # 'i' est une variable qui prend successivement les valeurs de cette plage mais n'est pas utilisée dans le corps de la boucle
    for i in range(n):
        # Dans chaque itération, on lit une ligne de l'utilisateur contenant trois nombres séparés par des espaces
        # input() récupère cette ligne en tant que chaîne de caractères
        # split() découpe cette chaîne en une liste de sous-chaînes, séparées par l'espace par défaut
        # map(int, ...) applique la fonction int à chaque élément de la liste pour convertir chaque sous-chaîne en entier
        # Enfin, l'expression entière est décompressée en trois variables m, e, j, qui contiennent les trois notes saisies
        m, e, j = map(int, input().split())
        
        # Plusieurs conditions sont testées dans un ordre précis pour décider quelle lettre afficher selon les notes
        
        # Si au moins une des notes est parfaite (100), alors on affiche la meilleure note, 'A'
        if m == 100 or e == 100 or j == 100:
            print("A")
        
        # Sinon, si la moyenne des deux premières notes m et e est supérieure ou égale à 90, on affiche 'A'
        elif (m + e) / 2 >= 90:
            print("A")
        
        # Sinon, si la moyenne des trois notes m, e et j est supérieure ou égale à 80, on affiche 'A'
        elif (m + e + j) / 3 >= 80:
            print("A")
        
        # Sinon, si la moyenne des trois notes est supérieure ou égale à 70, on affiche 'B'
        elif (m + e + j) / 3 >= 70:
            print("B")
        
        # Sinon, si la moyenne des trois notes est supérieure ou égale à 50 ET que l'une des deux premières notes est au moins 80,
        # alors on affiche 'B'
        elif (m + e + j) / 3 >= 50 and (m >= 80 or e >= 80):
            print("B")
        
        # Si aucune des conditions précédentes ne s'est vérifiée, alors on affiche 'C'
        else:
            print("C")