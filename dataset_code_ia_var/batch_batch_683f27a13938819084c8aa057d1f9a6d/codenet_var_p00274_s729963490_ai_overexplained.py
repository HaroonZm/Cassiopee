# Démarre une boucle infinie utilisant 'while 1', ce qui fonctionne car 1 est toujours évalué comme 'True'.
while 1:
    # Prend une entrée de l'utilisateur avec la fonction 'input()', qui retourne une chaîne (string).
    # Convertit cette chaîne en entier avec 'int()' et assigne le résultat à la variable 'n'.
    n = int(input())
    
    # Vérifie si la valeur de 'n' est égale à 0 à l'aide de l'opérateur '=='.
    # Si c'est vrai, alors exécute 'break' pour sortir immédiatement de la boucle 'while', arrêtant ainsi le programme principal.
    if n == 0:
        break
    
    # Prend une nouvelle entrée utilisateur avec 'input()', qui attend une ligne contenant des entiers séparés par des espaces.
    # 'input().split()' sépare cette chaîne en une liste de sous-chaînes (liste de chaînes), où chaque élément correspond à un nombre.
    # 'map(int, ...)' applique la fonction 'int' à chaque sous-chaîne, transformant la liste de chaînes en liste d'entiers.
    # 'list(...)' convertit l'objet map en une liste Python contenant tous ces entiers.
    # La variable 'a' devient donc une liste d'entiers correspondant à l'entrée utilisateur.
    a = list(map(int, input().split()))
    
    # Calcule la valeur maximale de la liste 'a' avec la fonction 'max(a)'.
    # Vérifie ensuite si cette valeur maximale est strictement inférieure à 2 avec l'opérateur '<'.
    if max(a) < 2:
        # Si tous les éléments de la liste sont inférieurs à 2 (c'est-à-dire que le maximum < 2),
        # alors on affiche "NA" avec la fonction 'print()'.
        print("NA")
        # Utilise 'continue' pour passer immédiatement à l'itération suivante de la boucle 'while',
        # sautant ainsi les instructions en dessous pour cette itération.
        continue
    
    # Construit une liste filtrée via une 'list comprehension' qui parcourt chaque élément 'x' dans la liste 'a'.
    # Pour chaque 'x', la condition 'x > 0' est testée : si vraie, 'x' est inclus dans la nouvelle liste.
    # Cela crée ainsi une nouvelle liste ne contenant que les éléments STRICTEMENT POSITIFS.
    # 'len(...)' calcule le nombre d'éléments de cette nouvelle liste, soit le nombre de valeurs strictement positives dans 'a'.
    # On ajoute 1 à ce nombre (raison inconnue sans le contexte exact du problème).
    # Enfin, on affiche le résultat du calcul précédent avec 'print'.
    print(len([x for x in a if x > 0]) + 1)