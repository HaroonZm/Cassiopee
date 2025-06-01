def lire_date():
    return map(int, input().split())

def echange_dates_si_necessaire(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        return y2, m2, d2, y1, m1, d1
    if y1 == y2:
        if m1 > m2:
            return y2, m2, d2, y1, m1, d1
        if m1 == m2 and d1 > d2:
            return y2, m2, d2, y1, m1, d1
    return y1, m1, d1, y2, m2, d2

def condition_print1(m1, d1, m2, d2):
    if m1 < m2:
        return True
    if m1 == m2 and d1 < d2:
        return True
    return False

def calcul_annees(y1, y2, m1, d1, m2, d2):
    if condition_print1(m1, d1, m2, d2):
        return y2 - y1 + 1
    return y2 - y1

def afficher_resultat(resultat):
    print(resultat)

def main():
    y1, m1, d1 = lire_date()
    y2, m2, d2 = lire_date()
    y1, m1, d1, y2, m2, d2 = echange_dates_si_necessaire(y1, m1, d1, y2, m2, d2)
    resultat = calcul_annees(y1, y2, m1, d1, m2, d2)
    afficher_resultat(resultat)

main()