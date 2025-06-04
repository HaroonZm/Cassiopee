mot = input()
if len(mot) > 0:
    derniere_lettre = mot[len(mot)-1]
    if derniere_lettre == 's':
        print(mot + 'es')
    else:
        print(mot + 's')