from bisect import bisect

def main():
    """
    Programme principal qui lit des entrées successives, traite chaque cas, et affiche le résultat.

    Pour chaque cas de test, le programme lit deux entiers n et lmt,
    suivis d'une liste de n entiers. Le programme cherche ensuite à déterminer
    la somme maximale d'une paire de sommes d'éléments issus de la liste,
    ne dépassant pas la limite lmt.

    La boucle se termine lorsque n vaut 0.
    """
    while True:
        # Lecture des deux entiers n (nombre d'éléments) et lmt (limite de somme)
        n, lmt = map(int, raw_input().split())

        # Condition d'arrêt : si n vaut 0, on quitte la boucle
        if n == 0:
            break

        # Lecture des n entiers suivants et ajout d'un élément 0 pour les combinaisons
        p = [input() for _ in range(n)] + [0]

        # Calcul de toutes les sommes possibles de p[i] + p[j], en évitant les doublons
        p = sorted(set(i + j for i in p for j in p))

        # Trouve l'indice d'insertion de lmt dans la liste triée p (limite supérieure)
        s = bisect(p, lmt)

        # Pour chaque valeur i dans p jusqu'à l'indice s (exclus),
        # on recherche la valeur maximale dans p qui peut être ajoutée à i sans dépasser lmt
        max_sum = max(i + p[bisect(p, lmt - i) - 1] for i in p[:s])

        # Affiche la somme maximale trouvée
        print max_sum

if __name__ == '__main__':
    main()