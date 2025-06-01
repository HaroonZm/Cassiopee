# Programme pour calculer la différence maximale d'âges entre Hatsumi et Taku

# Import nécessaire pour manipuler les dates
from datetime import date, timedelta

def is_leap_year(year):
    """
    Détermine si une année est bissextile.
    Règles :
    - Divisible par 400 => bissextile
    - Divisible par 100 mais pas par 400 => non bissextile
    - Divisible par 4 mais pas par 100 => bissextile
    - Sinon non bissextile
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def next_birthday(birth_y, birth_m, birth_d, year):
    """
    Calcule la date anniversaire pour une année donnée en tenant compte que si la date
    est le 29 février (jour spécial des années bissextiles), 
    alors dans une année non bissextile, l'anniversaire est décalé au 1er mars.
    """
    # Si la date de naissance est le 29 février
    if birth_m == 2 and birth_d == 29:
        if is_leap_year(year):
            # L'année est bissextile, anniversaire le 29 février
            return date(year, 2, 29)
        else:
            # Année non bissextile, anniversaire le 1er mars
            return date(year, 3, 1)
    else:
        # Narcissique, anniversaire à la date exacte
        return date(year, birth_m, birth_d)

def age_on_date(birth_y, birth_m, birth_d, current_date):
    """
    Calcule l'âge à la date spécifiée, en tenant compte des règles particulières
    pour les anniversaires le 29 février.
    L'âge augmente au moment où débute la date anniversaire.
    """
    # Calcul de la date anniversaire dans l'année courante de current_date
    bday = next_birthday(birth_y, birth_m, birth_d, current_date.year)
    # Si l'anniversaire est postérieur ou égal à la date courante, l'âge est calculé
    # en soustrayant 1 car l'anniversaire n'a pas encore eu lieu cette année (sauf si égal)
    if current_date >= bday:
        return current_date.year - birth_y
    else:
        return current_date.year - birth_y - 1

def main():
    # Lecture des données d'entrée
    y1, m1, d1 = map(int, input().split())
    y2, m2, d2 = map(int, input().split())

    # On détermine qui est le plus âgé pour optimiser le calcul
    # On prendra en compte que la différence est absolue, mais pour trouver la max diff,
    # on calcule toujours âge plus âgé - âge plus jeune
    # Si première personne plus jeune, échange
    birth1 = (y1, m1, d1)
    birth2 = (y2, m2, d2)

    # Comparaison des dates de naissance pour déterminer l'ordre
    if (y1, m1, d1) > (y2, m2, d2):
        birth_older = birth2
        birth_younger = birth1
    else:
        birth_older = birth1
        birth_younger = birth2

    # L'âge maximal viendra à partir de l'année où la différence d'âge augmente pour la dernière fois.
    # Plus précisément, l'âge augmente à l'arrivée des anniversaires, 
    # Cette différence évolue uniquement aux dates d'anniversaire des deux individus.
    #
    # L'idée :
    # On considère un intervalle d'années à tester. La différence d'âge maximale ne croît plus après
    # un certain point. Cet âge maximal correspond à la différence en années complètement écoulées.
    #
    # Nous allons simuler, année par année, la différence dores et déjà en tenant compte des anniversaires.

    # On détermine l'année de départ : le plus jeune doit avoir au minimum 0 an
    start_year = max(birth_older[0], birth_younger[0])

    # Limite haute arbitraire : 3000 (max année possible) + 100 ans pour couvrir tous les cas
    end_year = 3100

    max_diff = 0

    # On crée un ensemble de dates où la différence peut changer : anniversaires des 2 personnes chaque année
    # On récupère toutes ces dates dans intervalle fixé, et on calcule différence à chaque date.

    # Pour optimiser, on ne testera que ces dates où la différence peut changer

    # Stockage des points de contrôle
    change_points = []

    for y in range(start_year, end_year+1):
        try:
            bday_older = next_birthday(*birth_older, y)
            change_points.append(bday_older)
        except ValueError:
            # Date invalide, probablement 29/02 dans année non bissextile => traité dans next_birthday
            pass
        try:
            bday_younger = next_birthday(*birth_younger, y)
            change_points.append(bday_younger)
        except ValueError:
            pass

    # Supprime doublons
    change_points = list(set(change_points))
    change_points.sort()

    # Pour chaque point, calcule la différence d'âge
    for current_date in change_points:
        # On calcule l'age des deux à la date actuelle
        age_older = age_on_date(*birth_older, current_date)
        age_younger = age_on_date(*birth_younger, current_date)
        diff = age_older - age_younger
        if diff > max_diff:
            max_diff = diff

    print(max_diff)

if __name__ == "__main__":
    main()