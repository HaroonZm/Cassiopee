def calculate_ratio_scaled_time(a, t, r):
    """
    Calcule le produit du temps 't' et du quotient 'r / a'.

    Cette fonction effectue le calcul suivant : (r / a) * t,
    où :
        - a (int): Diviseur utilisé pour mettre à l'échelle la valeur r.
        - t (int): Paramètre temps ou multiplicateur.
        - r (int): Numérateur que l'on souhaite mettre à l'échelle.

    Returns:
        float: Le résultat du calcul (r / a) * t.
    """
    return (r / a) * t

def main():
    """
    Fonction principale du script.
    Lit trois entiers de l'entrée standard, effectue le calcul,
    et affiche le résultat.
    """
    # Lis une ligne de l'entrée utilisateur, sépare les valeurs et les convertit en entiers
    a, t, r = map(int, input().split())

    # Appelle la fonction de calcul avec les valeurs lues
    result = calculate_ratio_scaled_time(a, t, r)

    # Affiche le résultat final
    print(result)

if __name__ == "__main__":
    main()