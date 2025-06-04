from heapq import heappush, heappop

# Lecture des dimensions et des paramètres
hauteur_grille, largeur_grille, temps_attente, nombre_requetes = map(int, input().split())

etat_cellule = [[0] * (largeur_grille + 1) for _ in range(hauteur_grille + 1)]

class ArbreBinaire2D:
    def __init__(self, max_hauteur, max_largeur):
        self.table_binaire = [[0] * (max_largeur + 1) for _ in range(max_hauteur + 1)]
        self.max_hauteur = max_hauteur
        self.max_largeur = max_largeur

    def ajouter(self, ligne, colonne, valeur):
        ligne_courante = ligne
        while ligne_courante <= self.max_hauteur:
            colonne_courante = colonne
            reference_colonne = self.table_binaire[ligne_courante]
            while colonne_courante <= self.max_largeur:
                reference_colonne[colonne_courante] += valeur
                colonne_courante += colonne_courante & -colonne_courante
            ligne_courante += ligne_courante & -ligne_courante

    def somme_prefixe(self, ligne, colonne):
        resultat = 0
        ligne_courante = ligne
        while ligne_courante > 0:
            colonne_courante = colonne
            reference_colonne = self.table_binaire[ligne_courante]
            while colonne_courante > 0:
                resultat += reference_colonne[colonne_courante]
                colonne_courante -= colonne_courante & -colonne_courante
            ligne_courante -= ligne_courante & -ligne_courante
        return resultat

    def somme_region(self, debut_ligne, debut_colonne, fin_ligne, fin_colonne):
        return (
            self.somme_prefixe(fin_ligne, fin_colonne)
            - self.somme_prefixe(debut_ligne - 1, fin_colonne)
            - self.somme_prefixe(fin_ligne, debut_colonne - 1)
            + self.somme_prefixe(debut_ligne - 1, debut_colonne - 1)
        )

    def afficher(self):
        for ligne in self.table_binaire:
            print(ligne)

    def sommes_intermediaires(self, debut_ligne, debut_colonne, fin_ligne, fin_colonne):
        return [
            self.somme_prefixe(fin_ligne, fin_colonne),
            self.somme_prefixe(debut_ligne - 1, fin_colonne),
            self.somme_prefixe(fin_ligne, debut_colonne - 1),
            self.somme_prefixe(debut_ligne - 1, debut_colonne - 1)
        ]

file_evenements = []
arbre_cellules_encours = ArbreBinaire2D(hauteur_grille, largeur_grille)
arbre_cellules_terminees = ArbreBinaire2D(hauteur_grille, largeur_grille)

for numero_requete in range(nombre_requetes):
    ligne_entree = list(map(int, input().split()))
    temps_actuel, code_operation, *parametres = ligne_entree

    # Libérer les événements dont le temps est écoulé
    while file_evenements and file_evenements[0][0] <= temps_actuel:
        temps_echeance, ligne_cellule, colonne_cellule = heappop(file_evenements)
        arbre_cellules_encours.ajouter(ligne_cellule, colonne_cellule, -1)
        arbre_cellules_terminees.ajouter(ligne_cellule, colonne_cellule, 1)
        etat_cellule[ligne_cellule][colonne_cellule] = 2  # Etat terminé

    if code_operation == 0:
        ligne_cellule, colonne_cellule = parametres
        etat_cellule[ligne_cellule][colonne_cellule] = 1  # Etat en cours
        arbre_cellules_encours.ajouter(ligne_cellule, colonne_cellule, 1)
        heappush(file_evenements, (temps_actuel + temps_attente, ligne_cellule, colonne_cellule))
    elif code_operation == 1:
        ligne_cellule, colonne_cellule = parametres
        if etat_cellule[ligne_cellule][colonne_cellule] == 2:
            arbre_cellules_terminees.ajouter(ligne_cellule, colonne_cellule, -1)
            etat_cellule[ligne_cellule][colonne_cellule] = 0  # Etat remis à vide
    else:
        debut_ligne, debut_colonne, fin_ligne, fin_colonne = parametres
        nombre_terminees = arbre_cellules_terminees.somme_region(debut_ligne, debut_colonne, fin_ligne, fin_colonne)
        nombre_encours = arbre_cellules_encours.somme_region(debut_ligne, debut_colonne, fin_ligne, fin_colonne)
        print(nombre_terminees, nombre_encours)