def main():
    """
    Programme principal qui recherche, pour plusieurs jardins de tailles différentes, le volume maximal d'un étang
    qui peut être formé dans une matrice. La surface d'un étang doit être minimale de 3x3, ses bords doivent être
    strictement plus élevés que l'intérieur, et le volume correspond à la somme des différences de niveau,
    pour chaque case intérieure, avec le bord minimal.
    """
    while True:
        # Lecture du nombre de lignes (d) et colonnes (w) du jardin
        d, w = map(int, input().split())
        if d == 0:
            # Arrête la boucle si d vaut 0 (fin des données)
            break

        # Construction de la matrice représentant le jardin
        garden = []
        for i in range(d):
            # Ajout de chaque ligne (convertie en entier) à la matrice
            garden.append(list(map(int, input().split())))

        pondmax = 0  # Variable stockant le volume maximal d'un étang trouvé

        # Parcours de tous les sous-rectangles d'au moins 3x3 dans le jardin
        for tly in range(len(garden)):  # tly = top left y (coordonnée ligne coin supérieur gauche)
            for tlx in range(len(garden[0])):  # tlx = top left x (coordonnée colonne coin supérieur gauche)
                # Limites maximales du sous-rectangle, minimum 3x3
                for bry in range(tly + 2, len(garden)):  # bry = bottom right y
                    for brx in range(tlx + 2, len(garden[0])):  # brx = bottom right x
                        # Initialisation des listes pour les bords (d_gray) et l'intérieur (l_gray)
                        l_gray = []  # Cellules intérieures de l'étang candidat
                        d_gray = []  # Cellules du bord de l'étang candidat

                        # Parcours de chaque case du sous-rectangle
                        for spy in range(tly, bry + 1):  # spy = sub y
                            for spx in range(tlx, brx + 1):  # spx = sub x
                                if (spy == tly or spy == bry or spx == tlx or spx == brx):
                                    # Si la case est sur le bord extérieur du rectangle, l'ajouter à d_gray
                                    d_gray.append(garden[spy][spx])
                                else:
                                    # Sinon, ajouter à l'intérieur
                                    l_gray.append(garden[spy][spx])

                        # Vérification de la condition : le minimum du bord > maximum de l'intérieur
                        if l_gray and d_gray and min(d_gray) > max(l_gray):
                            # Calcul du volume du bassin possible dans ce sous-rectangle
                            pond = 0
                            for depth in l_gray:
                                # Ajouter différence entre le bord le plus bas et chaque case intérieure
                                pond += min(d_gray) - depth
                            if pond > pondmax:
                                # Mise à jour du volume maximal trouvé
                                pondmax = pond

        # Affichage du plus gros volume d'étang trouvable dans ce jardin
        print(pondmax)
                        
main()