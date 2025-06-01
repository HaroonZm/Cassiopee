def lire_nombre_de_tests():
    return int(raw_input())

def lire_heure():
    return raw_input()

def extraire_heures_minutes(heure_str):
    return [int(x) for x in heure_str.split(':')]

def calculer_angle_aigu_long(long_minutes):
    return long_minutes * 360 / 60.

def calculer_angle_aigu_short(short_heures, short_minutes):
    return short_heures * 360 / 12. + short_minutes * 30 / 60.

def ordonner_angles(angle1, angle2):
    return max(angle1, angle2), min(angle1, angle2)

def calculer_distance_entre_angles(longdeg, shortdeg):
    return min(longdeg - shortdeg, 360 - (longdeg - shortdeg))

def afficher_resultat(distance):
    if distance < 30:
        print 'alert'
    elif distance >= 90:
        print 'safe'
    else:
        print 'warning'

def traiter_heure(heure_str):
    t = extraire_heures_minutes(heure_str)
    longdeg = calculer_angle_aigu_long(t[1])
    shortdeg = calculer_angle_aigu_short(t[0], t[1])
    longdeg, shortdeg = ordonner_angles(longdeg, shortdeg)
    dist = calculer_distance_entre_angles(longdeg, shortdeg)
    afficher_resultat(dist)

def main():
    n = lire_nombre_de_tests()
    for _ in range(n):
        heure_str = lire_heure()
        traiter_heure(heure_str)

main()