def calculate_expression():
    """
    Lit deux lignes d'entrée utilisateur, chacune contenant une ou plusieurs valeurs entières séparées par des espaces.
    La première ligne fournit les valeurs de 'a' et 'b'.
    La seconde ligne fournit les valeurs de 'p', 'q' et 'r'.
    Calcule ensuite la valeur de l'expression : (p * b + q * a + r * b) / (q + r)
    et affiche le résultat.

    Entrées :
        a, b : int - Les deux premiers entiers lus.
        p, q, r : int - Les trois entiers suivants.

    Sortie :
        float - Le résultat du calcul affiché sur la sortie standard.
    """
    # Lecture de la première ligne : deux entiers séparés par des espaces
    a, b = map(int, input().split())
    # Lecture de la seconde ligne : trois entiers séparés par des espaces
    p, q, r = map(int, input().split())
    # Calcul du numérateur de l'expression
    numerator = (p * b) + (q * a) + (r * b)
    # Calcul du dénominateur de l'expression
    denominator = q + r
    # Calcul final de l'expression
    result = numerator / denominator
    # Affiche le résultat
    print(result)

# Appel de la fonction principale
calculate_expression()