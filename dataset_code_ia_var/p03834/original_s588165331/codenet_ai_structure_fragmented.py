def lire_entree():
    return input()

def remplacer_virgules(texte):
    return texte.replace(",", " ")

def afficher_texte(texte):
    print(texte)

def main():
    entree = lire_entree()
    texte_modifie = remplacer_virgules(entree)
    afficher_texte(texte_modifie)

main()