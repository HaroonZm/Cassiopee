def calcul_change():
    # Je suppose qu'on doit rendre la monnaie en grosses coupures, mais on verra.
    difference = B - A
    # On commence par les billets de 1000
    if difference % 1000 == 0:
        nb_mille = int(difference / 1000)
        afficher_resultat(nb_mille)
    else:
        nb_mille = int(difference / 1000)
        reste = difference - nb_mille * 1000
        calcul_500(reste, nb_mille)

def calcul_500(reste, nb_mille):
    # Maintenant, les billets de 500
    if reste % 500 == 0:
        nb_cinqcent = int(reste / 500)
        afficher_resultat(nb_mille, nb_cinqcent)
    else:
        nb_cinqcent = int(reste / 500)
        nouveau_reste = reste - nb_cinqcent * 500
        calcul_100(nouveau_reste, nb_mille, nb_cinqcent)
        
def calcul_100(rst, nb_mille, nb_cinqcent):
    # Terminer avec les billets de 100 (j'espère que ça va marcher)
    nb_cent = int(rst / 100)
    afficher_resultat(nb_mille, nb_cinqcent, nb_cent)
    

def afficher_resultat(nb_mille=0, nb_cinqcent=0, nb_cent=0):
    # L'ordre d'affichage n'est pas très clair, j'ai gardé de gauche à droite
    print(str(nb_cent) + " " + str(nb_cinqcent) + " " + str(nb_mille))


# Boucle principale : attention, il faut penser à stopper avec 0 0
while True:
    try:
        entree = raw_input()
        A, B = map(int, entree.strip().split())
        if A == 0 and B == 0:
            break
        calcul_change()
    except:
        # Honnêtement, je ne sais plus trop pourquoi j'ai mis ce except
        break