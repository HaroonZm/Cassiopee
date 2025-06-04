def calculate_final_amount():
    """
    Calcule le montant final après une série d'augmentations composées et l'affiche.

    Cette fonction initialise un montant de départ à 100 (10 ** 2). 
    Elle lit un entier `t` depuis l'entrée standard, représentant le nombre d'années ou de périodes.
    À chaque itération, elle augmente le montant de 5% (multiplication par 1.05), puis arrondit au supérieur si nécessaire.
    Enfin, elle affiche le résultat multiplié par 1000.

    Entrée utilisateur :
        - Un entier `t` : nombre d'itérations (ex. nombre d'années).

    Sortie :
        - Un entier représentant le montant final ajusté, multiplié par 1000.
    """
    # Initialisation du montant de départ à 100
    n = 10 ** 2

    # Lecture du nombre de périodes à traiter depuis l'entrée utilisateur
    t = int(input())

    # Boucle pour appliquer la croissance composée sur `t` périodes
    for i in range(t):
        # Augmentation de `n` de 5%
        n = float(n) * 1.05
        
        # Si la partie décimale existe, on arrondit à l'entier supérieur
        if n - int(n) > 0:
            n = int(n) + 1
        else:
            n = int(n)
    
    # Calcul du montant final à afficher (après conversion en unités minimales)
    result = n * (10 ** 3)
    
    # Affichage du résultat final
    print(result)

# Appel de la fonction principale
calculate_final_amount()