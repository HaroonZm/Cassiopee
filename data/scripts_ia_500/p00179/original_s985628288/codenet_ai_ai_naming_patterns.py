ensemble_couleurs_rgb = set(["r", "g", "b"])
while True:
    entree_ver = raw_input()
    if entree_ver == "0":
        break
    longueur_ver = len(entree_ver)
    taille_ensemble = 1
    compteur_iterations = 0
    trouve_sequence_uni = False
    ensemble_files = set([entree_ver])
    while True:
        liste_files = list(ensemble_files)
        ensemble_files = set()
        for _ in range(taille_ensemble):
            ver_courant = liste_files.pop(0)
            if len(set(ver_courant)) == 1:
                trouve_sequence_uni = True
                break
            for index in range(longueur_ver -1):
                if ver_courant[index] != ver_courant[index + 1]:
                    couleur_suivante = list(ensemble_couleurs_rgb - set(ver_courant[index:index + 2]))[0]
                    nouvelle_chaine = ver_courant[:index] + 2 * couleur_suivante + ver_courant[index + 2:]
                    ensemble_files.add(nouvelle_chaine)
        taille_ensemble = len(ensemble_files)
        if trouve_sequence_uni:
            break
        compteur_iterations += 1
        if compteur_iterations > 15:
            break
    if trouve_sequence_uni:
        print(compteur_iterations)
    else:
        print("NA")