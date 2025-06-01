def calculer_somme_entier_quotient_reste():
    """
    Lit deux entiers D et L depuis l'entrée standard, où D est un nombre entier
    et L est un diviseur. Calcule ensuite le quotient entier et le reste de la
    division de D par L, puis calcule et affiche la somme de ces deux valeurs.

    Le programme réalise les étapes suivantes :
    1. Lit une ligne d'entrée contenant deux entiers séparés par un espace.
    2. Sépare et convertit ces valeurs en entiers D et L.
    3. Calcule le quotient entier de la division D // L.
    4. Calcule le reste de la division D % L.
    5. Calcule la somme du quotient et du reste.
    6. Affiche cette somme.
    """

    # Lecture de la ligne d'entrée et conversion des deux nombres en entiers
    D, L = map(int, input().split())

    # Calcul du quotient entier de D divisé par L
    quotient = D // L

    # Calcul du reste de la division de D par L
    reste = D % L

    # Calcul de la somme du quotient et du reste
    somme = quotient + reste

    # Affichage du résultat
    print(somme)

# Appel de la fonction principale
calculer_somme_entier_quotient_reste()