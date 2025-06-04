def lire_dantai():
    return int(input())

def lire_ligne():
    return input()

def lire_lignes(dantai):
    lignes = []
    for _ in range(1, dantai + 1):
        lignes.append(lire_ligne())
    return lignes

def split_ligne(ligne):
    return ligne.split()

def extraire_b1_b2(parts):
    return parts[0], parts[1]

def calculer_ecart(b1, b2):
    return int(b2) - int(b1)

def ajouter_un(valeur):
    return valeur + 1

def traiter_ligne(ligne):
    parts = split_ligne(ligne)
    b1, b2 = extraire_b1_b2(parts)
    ecart = calculer_ecart(b1, b2)
    result = ajouter_un(ecart)
    return result

def traiter_lignes(lignes):
    total = 0
    for ligne in lignes:
        total = incrementer_total(total, traiter_ligne(ligne))
    return total

def incrementer_total(total, ajout):
    return total + ajout

def afficher_resultat(resultat):
    print(resultat)

def main():
    dantai = lire_dantai()
    lignes = lire_lignes(dantai)
    resultat = traiter_lignes(lignes)
    afficher_resultat(resultat)

main()