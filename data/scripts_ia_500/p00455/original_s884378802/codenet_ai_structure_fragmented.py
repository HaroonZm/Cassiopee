def lire_entree():
    return list(map(int, input().split()))

def calculer_secondes_debut(a):
    return 3600 * a[0] + 60 * a[1] + a[2]

def calculer_secondes_fin(a):
    return 3600 * a[3] + 60 * a[4] + a[5]

def calculer_duree(a):
    debut = calculer_secondes_debut(a)
    fin = calculer_secondes_fin(a)
    return fin - debut

def convertir_en_hms(secondes):
    heures = secondes // 3600
    reste = secondes % 3600
    minutes = reste // 60
    secondes_restantes = reste % 60
    return heures, minutes, secondes_restantes

def afficher_hms(h, m, s):
    print('{0} {1} {2}'.format(h, m, s))

def traiter_une_line():
    a = lire_entree()
    duree = calculer_duree(a)
    h, m, s = convertir_en_hms(duree)
    afficher_hms(h, m, s)

def main():
    for _ in range(3):
        traiter_une_line()

main()