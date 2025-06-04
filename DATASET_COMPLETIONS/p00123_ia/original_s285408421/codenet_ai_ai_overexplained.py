# Boucle infinie qui permet de traiter plusieurs paires de valeurs tant que l'utilisateur entre des données valides
while True:
    try:
        # On demande à l'utilisateur d'entrer deux nombres séparés par un espace, puis on essaie de les convertir en float
        # input() récupère une chaîne de caractères saisie par l'utilisateur
        # split() divise cette chaîne en une liste de sous-chaînes autour des espaces par défaut
        # map(float, ...) applique la fonction 'float' à chaque sous-chaîne obtenue, convertissant les deux valeurs en nombres décimaux
        t1, t2 = map(float, input().split())
    except:
        # Si une erreur survient (par exemple, fin de fichier ou mauvaise saisie),
        # on sort de la boucle infinie avec break pour arrêter le programme proprement
        break
    
    # On transforme les nombres décimaux en entiers pour faciliter les comparaisons
    # Chaque nombre est multiplié par 100 pour passer de valeurs avec deux décimales à des entiers (centièmes)
    # int() tronque la partie décimale résultante
    t1, t2 = int(t1*100), int(t2*100)
    
    # On utilise une série de conditions pour déterminer quelle catégorie renvoyer en fonction des valeurs de t1 et t2
    # Chaque condition vérifie si t1 et t2 sont inférieurs à certains seuils
    if t1 < 3550 and t2 < 7100:
        # Si t1 < 35.50 et t2 < 71.00, afficher "AAA"
        print("AAA")
    elif t1 < 3750 and t2 < 7700:
        # Sinon si t1 < 37.50 et t2 < 77.00, afficher "AA"
        print("AA")
    elif t1 < 4000 and t2 < 8300:
        # Sinon si t1 < 40.00 et t2 < 83.00, afficher "A"
        print("A")
    elif t1 < 4300 and t2 < 8900:
        # Sinon si t1 < 43.00 et t2 < 89.00, afficher "B"
        print("B")
    elif t1 < 5000 and t2 < 10500:
        # Sinon si t1 < 50.00 et t2 < 105.00, afficher "C"
        print("C")
    elif t1 < 5500 and t2 < 11600:
        # Sinon si t1 < 55.00 et t2 < 116.00, afficher "D"
        print("D")
    elif t1 < 7000 and t2 < 14800:
        # Sinon si t1 < 70.00 et t2 < 148.00, afficher "E"
        print("E")
    else:
        # Si aucune des conditions précédentes n'est remplie, afficher "NA" pour indiquer que la catégorie ne s'applique pas
        print("NA")