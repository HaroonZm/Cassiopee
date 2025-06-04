nombre_de_lignes, nombre_de_colonnes = map(int, raw_input().split())

somme_maximale = 0

for indice_ligne in xrange(nombre_de_lignes):
    
    ligne_entree = map(int, raw_input().split())
    
    if indice_ligne != 0:
        ligne_entree = [element ^ 1 for element in ligne_entree]
    
    meilleure_valeur_ligne = 0

    if nombre_de_colonnes > 2:
        for indice_element in xrange(1, nombre_de_colonnes - 1):
            valeur_courante = (
                ligne_entree[0] +
                ligne_entree[-1] +
                sum(
                    (ligne_entree[indice]^1) ^ (indice == indice_element)
                    for indice in xrange(1, nombre_de_colonnes - 1)
                )
            )
            if valeur_courante > meilleure_valeur_ligne:
                meilleure_valeur_ligne = valeur_courante
    else:
        meilleure_valeur_ligne = 0

    debut_somme = ligne_entree[0] + sum(element ^ 1 for element in ligne_entree[1:])
    fin_somme   = ligne_entree[-1] + sum(element ^ 1 for element in ligne_entree[:-1])

    somme_maximale += max(meilleure_valeur_ligne, debut_somme, fin_somme)

print somme_maximale