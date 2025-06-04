# Début d'une boucle while qui ne s'arrête jamais sauf en cas de 'break' explicite
while(1):
    # Demande à l'utilisateur de saisir une chaîne de caractères et la stocke dans la variable 'up'
    # raw_input() lit une ligne depuis l'entrée standard (console) en tant que chaîne de caractères (en Python 2)
    up = raw_input()
    # Si l'entrée utilisateur pour 'up' est le caractère '-', alors on considère que l'utilisateur veut arrêter la boucle
    if up == '-':
        break  # On sort alors immédiatement de la boucle while avec 'break'
    # Demande à l'utilisateur de saisir une chaîne de caractères et la stocke dans la variable 'left'
    left = raw_input()
    # Demande à l'utilisateur de saisir une chaîne de caractères et la stocke dans la variable 'down'
    down = raw_input()
    
    # Initialise la variable 'cen' (centre) avec le 1er caractère de la chaîne 'left'
    # L'index 0 est toujours le 1er caractère d'une chaîne en Python
    cen = left[0]
    # Initialise l'indice utilisé pour parcourir la chaîne 'up' à 0, avant le début du parcours
    idu = 0
    # Initialise l'indice utilisé pour parcourir la chaîne 'down' à 0
    idd = 0
    # Initialise l'indice utilisé pour parcourir la chaîne 'left' à 0
    idl = 0
    # Initialise la variable de résultat 'ans' comme une chaîne vide qui contiendra le résultat final
    ans = ''

    # Boucle for avec 'i' comme variable de boucle. La boucle s'exécute un nombre fixe de fois :
    # - de 0 jusqu'à (len(up) + len(left) - 1) exclu, soit (len(up) + len(left) - 1) tours de boucle
    for i in range(len(up) + len(left) - 1):
        # La condition suivante compare le caractère de la chaîne 'down' à l'indice 'idd'
        # avec le caractère courant 'cen'
        # Si ils sont égaux, on exécute le cercle "descendre" vers 'up'
        if down[idd] == cen: # On compare et décide si on doit "descendre"
            # On met à jour 'cen' pour qu'il prenne la valeur du caractère suivant de la chaîne 'up'
            cen = up[idu]
            # On passe à l'indice suivant de 'up'
            idu += 1
            # On passe aussi à l'indice suivant dans la chaîne 'down', en s'assurant de ne pas dépasser la taille de 'down'
            # On utilise min(...) pour ne jamais dépasser la taille maximale possible (len(down) - 1)
            idd = min(idd + 1, len(down) - 1)
        else:
            # Si la précédente condition n'est pas remplie, on ajoute le caractère courant 'cen'
            # à la chaîne de résultat 'ans'
            ans += cen
            # On passe à l'indice suivant de 'left'
            idl += 1
            # On met à jour 'cen' avec la valeur du caractère de 'left' à la nouvelle position 'idl'
            cen = left[idl]
    # Après la boucle, on ajoute encore le caractère courant 'cen' à la chaîne 'ans'
    ans += cen
    # Affiche le résultat final construit, c'est-à-dire la nouvelle chaîne sous la forme calculée
    print ans