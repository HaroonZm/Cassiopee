nombre_de_sommets, nombre_de_aretes = map(int, raw_input().split())
liste_des_aretes = []
while True:
    sommet_source, sommet_cible, poids_arete = map(int, raw_input().split())
    if sommet_source == 0 and sommet_cible == 0 and poids_arete == 0:
        break
    liste_des_aretes.append([sommet_source - 1, sommet_cible - 1, poids_arete])
nombre_de_tests = int(raw_input())
for indice_test in xrange(nombre_de_tests):
    vecteur_entree = map(int, raw_input().split())
    vecteur_sortie = [0] * nombre_de_sommets
    for sommet_source, sommet_cible, poids_arete in liste_des_aretes:
        vecteur_sortie[sommet_source] += poids_arete * vecteur_entree[sommet_cible]
    print " ".join(map(str, vecteur_sortie))