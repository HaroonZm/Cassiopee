def calcul_ratio():
    """
    Lit trois valeurs flottantes depuis l'entrée standard, séparées par des espaces: a, t et r.
    Calcule le résultat de (t * r) / a et l'affiche.

    Entrée attendue : trois nombres flottants séparés par des espaces.
    Sortie : un nombre flottant correspondant au calcul.
    """
    # Lecture d'une ligne de l'entrée standard et conversion des valeurs en float
    a, t, r = [float(i) for i in input("Entrez les valeurs a, t et r séparées par des espaces : ").split()]

    # Calcul du ratio selon la formule donnée
    resultat = t * r / a

    # Affichage du résultat
    print(resultat)

calcul_ratio()