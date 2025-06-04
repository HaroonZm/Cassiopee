def collect_key_page_pairs():
    """
    Collecte des paires clé-valeur depuis l'entrée utilisateur jusqu'à ce qu'une erreur survienne (EOF ou entrée invalide).

    Les clés sont stockées dans une liste `key_list` et les valeurs (pages) correspondantes dans une liste de listes `page_list`. 
    Chaque élément de `page_list` correspond à la clé à la même position de `key_list`.

    Returns:
        tuple: Deux listes, `key_list` (list of str), et `page_list` (list of list of int).
    """
    key_list = []
    page_list = []
    while True:
        try:
            # Lecture d'une ligne d'entrée, séparation en deux parties : clé et page
            key, page = map(str, input().split())
            # Si la clé existe déjà dans key_list, on ajoute la page à la liste correspondante
            if key in key_list:
                page_list[key_list.index(key)].append(int(page))
            else:
                # Sinon, on ajoute la clé et la nouvelle liste contenant la page
                key_list.append(key)
                page_list.append([int(page)])
        except:
            # Arrêt sur exception (probablement EOF ou entrée invalide)
            break
    return key_list, page_list

def display_sorted_keys_and_pages(key_list, page_list):
    """
    Affiche les clés triées par ordre alphabétique avec leurs listes de pages triées dans l'ordre croissant.

    Args:
        key_list (list of str): Liste des clés collectées.
        page_list (list of list of int): Liste des listes de pages correspondantes à chaque clé.
    """
    # Création d'une copie triée de la liste de clés
    key_list_sorted = key_list[:]
    key_list_sorted.sort()
    # Pour chaque clé triée, récupérer la liste correspondante, la trier et afficher
    for key in key_list_sorted:
        print(key)
        # Récupération de la liste des pages pour cette clé puis tri
        ans = page_list[key_list.index(key)][:]
        ans.sort()
        # Affichage de la liste triée, séparée par des espaces
        print(' '.join(map(str, ans)))

def main():
    """
    Point d'entrée du programme.
    Collecte les entrées utilisateur, puis affiche les résultats triés.
    """
    # Collecte des paires clé-page
    key_list, page_list = collect_key_page_pairs()
    # Affichage des résultats triés
    display_sorted_keys_and_pages(key_list, page_list)

if __name__ == "__main__":
    main()