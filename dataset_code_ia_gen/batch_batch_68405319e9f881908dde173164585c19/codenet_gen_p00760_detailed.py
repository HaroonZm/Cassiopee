# Solution complète en Python avec commentaires détaillés

def is_big_year(year):
    # Les années multiples de 3 ont 10 big months toutes de 20 jours
    return year % 3 == 0

def days_in_month(year, month):
    # Retourne le nombre de jours dans un mois donné pour une année donnée
    if is_big_year(year):
        # Toutes les 10mois sont big months de 20 jours
        return 20
    else:
        # Année commune : big et small alternent, starting par big
        # Big month si mois impair, small month sinon
        if month % 2 == 1:
            return 20
        else:
            return 19

def days_in_year(year):
    # Retourne le nombre total de jours dans une année donnée
    if is_big_year(year):
        return 10 * 20  # 10 big months
    else:
        # Alternance 20+19+20+19+... sur 10 mois
        big_months = 5
        small_months = 5
        return big_months * 20 + small_months * 19

def total_days_until(year, month, day):
    # Calcule le nombre de jours depuis le début du calendrier (1/1/1) jusqu'à la date (year, month, day)
    # non inclus : 1/1/1 correspond à 0 jour
    total = 0
    # Ajouter jours des années complètes avant l'année courante
    for y in range(1, year):
        total += days_in_year(y)
    # Ajouter jours des mois complets avant le mois courant dans l'année courante
    for m in range(1, month):
        total += days_in_month(year, m)
    # Ajouter jours dans le mois courant avant le jour
    total += (day - 1)
    return total

def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    # Date du millennium: année 1000, mois 1, jour 1
    millennium_total_days = total_days_until(1000, 1, 1)

    for _ in range(n):
        Y, M, D = map(int, input().split())
        birth_total_days = total_days_until(Y, M, D)
        # Nombre de jours depuis la naissance (inclusive) jusqu'au millennium (exclusive)
        print(millennium_total_days - birth_total_days)

if __name__ == "__main__":
    main()