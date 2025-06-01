# Boucle infinie pour répéter le processus jusqu'à une condition d'arrêt spécifique
while 1:
    # Lecture et conversion de la première entrée utilisateur en entier, stockée dans la variable 'n'
    n = int(input())
    # Lecture et conversion de la deuxième entrée utilisateur en entier, stockée dans la variable 'm'
    m = int(input())
    
    # Vérification simultanée si 'n' et 'm' sont tous les deux égaux à zéro
    # Cette condition sert de signal pour sortir de la boucle infinie et arrêter le programme
    if n == m == 0:
        break  # Arrête la boucle while dès que la condition ci-dessus est satisfaite
    
    # Initialisation d'une liste vide 'a' qui contiendra des paires d'entiers
    a = []
    
    # Boucle itérant 'm' fois, correspondant au nombre d'entrées suivantes à lire
    for i in range(m):
        # Lecture d'une ligne d'input, séparant la chaîne en plusieurs parties selon les espaces
        # Conversion de ces parties en entiers et assignation aux variables 'x' et 'y'
        x, y = map(int, input().split())
        # Ajout de la paire [x, y] comme une liste à la liste 'a'
        a.append([x, y])
    
    # Tri de la liste 'a' en place, utilisant comme clé de tri la première valeur de chaque sous-liste
    # La fonction lambda prend un élément de la liste 'a' (qui est une liste [x, y]) et retourne x
    a.sort(key=lambda x: x[0])
    
    # Initialisation de deux listes vides qui seront utilisées pour stocker certaines valeurs
    f1 = []
    f2 = []
    
    # Boucle itérant sur chaque élément index 'i' dans la liste 'a'
    for i in range(m):
        # Si la première valeur de la paire est 1
        if a[i][0] == 1:
            # On ajoute la deuxième valeur de la paire à la liste f1
            f1.append(a[i][1])
        # Sinon, si la première valeur de la paire est déjà dans f1,
        # et que la deuxième valeur n'est ni dans f1 ni dans f2
        elif a[i][0] in f1 and not (a[i][1] in f1) and not (a[i][1] in f2):
            # Ajouter la deuxième valeur à la liste f2
            f2.append(a[i][1])
        # Sinon, si la deuxième valeur est dans f1,
        # et que la première valeur n'est ni dans f1 ni dans f2
        elif a[i][1] in f1 and not (a[i][0] in f1) and not (a[i][0] in f2):
            # Ajouter la première valeur à la liste f2
            f2.append(a[i][0])
    
    # Affiche la somme du nombre d'éléments dans la liste f1 et dans la liste f2
    # Cela représente un total calculé selon la logique précédente
    print(len(f1) + len(f2))