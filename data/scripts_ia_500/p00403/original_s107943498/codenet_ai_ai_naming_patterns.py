nombre_elements = int(input())
liste_valeurs = [int(valeur) for valeur in input().split()]
pile_memoire = []
index_erreur_trouve = False

for index_courant in range(nombre_elements):
    valeur_courante = liste_valeurs[index_courant]
    if valeur_courante > 0:
        if valeur_courante in pile_memoire:
            print(index_courant + 1)
            index_erreur_trouve = True
            break
        else:
            pile_memoire.append(valeur_courante)
    else:
        valeur_abs_courante = abs(valeur_courante)
        if len(pile_memoire) > 0 and pile_memoire[-1] == valeur_abs_courante:
            pile_memoire.pop()
        else:
            print(index_courant + 1)
            index_erreur_trouve = True
            break

if not index_erreur_trouve:
    print("OK")