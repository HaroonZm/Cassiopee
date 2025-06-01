def calcul_somme_entier_quotient_restant():
    """
    Lit deux entiers D et L depuis l'entrée standard séparés par un espace,
    puis calcule et affiche la somme de la division entière de D par L
    et du reste de cette division.

    Par exemple, si D=10 et L=3:
        - Division entière: 10 // 3 = 3
        - Reste: 10 % 3 = 1
        - Somme affichée: 3 + 1 = 4
    """
    # Lecture des deux entiers D et L depuis l'entrée standard
    D, L = map(int, input().split())

    # Calcul de la division entière de D par L
    division_entiere = D // L

    # Calcul du reste de la division de D par L
    reste = D % L

    # Somme de la division entière et du reste
    resultat = division_entiere + reste

    # Affichage du résultat
    print(resultat)