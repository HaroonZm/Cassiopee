# Définition et initialisation d'un dictionnaire nommé "dic"
# Un dictionnaire en Python est une structure de données qui stocke des paires clé-valeur.
# Ici, chaque clé représente un type de groupe sanguin ('A', 'B', 'AB', 'O')
# et chaque valeur initialize à 0 va compter le nombre d'occurrences de ce groupe.
dic = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}

# Début d'une boucle infinie qui va s'exécuter indéfiniment jusqu'à ce qu'on casse la boucle manuellement
# Une boucle infinie est une boucle qui tourne sans condition d'arrêt explicite dans la structure while.
while True:
    # Utilisation d'un bloc try-except pour gérer les erreurs possibles lors de l'exécution du code à l'intérieur de try
    # Ici, on va essayer de lire des entrées utilisateur et les traiter.
    try:
        # Lecture d'une ligne depuis l'entrée standard (clavier ou fichier redirigé)
        # La fonction raw_input() attend que l'utilisateur tape quelque chose et appuie sur Entrée.
        s = raw_input()
        
        # On prend la chaîne lue (s), on la découpe en une liste de sous-chaînes
        # en utilisant la virgule ',' comme séparateur.
        # La méthode split() retourne une liste. Par exemple, "Jean,A" devient ['Jean', 'A'].
        sp = s.split(',')
        
        # On accède au deuxième élément de la liste sp (index 1, car l'indexation commence à 0)
        # qui correspond au groupe sanguin fourni dans l'entrée.
        # On incremente la valeur associée à cette clé dans le dictionnaire dic.
        # Le signe += 1 signifie qu'on ajoute 1 à la valeur déjà présente.
        dic[ sp[1] ] += 1;
        
    # Le bloc except capture l'exception spécifique EOFError, qui se déclenche quand il n'y a plus de donnée à lire.
    # Cette erreur est levée quand raw_input() ne reçoit plus rien car la fin de fichier (EOF) est atteint.
    except EOFError:
        # Quand on arrive ici, cela signifie qu'on a terminé de lire toutes les entrées.
        # On imprime alors les totaux des différents groupes sanguins comptés.
        # Le mot-clé print affiche une chaîne formatée. 
        # "%d" est un format pour un entier, et les valeurs entre parenthèses sont insérées dans cette chaîne dans l'ordre.
        # Les \n sont des caractères spéciaux qui indiquent un retour à la ligne.
        print "%d\n%d\n%d\n%d" % (dic['A'], dic['B'], dic['AB'], dic['O'])
        
        # Cette instruction break sert à interrompre la boucle infinie while True,
        # ce qui permet de terminer proprement le programme.
        break