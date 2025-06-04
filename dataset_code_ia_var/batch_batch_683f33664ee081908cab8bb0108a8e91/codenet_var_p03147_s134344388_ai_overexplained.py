# Demander à l'utilisateur d'entrer un nombre entier, qui représente le nombre d'éléments à traiter
n = int(input())

# Demander à l'utilisateur de saisir une séquence d'entiers (séparés par des espaces),
# les convertir en entiers grâce à map() et list()
h = list(map(int, input().split()))

# Créer une liste 'kadan' de longueur n, initialisée avec des zéros.
# Cette liste va servir à suivre la progression de l'arrosage de chaque plante.
kadan = [0 for _ in range(n)]

# Initialiser un compteur 'cnt' à zéro pour compter le nombre d'opérations effectuées.
cnt = 0

# Créer une liste 'tf' de longueur n, initialisée avec la valeur booléenne False.
# Cette liste indique si une plante a atteint la hauteur souhaitée (True) ou non (False).
tf = [False for _ in range(n)]

# Boucle principale, conçue pour s'exécuter un nombre très élevé de fois au maximum (10^5),
# mais en réalité elle s'arrête plus tôt car une condition de fin est prévue.
for i in range(1, 10**5):
    # À chaque nouvelle itération de la boucle, incrémenter le compteur d'opérations de 1.
    cnt += 1

    # La variable flg (drapeau) est initialisée à False à chaque tour.
    # Ce drapeau va servir à savoir si la portion de traitement de groupe d'herbe est en cours.
    flg = False

    # Commencer une boucle sur chaque plante (indexée par j)
    for j in range(n):
        # Vérifie si la plante actuelle n'a pas encore atteint la hauteur désirée.
        if tf[j] == False:
            # Comme tf[j] est False, cela veut dire qu'on va devoir traiter (arroser) cette plante.
            flg = True  # Signale qu'un début de séquence d'arrosage est trouvé (ou en cours).

            # Si la progression actuelle de la plante (kadan[j]) est égale à la hauteur cible (h[j]),
            if kadan[j] == h[j]:
                # Marquer la plante comme terminée (arrosée jusqu'à la bonne hauteur)
                tf[j] = True
            else:
                # Sinon, on incrémente l'arrosage de cette plante d'une unité.
                kadan[j] += 1

        # Si la plante est déjà à bonne hauteur
        elif tf[j] == True and flg == False:
            # Si aucune séquence d'arrosage n'est en cours (flg == False), on ne fait rien (pass)
            pass

        else:
            # Si on tombe ici, cela signifie qu'on a rencontré une zone où l'arrosage doit s'arrêter.
            # On cesse le traitement de la séquence actuelle d'arrosage.
            break

    # Après avoir fini le tour de toutes les plantes,
    # vérifier si elles sont toutes terminées (tous les tf[j] sont True)
    if not False in tf:
        # Si c'est le cas, arrêter la boucle principale car il n'y a plus rien à arroser.
        break

# Le nombre d'opérations (cnt) a été incrémenté une fois de trop à la fin, donc on affiche cnt-1.
print(cnt-1)