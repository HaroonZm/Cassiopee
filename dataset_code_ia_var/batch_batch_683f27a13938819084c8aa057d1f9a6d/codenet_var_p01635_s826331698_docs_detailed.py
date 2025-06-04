def calculate_time(n, t, F):
    """
    Calcule le temps requis en fonction des paramètres d'entrée.

    Args:
        n (int): Un entier utilisé pour les opérations arithmétiques.
        t (int): Un entier représentant une unité de temps.
        F (list of str): Une liste de caractères correspondant à des opérations.

    Returns:
        int or str: Le temps total calculé ou 'TLE' si le temps dépasse 1_000_000_000.
    """
    total = 0  # Initialise le total à 0

    # Traite chaque élément de la liste F jusqu'à ce qu'elle soit vide
    while F != []:
        tmp = F.pop(0)  # Prend le premier caractère de la liste
        # Si c'était le dernier élément, ajoute n au total
        if F == []:
            total += n
        # Si c'est un caractère 'n', on vérifie la prochaine opération
        elif tmp == "n":
            p = F.pop(0)  # Prend l'opérateur suivant
            # Si l'opérateur est l'exponentiation
            if p == "^":
                num = F.pop(0)  # Prend le prochain nombre pour l'exposant
                total += pow(n, int(num))  # Ajoute n élevé à la puissance num au total
            else:
                total += n  # Ajoute n au total si ce n'est pas une exponentiation

    time = total * t  # Calcule le temps total

    # Si le temps total dépasse le seuil, retourne 'TLE' (Time Limit Exceeded)
    if time > 1_000_000_000:
        return "TLE"
    # Sinon, retourne le temps calculé
    else:
        return time


if __name__ == "__main__":
    # Lecture des deux entiers séparés par un espace
    n, t = map(int, input().split())
    # Lecture de la chaîne représentant la formule et conversion en liste de caractères
    F = list(input())

    # Appel de la fonction pour obtenir le résultat
    result = calculate_time(n, t, F)
    # Affiche le résultat à l'utilisateur
    print(result)