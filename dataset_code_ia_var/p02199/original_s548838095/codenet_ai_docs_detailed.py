def compute_result(a: int, b: int, p: int, q: int, r: int) -> float:
    """
    Calcule le résultat de l'expression suivante :
        b + (p * b - (b - a) * q) / (q + r)

    Paramètres:
        a (int): Le premier entier de la première ligne d'entrée.
        b (int): Le deuxième entier de la première ligne d'entrée.
        p (int): Le premier entier de la deuxième ligne d'entrée.
        q (int): Le deuxième entier de la deuxième ligne d'entrée.
        r (int): Le troisième entier de la deuxième ligne d'entrée.

    Retourne:
        float: Le résultat du calcul.
    """
    # Calcul de la différence entre b et a, puis multiplication par q
    diff_times_q = (b - a) * q

    # Multiplication de p par b
    p_times_b = p * b

    # Soustraction des deux résultats précédents
    numerator = p_times_b - diff_times_q

    # Calcul du dénominateur (q + r)
    denominator = q + r

    # Division pour obtenir la fraction
    fraction = numerator / denominator

    # Ajout de la valeur de b au résultat de la fraction
    result = b + fraction

    return result

def main():
    """
    Lit les entrées de l'utilisateur, exécute le calcul et affiche le résultat.
    """
    # Lecture de la première ligne d'entrée et conversion en entiers
    a, b = map(int, input().split())

    # Lecture de la seconde ligne d'entrée et conversion en entiers
    p, q, r = map(int, input().split())

    # Calcul du résultat via la fonction compute_result
    res = compute_result(a, b, p, q, r)

    # Affichage du résultat
    print(res)

# Point d'entrée du script
if __name__ == '__main__':
    main()