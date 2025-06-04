def eratosthenes(n):
    """
    Génère les premiers nombres premiers strictement supérieurs à n.
    Utilise le crible d'Ératosthène pour générer des nombres premiers.

    Args:
        n (int): Nombre à partir duquel chercher les nombres premiers (non inclus).

    Returns:
        list: Liste des premiers nombres premiers strictement supérieurs à n (maximum 51 résultats).
    """
    length = 150000  # Limite supérieure pour le crible (nombre maximal testé comme candidat premier)
    ret = []  # Liste pour stocker les nombres premiers trouvés
    flag = [True] * length  # Tableau de booléens, True si l'indice est premier, False sinon

    # Parcours de tous les entiers à partir de 2 jusqu'à 'length'
    for i in range(2, length):
        if flag[i]:
            if n < i:
                ret.append(i)  # i est un nombre premier strictement supérieur à n
            # Met à jour le tableau flag pour éliminer les multiples de i (i.e., non premiers)
            for j in range(i, length, i):
                flag[j] = False
        # On arrête la recherche dès que la liste de résultats dépasse 50 éléments
        if len(ret) > 50:
            break
    return ret

def main():
    """
    Point d'entrée du programme.
    Lit en boucle des paires (N, P) depuis l'entrée standard.
    Pour chaque paire, calcule la liste des premiers > N, forme toutes les sommes possibles
    de deux nombres premiers (avec répétition), trie ces sommes et affiche la P-ème plus petite somme.

    Arrête la lecture et la boucle si la paire (-1, -1) est fournie.
    """
    while True:
        N, P = map(int, input().split())  # Lecture des valeurs N et P
        # Condition d'arrêt : si les deux valeurs sont -1
        if N == -1 and P == -1:
            break
        # Génération de la liste des 51 (maximum) premiers nombres premiers strictement supérieurs à N
        ret = eratosthenes(N)
        sosu_add = []  # Liste pour stocker les sommes de deux nombres premiers

        # Génère toutes les sommes possibles (avec répétition) entre deux nombres premiers de la liste
        for i in range(len(ret)):
            for j in range(i, len(ret)):
                sosu_add.append(ret[i] + ret[j])

        sosu_add.sort()  # Trie les sommes par ordre croissant
        print(sosu_add[P - 1])  # Affiche la P-ème somme (1-indexée)

if __name__ == "__main__":
    main()