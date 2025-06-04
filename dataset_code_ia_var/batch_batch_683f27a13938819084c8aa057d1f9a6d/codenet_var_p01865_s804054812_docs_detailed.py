def main():
    """
    Fonction principale qui lit des entrées utilisateur, calcule une somme pondérée et affiche un résultat en fonction de la valeur de la somme.

    Entrée :
        - Une première ligne ignorée (input()).
        - Une deuxième ligne : un entier n, le nombre de paires à traiter.
        - Les n lignes suivantes : deux entiers x et w séparés par un espace, à chaque ligne.

    Affichage :
        - Si la somme pondérée est nulle, affiche '0'.
        - Sinon, affiche '1', suivie d'un entier indiquant le signe (+1 ou -1) puis la valeur absolue de la somme.
    """
    input()  # Première ligne ignorée, peut contenir toute information inutile.
    n = int(input())  # Nombre de paires à traiter.
    pairs = []
    for _ in range(n):
        # Lecture de chaque paire d'entiers x et w.
        x, w = map(int, input().split())
        pairs.append((x, w))
    # Calcul de la somme pondérée des x par leur coefficient w.
    s = sum(x * w for x, w in pairs)
    if s == 0:
        # Si la somme est nulle, on affiche simplement '0'.
        print('0')
    else:
        # Si la somme n'est pas nulle :
        #   On affiche '1' suivi de :
        #       Le signe : 1 si la somme est négative, -1 si positive (car [1, -1][s>0] donne 1 quand False, -1 quand True)
        #       La valeur absolue de la somme.
        sign = [1, -1][s > 0]
        print(f'1\n{sign} {abs(s)}')

if __name__ == "__main__":
    main()