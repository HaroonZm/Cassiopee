def lire_entier():
    return int(raw_input())

def lire_heure_minute():
    return map(int, raw_input().split(":"))

def calculer_angle_aiguille_heures(hh, mm):
    return (60 * hh + mm) * 0.5

def calculer_angle_aiguille_minutes(mm):
    return 6 * mm

def calculer_difference_angle(angleh, anglem):
    diff = abs(angleh - anglem)
    if diff > 180:
        diff = 360 - diff
    return diff

def verifier_etat(diff):
    if 0 <= diff < 30:
        return "alert"
    elif 90 <= diff <= 180:
        return "safe"
    else:
        return "warning"

def traiter_heure():
    hh, mm = lire_heure_minute()
    angleh = calculer_angle_aiguille_heures(hh, mm)
    anglem = calculer_angle_aiguille_minutes(mm)
    diff = calculer_difference_angle(angleh, anglem)
    etat = verifier_etat(diff)
    print(etat)

def main():
    n = lire_entier()
    for _ in range(n):
        traiter_heure()

main()