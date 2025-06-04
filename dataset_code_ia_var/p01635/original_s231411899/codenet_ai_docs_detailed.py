def compute_time(n, t, S):
    """
    Calcule le temps total nécessaire à partir de l'expression S et du paramètre t.

    Args:
        n (int): Le nombre d'opérations ou un paramètre inutilisé dans le calcul direct.
        t (int): Le facteur multiplicatif appliqué à l'expression S.
        S (str): Une expression mathématique, possiblement utilisant '^' pour l'exponentiation.

    Returns:
        int: Le temps total calculé.
    """
    # Remplacement de l'opérateur '^' (puissance) par '**' compatible avec Python
    S = S.replace("^", "**")
    # Construction de l'expression finale à évaluer, sous forme "(S)*t", pour multiplier le résultat de S par t
    expression = "({})*t".format(S)
    # Évaluation de l'expression dans l'environnement local contenant t
    time = eval(expression, {"__builtins__": {}}, {"t": t})
    return time

def main():
    """
    Fonction principale du programme.
    Lit les entrées, calcule le temps total, et affiche soit le temps soit 'TLE' en cas de dépassement.
    """
    # Lecture et décomposition des deux premiers entiers n et t
    n, t = map(int, input().split())
    # Lecture de l'expression S sous forme de chaîne de caractères
    S = input()
    # Calcul du temps total à partir de la fonction compute_time
    time = compute_time(n, t, S)
    # Vérification du seuil afin d'afficher le message approprié
    if time > 10**9:
        print("TLE")
    else:
        print(time)

# Point d'entrée du script
if __name__ == "__main__":
    main()