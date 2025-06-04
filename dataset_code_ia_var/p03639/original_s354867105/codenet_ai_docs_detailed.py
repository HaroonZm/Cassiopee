from collections import Counter

def can_form_special_sequence(n, numbers):
    """
    Détermine si une séquence d'entiers peut être arrangée selon une condition spécifique liée au reste de 4.

    La condition est telle que pour la séquence, le nombre d'éléments dont le reste est 1, 2 ou 3 modulo 4
    ne dépasse pas le nombre d'éléments dont le reste est 0 modulo 4 plus un.

    Paramètres:
    ----------
    n : int
        Le nombre d'éléments dans la séquence.
    numbers : list of int
        La liste des entiers à analyser.

    Retourne:
    -------
    str
        'Yes' si la condition est satisfaite, sinon 'No'.
    """
    # Calculer le nombre d'éléments pour chaque reste de la division par 4
    c = Counter(num % 4 for num in numbers)
    # Vérifie si au plus un élément de reste 2 et si la sommation totale satisfait la condition
    count_one = c[1]
    count_two = 1 if c[2] > 0 else 0  # Uniquement 1 s'il y a au moins un reste 2
    count_three = c[3]
    # La condition requise énumérée ci-dessus
    if (count_one + count_two + count_three) <= (c[0] + 1):
        return 'Yes'
    else:
        return 'No'

def main():
    """
    Lit les entrées utilisateur, exécute la vérification et affiche le résultat.
    """
    # Lecture du nombre d'éléments de la séquence
    N = int(input())
    # Lecture de la séquence entière et conversion en liste d'entiers
    numbers = list(map(int, input().split()))
    # Vérifie et affiche le résultat selon la condition
    print(can_form_special_sequence(N, numbers))

if __name__ == "__main__":
    main()