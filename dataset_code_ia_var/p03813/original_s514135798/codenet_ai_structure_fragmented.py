def lire_entree():
    return input()

def convertir_entier(val):
    return int(val)

def est_inferieur_a_1200(n):
    return n < 1200

def afficher_abc():
    print("ABC")

def afficher_arc():
    print("ARC")

def analyser_et_afficher(n):
    if est_inferieur_a_1200(n):
        afficher_abc()
    else:
        afficher_arc()

def main():
    entree = lire_entree()
    nombre = convertir_entier(entree)
    analyser_et_afficher(nombre)

main()