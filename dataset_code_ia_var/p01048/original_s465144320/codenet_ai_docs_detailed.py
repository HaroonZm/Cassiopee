#!/usr/bin/env python3

def first_with_n_divisors(n):
    """
    Trouve le plus petit entier positif qui possède exactement n diviseurs.

    Args:
        n (int): Le nombre de diviseurs recherchés.

    Returns:
        int: Le plus petit entier ayant exactement n diviseurs.
    """
    # on stocke, pour chaque nombre de diviseurs <= 12, le premier entier rencontré possédant ce nombre de diviseurs
    num = [0] * 13  # Indices 0 à 12 [num[k] = plus petit entier ayant exactement k diviseurs]
    i = 1  # Entier courant à tester

    while True:
        # Compte le nombre de diviseurs de i
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1

        # On ignore les cas où le nombre de diviseurs dépasse 12
        if cnt > 12:
            i += 1
            continue

        # Si c'est la première fois qu'on rencontre cnt diviseurs, on l'enregistre
        if num[cnt] == 0:
            num[cnt] = i

        # Si on a trouvé un entier ayant exactement n diviseurs, on retourne ce nombre
        if num[n] > 0:
            return num[n]

        i += 1

def main():
    """
    Fonction principale du programme.
    Lit un entier n de l'entrée, calcule et affiche le plus petit entier avec exactement n diviseurs.
    """
    n = int(input())  # Lecture du nombre de diviseurs souhaité
    ans = first_with_n_divisors(n)  # Recherche du plus petit entier ayant n diviseurs
    print(ans)  # Affichage du résultat

if __name__ == "__main__":
    main()