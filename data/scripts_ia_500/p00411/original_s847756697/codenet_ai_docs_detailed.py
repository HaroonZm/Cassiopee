def calculate_scaled_value():
    """
    Lit trois entiers séparés par des espaces depuis l'entrée standard,
    où le premier entier représente une valeur de référence,
    le deuxième entier une autre valeur,
    et le troisième entier un facteur de mise à l'échelle.

    Calcule ensuite le produit du rapport du deuxième entier sur le premier entier multiplié par le troisième entier,
    puis affiche le résultat.

    Par exemple, si les entrées sont '2 6 4', la sortie sera (6/2)*4 = 3*4 = 12.0.
    """
    # Lire une ligne d'entrée, la scinder en une liste de chaînes en fonction des espaces,
    # convertir chaque élément en entier, et stocker la liste résultante dans 'inputs'
    inputs = list(map(int, input().split()))

    # Calculer le rapport de inputs[1] sur inputs[0], puis multiplier ce résultat par inputs[2]
    result = (inputs[1] / inputs[0]) * inputs[2]

    # Afficher le résultat calculé
    print(result)

# Appel de la fonction principale
calculate_scaled_value()