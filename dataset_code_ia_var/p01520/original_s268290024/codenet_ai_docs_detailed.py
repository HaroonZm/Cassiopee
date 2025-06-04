def find_watch_index(n, t, e, watch):
    """
    Détermine l'indice (1-based) du premier élément de la liste 'watch' pour lequel il existe un entier 'i' (0 <= i <= e)
    tel que (t + i) ou (t - i) soit un multiple de watch[w].
    Si aucun tel élément n'existe, retourne -1.

    Paramètres:
        n (int): Nombre d'éléments dans la liste 'watch'.
        t (int): Valeur cible à ajuster avec 'i'.
        e (int): Intervalle de tolérance autour de 't'.
        watch (list[int]): Liste des diviseurs potentiels.

    Retourne:
        int: Indice 1-based du premier 'watch' satisfaisant la condition, ou -1 si aucun n'existe.
    """
    # Parcourt tous les éléments de la liste 'watch'
    for w in range(n):
        # Parcourt tous les i possibles dans [0, e]
        for i in range(e + 1):
            # Vérifie si t + i est divisible par watch[w]
            if (t + i) % watch[w] == 0:
                return w + 1  # Indice 1-based
            # Vérifie si t - i est divisible par watch[w]
            if (t - i) % watch[w] == 0:
                return w + 1  # Indice 1-based
    # Aucun élément ne satisfait la condition
    return -1

def main():
    """
    Fonction principale qui lit l'entrée, appelle la logique de recherche, et affiche le résultat.
    """
    # Lecture et décomposition de la première ligne d'entrée
    n, t, e = map(int, input().split())

    # Lecture de la deuxième ligne correspondant à la liste 'watch'
    watch = list(map(int, input().split()))

    # Appel de la fonction de recherche et affichage du résultat
    result = find_watch_index(n, t, e, watch)
    print(result)

# Appel du point d'entrée
if __name__ == "__main__":
    main()