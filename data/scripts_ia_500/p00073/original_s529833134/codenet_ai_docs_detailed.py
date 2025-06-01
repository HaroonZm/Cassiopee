def calculate_surface_area():
    """
    Boucle infinie qui lit des paires de valeurs (x, h) depuis l'entrée standard.
    Pour chaque paire, calcule et affiche une surface selon une formule donnée.
    La boucle s'arrête lorsque les deux entrées sont '0'.
    
    La formule utilisée est :
    a = x / 2
    s = x^2 + 2 * x * sqrt(a^2 + h^2)
    
    Les entrées x et h doivent être des valeurs numériques.
    """
    while True:
        # Lire les entrées sous forme de chaînes de caractères
        x = input()  # Lire la première valeur x
        h = input()  # Lire la deuxième valeur h
        
        # Convertir les entrées en float pour les calculs
        # Il est nécessaire de convertir en float pour la division et la racine carrée
        try:
            x_val = float(x)
            h_val = float(h)
        except ValueError:
            # Si la conversion échoue, informer et continuer la boucle
            print("Entrées invalides. Veuillez entrer des nombres.")
            continue
        
        # Condition d'arrêt : si les deux valeurs sont 0, on quitte la boucle
        if x_val == 0 and h_val == 0:
            break
        
        # Calcul de a comme la moitié de x
        a = x_val / 2
        
        # Calcul de la surface s selon la formule donnée
        s = x_val**2 + 2 * x_val * (a**2 + h_val**2)**0.5
        
        # Affichage du résultat
        print(s)

# Appel de la fonction pour exécuter le programme
calculate_surface_area()