def compute_final_value():
    """
    Lit deux entrées de l'utilisateur :
    - Deux entiers a et b (première ligne d'entrée)
    - Trois entiers p, q et r (seconde ligne d'entrée)
    Effectue un calcul basé sur ces valeurs et affiche le résultat.

    Le calcul est le suivant :
    1. Calcule e = p * b
    2. Calcule s = (b - a) * q
    3. Calcule le résultat final : b + (e - s) / (q + r)
    4. Affiche ce résultat.
    """
    # Lire deux entiers de la première ligne d'entrée
    a, b = map(int, input().split())

    # Lire trois entiers de la seconde ligne d'entrée
    p, q, r = map(int, input().split())

    # Calculer 'e' comme p multiplié par b
    e = p * b

    # Calculer 's' comme (b - a) multiplié par q
    s = (b - a) * q

    # Calculer le résultat final en suivant la formule donnée
    result = b + (e - s) / (q + r)

    # Afficher le résultat
    print(result)

# Appeler la fonction pour exécuter le programme
compute_final_value()