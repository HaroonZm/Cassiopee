# Création d'un dictionnaire nommé 'dic' qui va stocker le nombre d'occurrences de chaque groupe sanguin.
# Les clés du dictionnaire sont les groupes sanguins possibles : 'A', 'B', 'AB', 'O'.
# Chaque clé est initialisée à la valeur entière 0.
dic = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}

# Mise en place d'une boucle infinie 'while True' pour continuer à lire des entrées utilisateur sans arrêt préalable connu.
while True:
    try:
        # Utilisation de 'raw_input()' pour lire une ligne depuis l'entrée standard.
        # L'entrée typique est supposée être au format 'nom,groupe', par exemple : 'Jean,A'
        s = raw_input()
        
        # La chaîne de caractères lue 's' est découpée en une liste à l'aide de la méthode 'split'.
        # Le séparateur utilisé est la virgule ','.
        # La sortie, 'sp', est une liste où
        # sp[0] = nom
        # sp[1] = groupe sanguin
        sp = s.split(',')
        
        # Incrémentation du compteur correspondant au groupe sanguin présent en sp[1].
        # On accède à la valeur courante du groupe dans le dictionnaire, et on l'augmente de un.
        dic[ sp[1] ] += 1;
        
    # Gestion de l'exception de fin de fichier (EOFError), qui se produit quand il n'y a plus d'entrée à lire.
    except EOFError:
        # Affichage du nombre d'occurrences pour chaque groupe sanguin sous la forme d'une chaîne de formatage.
        # L'ordre d'affichage est : 'A', 'B', 'AB', puis 'O', chacun sur une nouvelle ligne.
        print "%d\n%d\n%d\n%d" % (dic['A'], dic['B'], dic['AB'], dic['O'])
        # Le mot-clé 'break' permet de sortir de la boucle 'while', terminant ainsi le programme.
        break