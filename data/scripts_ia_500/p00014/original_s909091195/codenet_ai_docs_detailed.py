def calculate_size():
    """
    Demande à l'utilisateur de saisir un entier d, puis calcule et affiche une valeur 'size'
    basée sur une somme pondérée de carrés des multiples de d.

    Cette fonction s'exécute pour un maximum de 20 itérations ou jusqu'à ce qu'une entrée invalide soit détectée,
    auquel cas elle interrompt la boucle.

    La formule utilisée est :
        size = Σ_{i=1}^{(600//d - 1)} ((i * d)^2) * d
    
    La fonction gère les erreurs d'entrée pour arrêter proprement l'exécution.
    """
    for j in range(20):
        try:
            # Lecture de l'entrée utilisateur convertie en entier
            d = int(input())
            size = 0
            
            # La limite supérieure (non incluse) du compteur i est 600//d - 1
            # On itère de 0 à (600//d - 2), puis on ajoute 1 à i pour commencer à 1
            for i in range(600 // d - 1):
                i += 1  # Décaler l'indice pour commencer à 1 au lieu de 0
                
                # Calcul de l'élément courant : ((i*d)^2) multiplié par d
                size += ((i * d) ** 2) * d
                
            # Affichage de la taille calculée convertie en entier
            print(int(size))
            
        except:
            # En cas d'erreur d'entrée ou autre exception, on interrompt la boucle
            break

# Appel de la fonction principale
calculate_size()