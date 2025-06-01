def calcul_aire_surface():
    """
    Exécute une boucle infinie qui lit des valeurs en entrée,
    calcule une expression mathématique basée sur ces valeurs,
    puis affiche le résultat. La boucle se termine lorsque la valeur
    de 'x' est égale à 0.

    L'expression calculée est : x² + 2 * x * √((x/2)² + h²),
    ce qui peut correspondre à une opération géométrique
    (comme le calcul d'une surface ou d'un périmètre modifié).

    Entrées utilisateur :
    - x : nombre flottant
    - h : nombre flottant

    Sortie :
    - l'impression du résultat du calcul pour chaque couple (x, h)
      jusqu'à ce que x soit 0.
    """
    while True:
        # Lecture de la variable x convertie en float
        x = float(input())
        
        # Lecture de la variable h convertie en float
        h = float(input())
        
        # Condition d'arrêt de la boucle : si x vaut 0, on quitte
        if x == 0:
            break
        
        # Calcul de l'expression :
        # x² + 2 * x * racine carrée de ((x/2)² + h²)
        resultat = x * x + 2 * x * (((x / 2) ** 2) + h * h) ** 0.5
        
        # Affichage du résultat calculé
        print(resultat)