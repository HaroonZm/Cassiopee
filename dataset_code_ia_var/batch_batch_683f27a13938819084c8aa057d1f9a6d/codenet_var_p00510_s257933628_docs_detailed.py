def main():
    """
    Lit des entrées utilisateur pour déterminer si une quantité peut rester positive 
    après une liste d'opérations, puis affiche la plus grande valeur atteinte ou 0 si impossible.
    
    Entrées:
        n (int): Nombre de lignes d'opérations à lire.
        m (int): Valeur initiale.
        Puis n lignes contenant chacune deux entiers séparés par un espace.
        
    Sortie:
        Imprime le maximum atteint de la valeur ou 0 si une opération la rend négative.
    """
    # Lecture du nombre de lignes d'opérations
    n = int(input("Entrez le nombre de lignes d'opérations (n) : "))
    # Lecture de la valeur initiale
    m = int(input("Entrez la valeur initiale (m) : "))

    sm = m  # sm va contenir la valeur maximale atteinte
    C = []  # Cette liste stockera chaque opération lue

    # Lecture et transformation des entrées pour chaque opération
    for i in range(n):
        # Lecture des deux valeurs sur une ligne, transformation en liste d'entiers et ajout dans C
        C.append(list(map(int, input(f"Entrez les deux entiers de l'opération {i+1} séparés par un espace : ").split())))

    # Parcours de chaque opération pour calculer la valeur courante et le maximum atteint
    for i in C:
        # Mise à jour de la valeur courante m selon l'opération (ajout puis retrait)
        m += i[0] - i[1]
        # Si la valeur devient négative, afficher 0 et arrêter le programme
        if m < 0:
            print(0)
            return
        # Mise à jour du maximum atteint
        sm = max(m, sm)
    # Affichage de la plus grande valeur atteinte après toutes les opérations
    print(sm)


if __name__ == "__main__":
    main()