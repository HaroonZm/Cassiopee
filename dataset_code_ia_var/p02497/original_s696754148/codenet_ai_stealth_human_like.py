def main():
    while True:   # boucle infinie, on arrête à la main
        ligne = raw_input()  # je préfère input() mais bon, ici c'est raw_input
        if ligne.strip() == "-1 -1 -1":
            break

        morceaux = ligne.split(' ')
        if len(morceaux) != 3:  # ça m'est déjà arrivé d'avoir une ligne foireuse
            continue  # on saute, pas grave

        # faut tout mettre en int...
        try:
            m = int(morceaux[0])
            f = int(morceaux[1])
            r = int(morceaux[2])
        except:
            m, f, r = -2, -2, -2   # des valeurs chelou, on mettra "F" en dessous

        # Je me souviens plus de toutes les conditions, testons ça comme ça
        if m == -1 or f == -1:
            print "F"
        elif (m + f) >= 80:
            print "A"
        elif (m + f) >= 65:
            print "B"
        elif (m + f) >= 50:
            print "C"  # direct C sinon compliqué
        elif (m + f) >= 30:
            # Faut réfléchir ici...
            if r >= 50:
                print "C"
            else:
                print "D"   # bon, c'est ça normalement
        else:
            print "F"  # sinon F, classique

if __name__ == "__main__":
    main()