def compute_expression(a: float, t: float, r: float) -> float:
    """
    Calcule l'expression t * r / a.

    Paramètres:
    -----------
    a : float
        La valeur du dénominateur dans l'expression.
    t : float
        Premier facteur du numérateur dans l'expression.
    r : float
        Deuxième facteur du numérateur dans l'expression.

    Retourne:
    ---------
    float
        Le résultat du calcul t * r / a.
    """
    return t * r / a

# Demande à l'utilisateur d'entrer trois nombres séparés par des espaces.
# Utilisation de la compréhension de liste pour convertir chaque valeur en float.
# Les trois valeurs sont affectées aux variables a, t et r respectivement.
a, t, r = [float(i) for i in input("Entrez trois nombres (a t r) séparés par des espaces : ").split()]

# Calcule le résultat en appelant la fonction compute_expression avec les valeurs saisies.
result = compute_expression(a, t, r)

# Affiche le résultat du calcul à l'utilisateur.
print(result)