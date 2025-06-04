def main():
    """
    Fonction principale qui lit les entrées, traite les candidats et calcule la valeur maximale obtenue
    en sélectionnant jusqu'à m candidats, selon les contraintes de disponibilité par type.
    """

    # Lecture des paramètres principaux :
    # n : nombre de candidats
    # m : nombre maximum de sélections à effectuer
    # c : nombre de types disponibles (pas utilisé ailleurs dans le code mais requis pour le format d'entrée)
    n, m, c = map(int, input().split())

    # Lecture du nombre d'occurrences permises par type. Le premier élément est ignoré pour un accès basé sur 1.
    # l[k] indique le nombre disponible du type k.
    l = [0] + list(map(int, input().split()))

    # Lecture de la liste des candidats. Chaque candidat est représenté par un tuple (type, valeur).
    w = [tuple(map(int, input().split())) for _ in range(n)]

    # Trie des candidats selon leur valeur décroissante.
    # Ce tri permet de sélectionner en priorité les candidats ayant la valeur la plus élevée.
    w.sort(key=lambda x: x[1], reverse=True)

    # Initialisation des variables de calcul :
    v = 0  # Somme des valeurs des candidats sélectionnés
    p = 0  # Nombre total de candidats sélectionnés

    # Parcours de la liste triée des candidats
    for i in range(n):
        candidate_type = w[i][0]  # Type du candidat courant
        candidate_value = w[i][1]  # Valeur du candidat courant

        # Vérifie si une occurrence du type de ce candidat est encore disponible
        if l[candidate_type]:
            # Consomme une unité de ce type
            l[candidate_type] -= 1
            # Ajoute sa valeur au total
            v += candidate_value
            # Incrémente le nombre de sélections
            p += 1
            # Si on a atteint la limite de sélections, on arrête
            if p == m:
                break

    # Affiche la somme maximale des valeurs des candidats sélectionnés
    print(v)

if __name__ == "__main__":
    main()