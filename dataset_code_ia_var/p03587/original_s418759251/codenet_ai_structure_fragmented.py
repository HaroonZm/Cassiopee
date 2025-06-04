def lire_entree():
    return input()

def compter_uns(s):
    return s.count("1")

def afficher_resultat(res):
    print(res)

def main():
    entree = lire_entree()
    resultat = compter_uns(entree)
    afficher_resultat(resultat)

main()