def lire_entrees():
    w, h, c = input().split(" ")
    return w, h, c

def convertir_en_entiers(w, h):
    w_int = int(w)
    h_int = int(h)
    return w_int, h_int

def ligne_haute_basse(w):
    return "+" + "-" * (w - 2) + "+"

def ligne_intermediaire_avec_point(w):
    return "|" + "." * (w - 2) + "|"

def ligne_centrale(w, c):
    nb_points = (w - 3) // 2
    return "|" + "." * nb_points + c + "." * nb_points + "|"

def afficher_ligne(ligne):
    print(ligne)

def afficher_cadre(w, h, c):
    afficher_ligne(ligne_haute_basse(w))
    for i in range(h - 2):
        if i * 2 == h - 3:
            afficher_ligne(ligne_centrale(w, c))
        else:
            afficher_ligne(ligne_intermediaire_avec_point(w))
    afficher_ligne(ligne_haute_basse(w))

def main():
    w, h, c = lire_entrees()
    w, h = convertir_en_entiers(w, h)
    afficher_cadre(w, h, c)

main()