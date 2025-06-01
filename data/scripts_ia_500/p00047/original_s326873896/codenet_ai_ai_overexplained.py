# Initialisation de la variable 'now' avec la chaîne de caractères 'A'.
# Cette variable représente un état ou une position initiale qui va évoluer au cours de l'exécution du programme.
now = 'A'

# Début d'une boucle infinie. Cette boucle va continuer à s'exécuter sans fin jusqu'à ce qu'une instruction explicite mette fin à la boucle.
while True :
    # Le bloc 'try' est utilisé pour tenter d'exécuter un code qui pourrait potentiellement générer une erreur.
    # Si une erreur survient dans ce bloc, le programme passera au bloc 'except' pour gérer cette erreur sans planter.
    try :
        # Lecture d'une ligne depuis l'entrée standard (typiquement le clavier).
        # La méthode input() récupère une chaîne de caractères saisie par l'utilisateur.
        # La méthode split(',') divise cette chaîne en une liste de sous-chaînes, séparées par la virgule.
        # Par exemple, si l'utilisateur saisit "A,B", split(',') retournera la liste ['A', 'B'].
        # La syntaxe 'a, b =' permet d'affecter directement les deux éléments de cette liste aux variables 'a' et 'b'.
        a, b = input().split(',')

        # Vérification si la variable 'now' est strictement égale à la variable 'a'.
        # L'opérateur '==' compare les contenus des deux chaînes de caractères.
        # Si la condition est vraie, on met à jour la variable 'now' avec la valeur de 'b'.
        if   now == a : 
            now = b
        # Sinon, on vérifie si 'now' est égale à 'b'.
        # Si c'est le cas, on met à jour 'now' avec la valeur de 'a'.
        elif now == b : 
            now = a

    # Le bloc 'except' intercepte toute exception (erreur) qui pourrait survenir dans le bloc 'try'.
    # Ici, aucune exception spécifique n'est mentionnée, donc toutes les exceptions seront capturées.
    # Cela sert à détecter par exemple si l'utilisateur n'a pas entré de données ou s'il a entré une chaîne non conforme,
    # ce qui provoquerait une erreur lors de la décomposition en 'a, b'.
    # Dans ce cas, on sort de la boucle infinie grâce à l'instruction 'break'.
    except : 
        break

# Une fois que la boucle est terminée (par un 'break'), on affiche la valeur finale de la variable 'now' dans la sortie standard.
# La fonction print() convertit 'now' en chaîne de caractères si ce n'est déjà le cas, puis l'affiche suivie d'un retour à la ligne.
print(now)