def main():
    """
    Point d'entrée principal du programme. 
    Boucle indéfiniment pour traiter plusieurs jeux de données fournis par l'utilisateur.
    Pour chaque jeu de données :
        - lit un entier 'a' représentant le nombre d'éléments à traiter,
        - si 'a' vaut 0, sort de la boucle et termine le programme,
        - lit une liste de 'a' entiers,
        - calcule et affiche le nombre d'éléments inférieurs ou égaux à la moyenne.
    """
    while True:
        # Lecture du nombre d'éléments à traiter ; arrête le programme si 'a' est 0
        a = int(input())
        if a == 0:
            break

        # Lecture de la liste d'entiers, de taille 'a', séparés par des espaces
        b = list(map(int, input().split()))

        # Calcul de la moyenne arithmétique de la liste 'b'
        mean = sum(b) / a

        # Compte le nombre d'éléments inférieurs ou égaux à la moyenne
        count = 0
        for i in range(a):
            if mean >= b[i]:
                count += 1

        # Affiche le nombre d'éléments trouvés
        print(count)

if __name__ == '__main__':
    main()