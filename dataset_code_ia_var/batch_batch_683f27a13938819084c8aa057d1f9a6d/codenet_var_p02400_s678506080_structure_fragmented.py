def lire_r():
    return float(input())

def valeur_p():
    return 3.14159265358979

def aire_cercle(r, p):
    return r * r * p

def perimetre_cercle(r, p):
    return 2 * r * p

def formater_resultat(aire, perimetre):
    return "%.5f %.5f" % (aire, perimetre)

def affiche_resultat(texte):
    print(texte)

def main():
    rayon = lire_r()
    pi = valeur_p()
    surface = aire_cercle(rayon, pi)
    perimetre = perimetre_cercle(rayon, pi)
    resultat = formater_resultat(surface, perimetre)
    affiche_resultat(resultat)

main()