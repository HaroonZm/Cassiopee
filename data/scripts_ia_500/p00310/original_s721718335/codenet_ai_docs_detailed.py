def main():
    """
    Programme principal qui lit trois entiers séparés par des espaces depuis l'entrée standard,
    calcule leur somme, puis affiche le résultat.
    """
    # Lire une ligne d'entrée, la scinder en trois parties, et convertir chacune en entier
    p, m, c = map(int, input().split())

    # Calculer la somme des trois entiers
    total = sum((p, m, c))

    # Afficher la somme calculée
    print(total)

if __name__ == "__main__":
    main()