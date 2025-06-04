import copy

def main():
    """
    Propriétés du graphe :
    - Pas de boucle propre (pas d'arête de type (A, A))
    - Pas d'arête multiple (une seule arête entre deux nœuds donnés)
    - Graphe connexe (tous les nœuds sont accessibles depuis n'importe lequel)

    Un 'pont' est une arête qui, une fois retirée, rend le graphe non connexe.

    On cherche le nombre de ponts dans le graphe.
    """

    nombre_sommets, nombre_aretes = map(int, input().split())

    ensemble_aretes = set()
    for _ in range(nombre_aretes):
        sommet_depart, sommet_arrivee = map(int, input().split())
        ensemble_aretes.add((sommet_depart, sommet_arrivee))

    nombre_ponts = 0

    for arete_a_supprimer in ensemble_aretes:

        sommets_visites = set()
        ensemble_aretes_copie = copy.deepcopy(ensemble_aretes)
        ensemble_aretes_copie.remove(arete_a_supprimer)

        def parcours_profondeur(sommet_courant):
            sommets_visites.add(sommet_courant)
            for sommet_voisin in range(1, nombre_sommets + 1):
                if sommet_voisin in sommets_visites:
                    continue
                if (sommet_courant, sommet_voisin) in ensemble_aretes_copie or \
                   (sommet_voisin, sommet_courant) in ensemble_aretes_copie:
                    parcours_profondeur(sommet_voisin)

        sommet_racine = 1
        parcours_profondeur(sommet_racine)

        if len(sommets_visites) < nombre_sommets:
            nombre_ponts += 1

    print(nombre_ponts)

if __name__ == '__main__':
    main()