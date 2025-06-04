def is_leap_year(year):
    """
    Détermine si une année donnée est une année bissextile.
    Selon les règles :
    - divisible par 400 -> bissextile
    - divisible par 100 mais pas par 400 -> non bissextile
    - divisible par 4 mais pas par 100 -> bissextile
    - sinon -> non bissextile
    """
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    """
    Retourne le nombre de jours dans un mois donné d'une année donnée.
    Prend en compte les années bissextiles pour février.
    """
    # Jours dans chaque mois (indice 1 -> janvier, etc.)
    days_per_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return days_per_month[month]

def days_from_start(year, month, day):
    """
    Calcule le nombre total de jours écoulés depuis une date de référence arbitraire (par exemple, 0/0/0)
    jusqu'à la date donnée (year, month, day).
    Cela facilite le calcul des jours entre deux dates en faisant la différence.
    """
    total_days = 0
    # Ajouter les jours complets des années avant l'année donnée
    for y in range(0, year):
        total_days += 366 if is_leap_year(y) else 365
    # Ajouter les jours complets des mois avant le mois donné dans l'année donnée
    for m in range(1, month):
        total_days += days_in_month(year, m)
    # Ajouter les jours dans le mois actuel (day)
    total_days += day
    return total_days

def main():
    while True:
        # Lire une ligne d'entrée composée de six entiers
        inputs = input().split()
        if len(inputs) != 6:
            # S'il n'y a pas 6 valeurs, on ignore cette ligne
            continue
        y1, m1, d1, y2, m2, d2 = map(int, inputs)
        # Condition d'arrêt : si l'une des valeurs est négative
        if y1 < 0 or m1 < 0 or d1 < 0 or y2 < 0 or m2 < 0 or d2 < 0:
            break
        # Calculer le nombre total de jours pour les deux dates
        days1 = days_from_start(y1, m1, d1)
        days2 = days_from_start(y2, m2, d2)
        # La différence est le nombre de jours entre les deux dates,
        # en incluant la date 1 mais pas la date 2 comme demandé
        print(days2 - days1)

if __name__ == "__main__":
    main()