def read_input():
    """
    Lit les entrées standard pour obtenir le nombre d'éléments N et la fréquence F,
    puis les N lignes suivantes de données.

    Returns:
        N (int): Nombre de lignes de données à lire
        F (int): Fréquence minimale pour qu'une paire soit considérée
        data (list): Liste contenant N listes de chaînes, qui sont les entrées utilisateur
    """
    N, F = map(int, input().split())
    data = []
    for _ in range(N):
        # Ajoute chaque ligne d'entrée sous forme de liste à la liste principale 'data'
        data.append(list(input().split()))
    return N, F, data

def count_pairs(N, data):
    """
    Parcourt toutes les lignes de données et compte le nombre d'occurrences de chaque
    paire unique (a, b) de mots dans une même ligne (hors premier et dernier mot).

    Args:
        N (int): Le nombre de lignes dans la donnée
        data (list): Liste contenant N listes de chaînes

    Returns:
        tmp (dict): Dictionnaire avec pour clé un tuple trié (a, b)
                    et pour valeur le nombre d'occurrences de la paire
    """
    tmp = {}
    for i in range(N):
        # Pour chaque ligne, on considère uniquement les colonnes 1 à length-2 inclues
        for x in range(1, len(data[i]) - 1):
            for y in range(x + 1, len(data[i])):
                # Trie la paire pour garantir l'unicité quel que soit l'ordre d'apparition
                a, b = data[i][x], data[i][y]
                a, b = min(a, b), max(a, b)
                # Incrémente le compteur d'occurrence de la paire
                if (a, b) not in tmp:
                    tmp[(a, b)] = 1
                else:
                    tmp[(a, b)] += 1
    return tmp

def collect_frequent_pairs(tmp, F):
    """
    Récupère toutes les paires qui apparaissent au moins F fois.

    Args:
        tmp (dict): Dictionnaire des occurrences des paires
        F (int): Le seuil de fréquence minimale

    Returns:
        ans (list): Liste de listes de deux chaînes correspondant aux paires fréquentes
    """
    ans = []
    for k in tmp:
        if tmp[k] >= F:
            ans.append(list(k))
    return ans

def sort_pairs(ans):
    """
    Trie la liste des paires d'abord par le second élément, puis par le premier élément.

    Args:
        ans (list): Liste des paires sous forme [a, b]

    Returns:
        ans (list): Liste triée des paires
    """
    ans = sorted(ans, key=lambda x: x[1])
    ans = sorted(ans)
    return ans

def print_result(ans):
    """
    Affiche le nombre de paires fréquentes puis, le cas échéant, chacune d'elles.

    Args:
        ans (list): Liste des paires de mots fréquentes
    """
    print(len(ans))
    if len(ans) != 0:
        for i in range(len(ans)):
            print(*ans[i])

def main():
    """
    Programme principal qui orchestre la lecture des données, le comptage des paires,
    la filtration par fréquence, le tri et l'affichage du résultat.
    """
    N, F, data = read_input()                   # Lecture des entrées utilisateur
    tmp = count_pairs(N, data)                  # Comptage des paires dans les données lues
    ans = collect_frequent_pairs(tmp, F)        # Collecte les paires fréquentes
    ans = sort_pairs(ans)                       # Trie les paires pour l'affichage final
    print_result(ans)                           # Affiche le nombre et la liste des paires

if __name__ == "__main__":
    main()