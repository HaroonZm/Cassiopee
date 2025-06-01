def lire_entiers():
    return map(int, input().split())

def calculer_secondes(h, m, s):
    return h * 3600 + m * 60 + s

def calculer_duree(h1, m1, s1, h2, m2, s2):
    temps1 = calculer_secondes(h1, m1, s1)
    temps2 = calculer_secondes(h2, m2, s2)
    return temps2 - temps1

def extraire_heures(duree):
    return duree // 3600

def extraire_minutes(duree):
    return (duree % 3600) // 60

def extraire_secondes(duree):
    return duree % 60

def afficher_duree(h, m, s):
    print(h, m, s)

def traiter_une_entree():
    h1, m1, s1, h2, m2, s2 = lire_entiers()
    duree = calculer_duree(h1, m1, s1, h2, m2, s2)
    h = extraire_heures(duree)
    m = extraire_minutes(duree)
    s = extraire_secondes(duree)
    afficher_duree(h, m, s)

def main():
    for _ in range(3):
        traiter_une_entree()

main()