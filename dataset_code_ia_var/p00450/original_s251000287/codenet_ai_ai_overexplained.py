# Commencer une boucle infinie qui continuera de s'exécuter jusqu'à l'apparition d'un `break`
while (1):
    # Demander à l'utilisateur d’entrer une valeur, puis convertir cette entrée en entier grâce à int()
    # raw_input() lit une ligne de texte saisie par l'utilisateur (fonctionne en Python 2)
    n = int(raw_input())
    # Si l'entier entré 'n' est égal à 0, alors on sort de la boucle avec break
    if n == 0:
        break
    else:
        # Initialiser une variable 'top' à -1 ; cette variable va se souvenir de la 'pierre' précédente traitée
        top = -1
        # Créer une liste 'fault' initialisée avec un seul élément, 0 ; cette liste suivra les indices où une "faute" est détectée
        fault = [0]
        # Initialiser une variable S à 0 ; cette variable accumulera un certain score à calculer plus bas
        S = 0
        # Boucle for qui va de 0 à n/2 (attention, division entière en Python 2)
        # Cela signifie que pour chaque i, nous traitons deux entrées consécutives (pierres impaires et paires)
        for i in range(n / 2):
            # Lire une première entrée utilisateur (correspondant à une "pierre impaire"), la convertir en entier
            s = int(raw_input())
            # Si la dernière pierre traitée (top) est différente de la pierre actuelle (s)
            if top != s:
                # Ajouter l'indice actuel i à la liste 'fault', signalant qu'un changement est intervenu
                fault.append(i)
                # Mettre à jour 'top' avec le nouveau type de pierre (s)
                top = s
            # Lire la pierre suivante (pierre avec numéro pair), encore convertir en entier
            s = int(raw_input())
            # Si la dernière pierre traitée est différente de cette pierre
            if top != s:
                # Supprimer la dernière faute ajoutée car la pierre change encore
                fault.pop()
                # Mettre à jour 'top' sur la nouvelle valeur
                top = s
            # Si la liste 'fault' devient vide (ce qui est un cas particulier)
            if fault == []:
                # On la ré-initialise avec juste l'élément 0 pour éviter les erreurs plus tard
                fault = [0]
        # À la sortie de la boucle, 'fault' contient certains indices où les fautes ont commencé
        # i est défini comme le dernier indice valide de la liste 'fault' (longueur de fault moins 1)
        i = len(fault) - 1
        # Tant que i > 0 (pour parcourir la liste des indices de faute à l’envers, deux éléments à la fois)
        while i > 0:
            # Additionner à S la différence entre deux indices consécutifs dans fault (c'est le nombre d'éléments consécutifs entre ces fautes)
            # On multiplie par 2, probablement car chaque 'i' correspond à deux pierres
            S = S + (fault[i] - fault[i - 1]) * 2
            # Décrémenter i de 2 car on a traité une paire d'indices à chaque itération
            i = i - 2
        # Si la dernière pierre traitée (top) a une valeur "falsy" (typiquement 0 en Python), on ajuste le score S
        if not top:
            # Recalculer S en faisant 2 * (n / 2) moins la valeur précédente de S
            S = 2 * (n / 2) - S
        # Si n est impair (il reste une pierre à traiter à la fin du groupe)
        if n % 2 == 1:
            # On lit et convertit encore une pierre supplémentaire (la dernière pierre)
            s = int(raw_input())
            # Ajouter à S la différence entre 1 et s ; (ajoute 1 si la pierre vaut 0, rien si s est 1)
            S = S + (1 - s)
        # Affiche la valeur finale de S à l'écran (résultat accumulé ci-dessus)
        print S