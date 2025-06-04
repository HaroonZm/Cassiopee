def main():
    """
    Demande à l'utilisateur une chaîne à rechercher, puis un nombre n,
    puis lit n chaînes et compte pour chacune si la chaîne recherchée
    apparaît comme sous-chaîne dans la concaténation de la chaîne saisie avec elle-même.
    Affiche le total trouvé.
    """
    # Lecture de la chaîne recherchée
    t = input()

    # Lecture du nombre n d'essais
    n = int(input())

    # Initialisation du compteur
    count = 0

    # Boucle sur les n chaînes à lire
    for _ in range(n):
        # Lecture de la chaîne courante
        s = input()
        # La chaîne recherchée est-elle sous-chaîne de s+s ?
        if t in 2 * s:
            count += 1
    
    # Affichage du nombre de chaînes répondant au critère
    print(count)

if __name__ == "__main__":
    main()