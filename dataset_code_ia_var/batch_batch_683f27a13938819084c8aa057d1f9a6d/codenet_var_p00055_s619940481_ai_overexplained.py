# Commencer une boucle infinie qui s'exécutera continuellement jusqu'à ce qu'elle soit explicitement arrêtée par une commande break.
while True:
    # Utiliser un bloc try-except pour capturer les exceptions qui pourraient se produire,
    # notamment EOFError lors de la lecture des entrées utilisateurs.
    try:
        # Demander à l'utilisateur de saisir une entrée via la fonction input().
        # input() retourne une chaîne de caractères (str).
        # float() convertit la chaîne d'entrée en un nombre décimal à virgule flottante.
        # Le résultat est stocké dans la variable 'a'.
        a = float(input())
        
        # Initialiser la variable 'Sum' à 0.
        # Cette variable va accumuler la somme des résultats produits dans la boucle for suivante.
        Sum = 0
        
        # Calculer la valeur initiale de 'retu' en multipliant 'a' par 3.
        # Cette variable sera modifiée à chaque itération de la boucle for.
        retu = 3 * a
        
        # Démarrer une boucle for qui va s'exécuter 10 fois.
        # range(10) génère une séquence de nombres de 0 à 9 (au total 10 nombres).
        for i in range(10):
            # Vérifier si l'indice actuel 'i' est un nombre pair.
            # i % 2 == 0 évalue si le reste de la division de 'i' par 2 est zéro.
            if i % 2 == 0:
                # Si 'i' est pair, diviser la valeur courante de 'retu' par 3.
                retu = retu / 3
            else:
                # Si 'i' est impair, multiplier 'retu' par 2.
                retu = retu * 2
            # Ajouter (additionner) la valeur de 'retu' calculée à chaque itération à la variable 'Sum'.
            Sum += retu
        # Une fois la boucle for terminée, afficher le résultat final de la somme.
        print(Sum)
    # Ce bloc except capture l'exception EOFError, qui peut se produire si la fonction input()
    # n'a plus de données à lire (par exemple, fin de fichier (Ctrl+D)).
    except EOFError:
        # Sortir de la boucle while en utilisant break, ce qui arrête complètement la boucle infinie.
        break