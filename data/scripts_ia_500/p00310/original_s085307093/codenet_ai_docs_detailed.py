def main():
    """
    Lit trois nombres entiers depuis l'entrée standard, calcule leur somme,
    puis affiche le résultat.
    """
    # Lire une ligne d'entrée, la diviser en trois parties, et convertir chacune en entier
    p, c, m = map(int, input().split())
    
    # Calculer la somme des trois entiers
    total = p + c + m
    
    # Afficher la somme convertie en entier (utile si la somme était un float)
    print(int(total))


if __name__ == "__main__":
    main()