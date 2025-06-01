def lire_entrees():
    return map(int, input().split())

def convertir_heure_en_secondes(h, m, s):
    return h * 3600 + m * 60 + s

def calculer_difference_temps(h, m, s, nh, nm, ns):
    t1 = convertir_heure_en_secondes(h, m, s)
    t2 = convertir_heure_en_secondes(nh, nm, ns)
    return t2 - t1

def extraire_heures_totales(t):
    return t // 3600

def extraire_minutes_totales(t):
    return (t % 3600) // 60

def extraire_secondes_totales(t):
    return t % 60

def afficher_temps(h, m, s):
    print(h, m, s)

def traiter_une_ligne():
    h, m, s, nh, nm, ns = lire_entrees()
    t = calculer_difference_temps(h, m, s, nh, nm, ns)
    h_res = extraire_heures_totales(t)
    m_res = extraire_minutes_totales(t)
    s_res = extraire_secondes_totales(t)
    afficher_temps(h_res, m_res, s_res)

def main():
    for _ in range(3):
        traiter_une_ligne()

main()