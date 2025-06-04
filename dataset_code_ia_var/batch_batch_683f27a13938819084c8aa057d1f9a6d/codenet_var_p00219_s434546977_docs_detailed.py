def main():
    """
    Fonction principale qui lance une boucle interactive pour lire des listes de chiffres et afficher leur fréquence
    sous forme d'histogramme (barres d'étoiles).

    Fonctionnement :
    - Demande à l'utilisateur de saisir un nombre n.
    - Si n est 0, la boucle se termine.
    - Sinon, lit n entiers entre 0 et 9, compte la fréquence de chaque chiffre.
    - Pour chaque chiffre de 0 à 9, affiche un nombre d'étoiles correspondant à la fréquence,
      ou un trait d'union si la fréquence est nulle.
    """
    while True:
        # Lecture du nombre d'entrées à traiter
        n = int(input("Entrez le nombre d'éléments (0 pour quitter) : "))
        if n == 0:
            # Sortie de la boucle si l'utilisateur entre 0
            break

        # Initialisation d'une liste de taille 10 pour compter les occurrences des chiffres 0 à 9
        num_list = [0 for _ in range(10)]

        # Lecture des chiffres et mise à jour du nombre d'occurrences dans num_list
        for _ in range(n):
            c = int(input("Entrez une valeur (entre 0 et 9) : "))
            num_list[c] += 1

        # Affichage de l'histogramme : une ligne par chiffre de 0 à 9
        for i in range(10):
            cnt = '*' * num_list[i]
            if len(cnt) == 0:
                # Si aucun chiffre n'est présent, on affiche un tiret "-"
                print('-')
            else:
                # Sinon, on affiche autant d'étoiles que de chiffres comptés
                print(cnt)

if __name__ == "__main__":
    main()