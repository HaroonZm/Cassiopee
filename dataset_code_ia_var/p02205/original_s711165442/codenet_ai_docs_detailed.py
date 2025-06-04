def compute_sequence_value(n):
    """
    Calcule puis renvoie la valeur au nième indice modulo 12 dans une séquence générée avec des opérations alternées.

    La séquence commence par deux entiers a et b, puis évolue pendant 12 étapes selon :
      - étape paire (i%2 == 0) : nouveau terme = [a-b, b]
      - étape impaire (i%2 == 1) : nouveau terme = [a, a+b]

    Args:
        n (int): L'entier pour lequel on souhaite le nième élément de la séquence (en modulo 12).

    Returns:
        tuple: Un tuple (a, b) représentant le terme voulu après transformation.
    """
    # Lecture de la valeur d'entrée n (entier)
    # n dirige le nombre d'itérations en modulo 12
    # n = int(input()) est déplacé dans la fonction principale pour favoriser la modularité

    # Lecture des deux entiers de départ qui forment le premier élément de la séquence
    a, b = map(int, input().split())

    # Initialisation de la liste avec le premier couple (a, b)
    ab = [[a, b]]

    # Génération de la suite sur 12 termes supplémentaires
    for i in range(11):
        # Récupérer la dernière paire (a, b)
        a, b = ab[-1]

        # Si l'indice est pair, appliquer a-b sur le premier élément, laisser le deuxième inchangé
        if i % 2 == 0:
            ab.append([a - b, b])
        # Si l'indice est impair, laisser le premier élément inchangé, appliquer a+b sur le second
        else:
            ab.append([a, a + b])

    # Retourne le couple au rang n modulo 12
    return tuple(ab[n % 12])


def main():
    """
    Fonction principale pour saisir les entrées et afficher la sortie de la séquence demandée.
    """
    # Demander à l'utilisateur de saisir l'indice souhaité
    n = int(input())

    # Récupérer et afficher le terme calculé selon la méthode décrite
    result = compute_sequence_value(n)
    print(*result)


if __name__ == "__main__":
    main()