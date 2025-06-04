def int_to_balanced_ternary(n):
    """
    Convertit un entier en sa représentation ternaire équilibrée sous forme de chaîne de caractères.

    Dans le ternaire équilibré :
      - '0' représente 0,
      - '+' représente +1,
      - '-' représente -1.

    Args:
        n (int): L'entier à convertir.

    Returns:
        str: La représentation en ternaire équilibré.
    """
    # Liste pour accumuler les chiffres du ternaire équilibré (de droite à gauche)
    l = []
    # Boucle jusqu'à ce que le nombre soit réduit à 0
    while n:
        if n % 3 == 0:
            # Si le reste est 0, placer '0' et diviser n par 3
            l = ["0"] + l
            n //= 3
        elif n % 3 == 1:
            # Si le reste est 1, placer '+', puis retirer 1 et diviser n par 3
            l = ["+"] + l
            n = (n - 1) // 3
        else:
            # Si le reste est 2, cela correspond à -1; placer '-', puis ajuster n
            # (n+1)//3 compense pour le -1 représenté par '-'
            l = ["-"] + l
            n = (n + 1) // 3
    # Retourner la représentation sous forme de chaîne
    return "".join(l)

# Demander à l'utilisateur un entier à convertir
n = int(input("Entrez un entier à convertir en ternaire équilibré : "))
# Appeler la fonction et afficher le résultat
print(int_to_balanced_ternary(n))