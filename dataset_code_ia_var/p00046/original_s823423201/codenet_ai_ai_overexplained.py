# Création d'une liste vide pour stocker les différentes hauteurs saisies par l'utilisateur.
heightlist = []

# Démarrage d'une boucle infinie grâce à 'while 1:'.
# Celle-ci va permettre à l'utilisateur de saisir autant de valeurs qu'il le souhaite.
while 1:
    try:
        # Utilisation de la fonction input() pour obtenir une saisie clavier de l'utilisateur.
        # Comme input() retourne toujours une chaîne de caractères (string), 
        # il est nécessaire de la convertir en nombre à virgule flottante avec float().
        height = float(input())
        # Ajout de la valeur convertie à la liste des hauteurs 'heightlist' à l'aide de la méthode .append().
        heightlist.append(height)
    except:
        # Si une exception est levée (ex : saisie d'un texte non convertible en float, ou l'utilisateur fait Ctrl+D / Ctrl+Z),
        # le programme exécute ce bloc, ce qui permet de sortir de la boucle 'while'.
        break

# Calcul de la différence entre la plus grande et la plus petite valeur de la liste 'heightlist'.
# La fonction max() renvoie la valeur maximale trouvée dans la liste.
# La fonction min() renvoie la valeur minimale trouvée dans la liste.
# On les soustrait pour obtenir l'écart (différence) entre la plus grande et la plus petite valeur.
diff = max(heightlist) - min(heightlist)

# Affichage du résultat grâce à la fonction print().
# Cette fonction affiche dans le terminal la différence calculée précédemment.
print(diff)