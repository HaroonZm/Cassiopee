# Boucle infinie, elle continuera à s'exécuter tant que la condition est vraie. 
# Dans ce cas, la condition est simplement '1', ce qui est toujours évalué comme True en Python,
# donc cette boucle tourne indéfiniment jusqu'à ce qu'on utilise une instruction break pour sortir.
while 1:
    
    # On lit une entrée utilisateur avec input(), qui retourne toujours une chaîne de caractères.
    # On convertit cette chaîne en entier avec int(), sinon on ne pourrait pas faire des opérations mathématiques.
    a=int(input())
    
    # Ici, on vérifie si la valeur entrée est égale à zéro.
    # Si c'est le cas, on utilise break pour sortir de la boucle infinie et arrêter l'exécution du programme.
    if a == 0:
        break
    
    # On lit une nouvelle valeur entière 'b' depuis l'entrée utilisateur exactement comme pour 'a'.
    b=int(input())
    
    # Initialisation d'une variable 'd' à zéro.
    # Cette variable servira à accumuler un total qui sera calculé dans la boucle suivante.
    d=0
    
    # Boucle for qui s'exécute exactement 'b' fois.
    # La variable _ est conventionnellement utilisée lorsqu'on n'a pas besoin de la variable de boucle.
    for _ in range(b):
        
        # On lit une ligne d'entrée utilisateur avec input(), 
        # on sépare la chaîne en morceaux avec split() (par défaut, séparation par espaces),
        # on convertit chacun des morceaux en int avec map(int, ...),
        # puis on convertit le résultat en liste pour pouvoir accéder aux éléments par index.
        c=list(map(int,input().split()))
        
        # On calcule la différence entre le deuxième élément (index 1) et le premier élément (index 0) de la liste 'c'.
        # On ajoute cette différence à la variable 'd' pour accumuler le total.
        d += c[1] - c[0]
    
    # Condition ternaire : 
    # Si 'a' est strictement supérieur à 'd', on affiche la différence 'a - d'.
    # Sinon, on affiche la chaîne de caractères 'OK'.
    print(a - d if a > d else 'OK')