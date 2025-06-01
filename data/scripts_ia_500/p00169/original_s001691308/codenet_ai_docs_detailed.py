def process_hands():
    """
    Lit des mains de cartes depuis l'entrée standard, calcule la somme de leurs valeurs selon les règles du blackjack,
    puis affiche le résultat approprié pour chaque main.
    
    La lecture continue jusqu'à ce qu'une main commençant par 0 soit rencontrée.
    Règles de calcul des valeurs :
        - Cartes de 2 à 9 valent leur valeur numérique.
        - Cartes de 10 et plus valent 10.
        - Les As (valeur 1) comptent initialement comme 1, mais peuvent être comptés comme 11 si cela ne fait pas dépasser 21.
    """
    while True:
        # Lire une ligne d'entrée, la découper en entiers représentant les cartes de la main
        h = map(int, raw_input().split())
        
        # Si la première carte est 0, fin de la saisie et sortie de la boucle
        if h[0] == 0:
            break
        
        total = 0  # Somme temporaire des cartes autres que les As
        ace_count = 0  # Nombre de cartes As (valeur 1) dans la main
        
        # Trier les cartes de la main par ordre décroissant (utile pour traitement spécifique, ici pour lecture)
        for card in sorted(h, reverse=True):
            if 2 <= card <= 9:
                # Cartes entre 2 et 9 sont ajoutées avec leur valeur numérique
                total += card
            elif card >= 10:
                # Cartes de valeur 10 ou plus comptent pour 10 points
                total += 10
            elif card == 1:
                # Compter le nombre d'As pour traitement différé
                ace_count += 1
        
        # Ajouter initialement 1 point pour chaque As
        total += ace_count
        
        if total > 21:
            # Si la somme dépasse 21, la main est perdante (0 affiché)
            print 0
        else:
            # Tenter d'augmenter la valeur des As de 1 à 11 sans dépasser 21
            for _ in range(ace_count):
                if total + 10 > 21:
                    # Si ajouter 10 (pour transformer un As de 1 à 11) dépasse 21, afficher la somme actuelle
                    print total
                    break
                else:
                    # Sinon, augmenter la somme de 10 (un As vaut donc 11)
                    total += 10
            else:
                # Si la boucle n'a pas été interrompue, afficher la somme finale
                print total