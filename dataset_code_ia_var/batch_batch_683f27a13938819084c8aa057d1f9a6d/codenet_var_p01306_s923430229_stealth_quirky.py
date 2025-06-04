# Codage par un original : conventions personnalisées, noms ludiques, structure bizarre

TailleGrandeur = {
    "yotta":24, "zetta":21, "exa":18, "peta":15, "tera":12, "giga":9, "mega":6,
    "kilo":3, "hecto":2, "deca":1, "deci":-1, "centi":-2, "milli":-3,
    "micro":-6, "nano":-9, "pico":-12, "femto":-15, "ato":-18, "zepto":-21, "yocto":-24
}

nbTour = int(input())
boucle = 0
while boucle < nbTour:
    entree = input().split()
    if len(entree) == 2:
        valeur, unite = entree
        bonus = 0
    else:
        valeur, prefixe, unite = entree
        bonus = TailleGrandeur[prefixe]

    # Forcer le point
    if "." not in valeur:
        valeur += "."

    localisation = valeur.find(".")
    valeur = valeur[:localisation] + valeur[localisation+1:]

    # suppression esthétique des zéros
    while valeur and valeur[0] == "0":
        valeur = valeur[1:]
        localisation -= 1

    # Numération symbolique personnalisée 
    if len(valeur) > 1:
        valeur = "%s.%s"%(valeur[0], valeur[1:])

    bonus += localisation - 1

    print(f"{valeur} _* 10^{bonus} {unite}")
    boucle += 1