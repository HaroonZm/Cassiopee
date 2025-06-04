def calculate_ratio(a, t, r):
    """
    Calcule le ratio (r * t) / a avec une précision maximale.

    Args:
        a (int): Le diviseur principal.
        t (int): Le multiplicateur du ratio.
        r (int): Le multiplicateur du ratio.

    Returns:
        float: Le résultat du calcul (r * t) / a.
    """
    # Effectue le calcul en multipliant r et t, puis en divisant le résultat par a
    return (r * t) / a

def main():
    """
    Fonction principale du programme.
    Lit trois entiers à partir de l'entrée standard, effectue le calcul,
    puis affiche le résultat avec une précision de 6 décimales.
    """
    # Lit une ligne d'entrée, découpe la chaîne de caractères en une liste et convertit en entiers
    a, t, r = list(map(int, input().split()))
    # Calcule le résultat en appelant la fonction calculate_ratio
    ans = calculate_ratio(a, t, r)
    # Affiche le résultat formaté à 6 décimales après la virgule
    print("{:.6f}".format(ans))

if __name__ == "__main__":
    main()