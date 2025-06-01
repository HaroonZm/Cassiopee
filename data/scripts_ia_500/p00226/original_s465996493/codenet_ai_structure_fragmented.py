def lire_entree():
    return raw_input().split(' ')

def verifier_condition_sortie(a, b):
    return a == '0' and b == '0'

def convertir_en_liste(val):
    return list(val)

def initialiser_compteurs():
    return 0, 0

def compteur_hits_brs(a, b):
    br = 0
    hit = 0
    for i, data in enumerate(b):
        if verifier_presence(data, a):
            if verifier_position(i, a, data):
                hit = incrementer(hit)
            else:
                br = incrementer(br)
    return hit, br

def verifier_presence(item, collection):
    return item in collection

def verifier_position(index, collection, valeur):
    return collection[index] == valeur

def incrementer(valeur):
    return valeur + 1

def afficher_resultat(hit, br):
    print hit, br

def boucle_principale():
    while True:
        a, b = lire_entree()
        if verifier_condition_sortie(a, b):
            break
        a_list = convertir_en_liste(a)
        b_list = convertir_en_liste(b)
        hit, br = compteur_hits_brs(a_list, b_list)
        afficher_resultat(hit, br)

if __name__ == '__main__':
    boucle_principale()