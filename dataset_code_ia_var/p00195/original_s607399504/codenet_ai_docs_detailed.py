def get_input_scores():
    """
    Demande à l'utilisateur d'entrer une ligne composée d'entiers séparés par des espaces.
    Retourne la liste des entiers saisis.
    """
    sa = list(map(int, input().split()))
    return sa

def main():
    """
    Programme principal pour déterminer l'indice ayant le score total le plus élevé.
    L'utilisateur saisit cinq séries de valeurs entières (la première en dehors de la boucle, puis quatre dans la boucle).
    Le programme identifie l'indice de la liste ayant la somme maximale et l'affiche avec la valeur.
    S'arrête si l'utilisateur saisit "0 0" à la première ligne de chaque série.
    """
    # Dictionnaire reliant les indices aux lettres
    dic = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

    while True:
        # Saisie de la première ligne de valeurs
        sa = get_input_scores()

        # Condition d'arrêt : si l'utilisateur saisit [0, 0]
        if sa == [0, 0]:
            break

        # Stocke les sommes des cinq listes, en commençant par la première
        lst = [sum(sa)]

        # Traitement des quatre saisies suivantes
        for _ in range(4):
            scores = get_input_scores()
            lst.append(sum(scores))

        # Recherche de la somme maximale et de son indice
        max_score = max(lst)
        max_index = lst.index(max_score)

        # Affiche la lettre correspondante et la valeur maximale
        print(dic[max_index], max_score)

if __name__ == "__main__":
    main()