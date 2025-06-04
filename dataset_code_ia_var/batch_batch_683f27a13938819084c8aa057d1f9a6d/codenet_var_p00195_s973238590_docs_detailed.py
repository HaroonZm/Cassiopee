def get_max_sale(names):
    """
    Traite des paires d'entiers entrées par l'utilisateur.
    Pour chaque groupe de 'len(names)' paires, calcule la somme pour chaque paire,
    puis affiche le nom associé à la plus grande somme ainsi que la somme elle-même.

    Args:
        names (list): Liste des noms associés à chaque entrée de données.

    Entrée de l'utilisateur:
        L'utilisateur doit entrer des paires d'entiers séparés par un espace.
        Entrer '0 0' arrêtera la saisie.

    Affichage:
        Pour chaque groupe de 'len(names)' paires saisies, affiche le nom dont la somme (a+b)
        est la plus élevée ainsi que cette somme.
    """
    shop = []  # Liste pour stocker les sommes de chaque vente dans un groupe
    while True:
        # Demande à l'utilisateur de saisir deux entiers séparés par un espace
        try:
            a, b = map(int, input().split())
        except ValueError:
            # Si l'entrée n'est pas valide, affiche un message et continue la saisie
            print("Veuillez entrer deux entiers séparés par un espace.")
            continue

        # Condition d'arrêt : l'utilisateur entre '0 0'
        if a == 0 and b == 0:
            break

        # Ajoute la somme a+b à la liste shop
        shop.append(a + b)

        # Si cinq sommes ont été collectées, traite le groupe
        if len(shop) == len(names):
            # Recherche la plus grande somme dans la liste
            m = max(shop)
            # Trouve l'indice de la première occurrence de cette somme maximale
            idx = shop.index(m)
            # Affiche le nom associé à cette somme ainsi que la somme
            print(names[idx], m)
            # Réinitialise la liste pour traiter un nouveau groupe
            shop = []

if __name__ == "__main__":
    # Liste des noms correspondant aux données saisies
    name = ['A', 'B', 'C', 'D', 'E']
    # Appelle la fonction principale pour démarrer le programme
    get_max_sale(name)