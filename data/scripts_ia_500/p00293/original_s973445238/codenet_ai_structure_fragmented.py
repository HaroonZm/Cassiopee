import math

INF = 10 ** 18

def lire_entiers():
    return list(map(int, raw_input().split()))

def extraire_heures_minutes(liste):
    minutes_temps = []
    for i in range(1, len(liste), 2):
        h = liste[i]
        m = liste[i + 1]
        minutes_temps.append((h, m))
    return minutes_temps

def ajouter_dans_ensemble(ensemble, elements):
    for e in elements:
        ensemble.add(e)

def trier_temps(ensemble):
    return sorted(list(ensemble))

def formater_heure_minute(h, m):
    if m >= 10:
        return str(h) + ":" + str(m)
    else:
        return str(h) + ":0" + str(m)

def formater_liste_temps(liste_temps):
    for i in range(len(liste_temps)):
        h, m = liste_temps[i]
        liste_temps[i] = formater_heure_minute(h, m)
    return liste_temps

def afficher_liste(liste):
    print " ".join(liste)

def main():
    ls = set()
    ls1 = lire_entiers()
    ls2 = lire_entiers()
    elements1 = extraire_heures_minutes(ls1)
    elements2 = extraire_heures_minutes(ls2)
    ajouter_dans_ensemble(ls, elements1)
    ajouter_dans_ensemble(ls, elements2)
    ls_tri = trier_temps(ls)
    ls_formate = formater_liste_temps(ls_tri)
    afficher_liste(ls_formate)

main()