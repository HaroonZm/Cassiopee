# Lire les valeurs N et D à partir de l'entrée standard
# input() lit une seule ligne en tant que chaîne de caractères
# split() divise cette chaîne en une liste de sous-chaînes en se basant sur les espaces
# map(int, ...) convertit chaque sous-chaîne en un entier
# Enfin, on utilise l'affectation multiple pour assigner les deux entiers aux variables N et D respectivement
N, D = map(int, input().split())

# Initialiser la variable time qui sert à stocker le dernier instant traité
# On commence à 0, supposant que l'action commence à l'instant 0
time = 0

# Initialiser la variable floor pour mémoriser l'étage actuel. On commence au premier étage.
floor = 1

# num va compter le nombre d'actions ou de personnes (suivant le contexte) à chaque étape
num = 0

# result va accumuler la valeur finale ou le résultat global calculé, selon la logique du code
result = 0

# Boucle for pour itérer N fois (N étant le nombre d'actions ou d'éléments à traiter)
# [0]*N crée une liste contenant N zéros. On n'utilise pas la valeur de chaque élément, seulement le nombre d'itérations.
# Le caractère "_" est une variable spéciale généralement utilisée lorsqu'on n'a pas besoin de la valeur.
for _ in [0]*N:
    # Lire deux entiers à partir de l'entrée standard à chaque itération
    # Ils sont respectivement attribués à t (le temps cible) et f (l'étage cible)
    t, f = map(int, input().split())
    
    # Première condition: Est-ce qu'on peut se déplacer directement à l'étage cible depuis l'étage actuel ?
    # On analyse si on peut atteindre l'étage de destination (f) en partant de l'étage courant (floor)
    # On calcule combien d'étages on doit monter : (floor-1) pour se mettre au rez-de-chaussée, puis (f-1) pour aller à l'étage f
    # On compare ce total avec le temps disponible (t - time)
    if floor-1+f-1 <= t-time:
        # Si on peut y arriver :
        # On ajoute au résultat la valeur actuelle de num multipliée par le nombre d'étages à monter (floor-1)
        result += num * (floor-1)
        # On remet num à 1, car on démarre une nouvelle action ou groupe
        num = 1
        
    # Deuxième condition: Est-ce qu'on peut se déplacer directement d'un étage à un autre dans le temps imparti ?
    # Ici, on vérifie le nombre d'étages à parcourir (la différence absolue entre les étages actuel et cible)
    # et si on n'a pas encore atteint la limite D (par exemple, de personnes/groupe)
    elif abs(floor-f) <= t-time and num < D:
        # Si on peut :
        # On ajoute au résultat num fois la durée écoulée (t - time)
        result += num * abs(t-time)
        # On incrémente num car on a ajouté quelqu'un ou fait une action de plus dans le groupe
        num += 1
        
    # Si aucune des conditions précédentes n'est remplie, on ne peut pas réaliser l'action demandée
    else:
        # On affiche -1 pour indiquer une impossibilité ou une erreur
        print(-1)
        # On quitte la boucle for de manière prématurée grâce à break
        break
        
    # On met à jour time et floor à la fin de chaque itération
    # Ces variables retiennent respectivement le dernier temps traité et l'étage sur lequel on se trouve
    time, floor = t, f

# Le bloc else après une boucle for n'est exécuté que si la boucle s'est terminée sans interruption (sans break)
else:
    # On ajoute au résultat final le dernier calcul éventuel (num fois le nombre d'étages à monter à la fin)
    result += num * (floor-1)
    # On affiche le résultat final
    print(result)