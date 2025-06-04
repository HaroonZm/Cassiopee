def main():
    """
    Programme principal qui lit deux entrées, interprète une expression mathématique
    potentiellement contenant l'opérateur '^', la calcule et multiplie le résultat par T.
    Si le résultat dépasse 10^9, affiche 'TLE', sinon affiche le résultat.
    """
    # Lecture et analyse des entrées de l'utilisateur :
    n, T = map(int, raw_input().split())
    # Lecture de l'expression mathématique sous forme de chaîne
    expr = raw_input()

    # Calcul du résultat
    result = eval_expression(expr, T)

    # Affichage en fonction de la contrainte spécifiée
    if result <= 10**9:
        print(result)
    else:
        print("TLE")

def eval_expression(expr, multiplier):
    """
    Prend une expression mathématique en chaîne de caractères, remplace l'opérateur '^'
    par l'opérateur d'exponentiation Python '**' et évalue l'expression.
    Multiplie ensuite le résultat obtenu par le multiplicateur spécifié.

    Args:
        expr (str): L'expression mathématique à évaluer (par exemple '2^3+5').
        multiplier (int): Valeur entière à multiplier au résultat de l'expression.

    Returns:
        int ou float: Résultat de l'évaluation multiplié, selon ce que retourne eval().
    """
    # Remplacer '^' par '**' pour correspondre à la syntaxe Python
    python_expr = expr.replace('^', '**')
    # Utiliser eval pour évaluer l'expression (en supposant qu'elle soit sûre)
    value = eval(python_expr)
    # Multiplier le résultat par la valeur passée en paramètre
    return value * multiplier

# Exécute le programme principal si ce fichier est exécuté
if __name__ == "__main__":
    main()