def calculate_value(p, q, a, b, c, d):
    """
    Calcule une valeur basée sur les paramètres fournis.

    Le calcul est effectué selon la formule :
    p*a + (p/10)*c + q*b + (q/20)*d

    Args:
        p (int): Première variable d'entrée.
        q (int): Deuxième variable d'entrée.
        a (int): Coefficient multiplié par p.
        b (int): Coefficient multiplié par q.
        c (int): Coefficient multiplié par p/10.
        d (int): Coefficient multiplié par q/20.

    Returns:
        float: Résultat du calcul.
    """
    return p * a + (p / 10) * c + q * b + (q / 20) * d

def main():
    """
    Fonction principale qui lit les entrées, effectue les calculs et affiche le résultat.

    Lit deux paires d'entiers depuis l'entrée standard, puis quatre entiers supplémentaires.
    Calcule deux valeurs en utilisant la fonction calculate_value.
    Compare ces deux valeurs pour déterminer quelle chaîne doit être affichée :
    - "hiroshi" si la première valeur est strictement inférieure à la deuxième,
    - "even" si elles sont égales,
    - "kenjiro" si la première est strictement supérieure à la deuxième.
    """
    # Lecture des deux premières valeurs entières h1 et h2
    h1, h2 = map(int, raw_input().split())

    # Lecture des deux secondes valeurs entières k1 et k2
    k1, k2 = map(int, raw_input().split())

    # Lecture des coefficients a, b, c, d
    a, b, c, d = map(int, raw_input().split())

    # Calcul des valeurs pour les deux paires
    v1 = calculate_value(h1, h2, a, b, c, d)
    v2 = calculate_value(k1, k2, a, b, c, d)

    # Déterminer le résultat en fonction de la comparaison des valeurs v1 et v2
    # Index 0: "hiroshi" si v1 < v2
    # Index 1: "even" si v1 == v2
    # Index 2: "kenjiro" si v1 > v2
    result = ["hiroshi", "even", "kenjiro"][(v1 < v2) + (v1 == v2)]

    # Affichage du résultat
    print(result)

if __name__ == "__main__":
    main()