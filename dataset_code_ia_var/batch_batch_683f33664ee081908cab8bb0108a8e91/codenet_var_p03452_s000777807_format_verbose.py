import sys

# Augmente la limite de récursion pour éviter les problèmes de récursions profondes lors de la recherche du parent
sys.setrecursionlimit(10 ** 5)

# Lecture du nombre d'éléments et du nombre de relations
nombre_elements, nombre_relations = map(int, input().split())

# Redéfinition de la fonction d'entrée pour optimiser les lectures (lecture par ligne)
entree_optimisee = sys.stdin.readline

# Liste des contraintes sous forme de tuples (borne_gauche, borne_droite, difference)
liste_contraintes = [
    [int(valeur) for valeur in entree_optimisee().split()]
    for _ in range(nombre_relations)
]

# Initialisation des structures pour l'Union-Find avec gestion des différences pondérées
parent = [noeud for noeud in range(nombre_elements + 1)]
profondeur_racine = [0] * (nombre_elements + 1)
poids_diff_cumule = [0] * (nombre_elements + 1)

def trouver_racine(noeud_courant):
    """Trouve la racine du noeud et ajuste les pondérations cumulées"""
    if parent[noeud_courant] == noeud_courant:
        return noeud_courant
    else:
        racine = trouver_racine(parent[noeud_courant])
        poids_diff_cumule[noeud_courant] += poids_diff_cumule[parent[noeud_courant]]
        parent[noeud_courant] = racine
        return racine

def obtenir_poids(noeud):
    """Retourne le poids total du noeud jusqu'à la racine"""
    return poids_diff_cumule[noeud]

def difference_de_poids(noeud_gauche, noeud_droit):
    """Calcul de la différence de poids entre deux noeuds"""
    return obtenir_poids(noeud_droit) - obtenir_poids(noeud_gauche)

def fusionner_ensembles(noeud_gauche, noeud_droit, difference_attendue):
    """Fusionne deux ensembles avec une différence de poids spécifiée"""
    poids_ajuste = difference_attendue + obtenir_poids(noeud_gauche) - obtenir_poids(noeud_droit)
    racine_gauche = trouver_racine(noeud_gauche)
    racine_droite = trouver_racine(noeud_droit)

    if racine_gauche == racine_droite:
        return False
    
    if profondeur_racine[racine_gauche] < profondeur_racine[racine_droite]:
        racine_gauche, racine_droite = racine_droite, racine_gauche
        poids_ajuste = -poids_ajuste

    if profondeur_racine[racine_gauche] == profondeur_racine[racine_droite]:
        profondeur_racine[racine_gauche] += 1

    parent[racine_droite] = racine_gauche
    poids_diff_cumule[racine_droite] = poids_ajuste
    return True

def sont_dans_le_meme_ensemble(noeud_a, noeud_b):
    """Vérifie si deux noeuds appartiennent au même ensemble"""
    return trouver_racine(noeud_a) == trouver_racine(noeud_b)

for indice_relation in range(nombre_relations):

    borne_gauche, borne_droite, difference_poids = liste_contraintes[indice_relation]

    if not sont_dans_le_meme_ensemble(borne_gauche, borne_droite):
        fusionner_ensembles(borne_gauche, borne_droite, difference_poids)
    else:
        if difference_de_poids(borne_gauche, borne_droite) != difference_poids:
            print("No")
            exit(0)

print("Yes")