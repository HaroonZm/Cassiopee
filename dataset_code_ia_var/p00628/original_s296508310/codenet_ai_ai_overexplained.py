# Démarrage d'une boucle infinie ; cela signifie que le code à l'intérieur sera exécuté à répétition jusqu'à ce qu'une instruction break mette fin à la boucle.
while True:
    # Lecture d'une chaîne de caractères depuis l'entrée standard (le clavier).
    # La fonction input() permet à l'utilisateur de saisir du texte.
    string = input()
    # Vérification si la chaîne saisie correspond exactement à 'END OF INPUT'.
    # L'opérateur == compare l'égalité entre deux valeurs.
    if string == 'END OF INPUT':
        # Si la condition précédente est vraie, l'instruction break termine immédiatement la boucle la plus proche (ici le while True).
        break

    # Initialisation d'une liste vide appelée 'ans'.
    # Cette liste va servir à stocker des entiers représentant la longueur des mots dans la chaîne saisie.
    ans = []
    # Initialisation de la variable 'temp' à 0. Cette variable va compter le nombre de caractères consécutifs ne constituant pas un espace (donc appartenant au même mot).
    temp = 0
    # Initialisation de la variable 'space' à 0. Cette variable agit comme un indicateur (flag) pour savoir si le caractère précédent était un espace.
    space = 0

    # On parcourt la chaîne caractère par caractère en utilisant son indice avec la fonction range().
    # len(string) donne le nombre de caractères de 'string', et range(len(string)) génère tous les indices valides de la chaîne.
    for i in range(len(string)):
        # Vérifie si le caractère courant est un espace ' ' et que le flag 'space' vaut 0 (donc le précédent n'est pas un espace).
        if string[i] == ' ' and space == 0:
            # Si c'est le cas, on ajoute la valeur de 'temp' (qui contient ici la taille d'un mot) à la liste 'ans'.
            ans.append(temp)
            # On remet 'temp' à 0 pour commencer à compter un nouveau mot s'il y en a un après cet espace.
            temp = 0
            # On règle le flag 'space' à 1 pour indiquer qu'on vient de traiter un espace.
            space = 1
            # continue permet de passer à l'itération suivante de la boucle sans exécuter le reste du code à la suite dans la boucle.
            continue
        # On vérifie un autre cas : si on a déjà rencontré un espace juste avant (space > 0) et on tombe encore sur un espace.
        elif space > 0 and string[i] == ' ':
            # On ajoute un zéro à 'ans', représentant un mot de longueur nulle (conséquence de deux espaces successifs).
            ans.append(0)
            # continue pour passer directement à l'itération suivante.
            continue
        # Si les cas précédents ne s'appliquent pas, cela signifie que le caractère courant n'est pas un espace.
        # Donc, on remet le flag 'space' à 0 pour indiquer ce fait.
        space = 0
        # On incrémente 'temp' de 1 pour compter ce caractère comme faisant partie du mot courant.
        temp += 1
    # Après la boucle, il peut rester un dernier mot ou une suite de caractères non traités,
    # donc on ajoute le compteur 'temp' à la liste 'ans'.
    ans.append(temp)
    # On va maintenant afficher le résultat.
    # La compréhension de liste [str(x) for x in ans] convertit tous les éléments de 'ans' (qui sont des entiers) en chaînes de caractères.
    # Ensuite, la méthode join() concatène tous ces éléments dans une seule chaîne, sans séparateur (chaîne vide '').
    print(''.join([str(x) for x in ans]))