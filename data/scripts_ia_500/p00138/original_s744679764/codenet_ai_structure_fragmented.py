def lire_lignes():
    return [raw_input().split()[::-1] for _ in [0]*8]

def trier_lignes(lignes):
    return sorted(lignes)

def extraire_x(lignes_triees):
    return lignes_triees[0:2]

def extraire_y(lignes_triees):
    return lignes_triees[2:4]

def ajouter_elements_liste(liste, elements):
    liste += elements

def trier_y_prendre_deux(y):
    return sorted(y)[0:2]

def afficher_elements(liste):
    for e in liste:
        print " ".join(e[::-1])

def boucle_principale():
    x = []
    y = []
    for _ in [0]*3:
        lignes = lire_lignes()
        lignes_triees = trier_lignes(lignes)
        x_elements = extraire_x(lignes_triees)
        y_elements = extraire_y(lignes_triees)
        ajouter_elements_liste(x, x_elements)
        ajouter_elements_liste(y, y_elements)
    ajout = trier_y_prendre_deux(y)
    ajouter_elements_liste(x, ajout)
    afficher_elements(x)

boucle_principale()