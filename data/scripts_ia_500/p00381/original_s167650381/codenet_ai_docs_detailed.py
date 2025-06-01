def count_subsequences(N, s, t):
    """
    Calcule le nombre de sous-séquences de la chaîne 's' correspondant à la chaîne 't',
    selon une méthode spécifique.

    Args:
        N (int): La longueur des chaînes 's' et 't'.
        s (str): La chaîne source dans laquelle on cherche des sous-séquences.
        t (str): La chaîne cible à compter comme sous-séquence dans 's'.

    Returns:
        int: Le nombre de sous-séquences de 's' correspondant à 't',
             modulo 10^9 + 7.
    """
    MOD = 10**9 + 7

    # Initialiser le dictionnaire D avec la dernière lettre de t comme clé et 1 comme valeur:
    # Cela signifie qu'il y a exactement une façon de former le suffixe de t à partir de cette dernière lettre.
    D = {t[-1]: 1}

    # Itérer à l'envers sur les positions dans 's' de N-2 à 1 inclus (indices 1..N-2 en ordre décroissant):
    for i in range(N - 2, 0, -1):
        si = s[i]  # caractère courant dans s
        ti = t[i]  # caractère courant dans t

        # Récupère le nombre de façons de former la sous-séquence commençant par si,
        # par exemple, combien de fois si apparaît dans les combinaisons précédentes (ou 0 si absent).
        v = D.get(si, 0)

        # Met à jour le nombre de façons de former la sous-séquence commençant par ti.
        # Cela correspond à l'ajout du nombre d'occurrences déjà comptées de ti plus celles de si.
        D[ti] = (D.get(ti, 0) + v) % MOD

    # À la fin, on renvoie le nombre de façons de former la sous-séquence correspondant à s[0] selon D,
    # ou 0 si aucune occurrence.
    return D.get(s[0], 0)


if __name__ == "__main__":
    # Lecture de la taille des chaînes
    N = int(input())

    # Lecture des chaînes s et t
    s = input()
    t = input()

    # Affichage du résultat calculé
    print(count_subsequences(N, s, t))