def count_cyclic_occurrences(s, n, words):
    """
    Compte le nombre de mots parmi la liste `words` qui contiennent la chaîne `s` 
    comme sous-chaîne continue dans n'importe quelle rotation circulaire du mot.

    Args:
        s (str): La chaîne à rechercher comme motif dans les rotations circulaires.
        n (int): Le nombre de mots dans la liste.
        words (list of str): Liste des mots à vérifier.

    Returns:
        int: Le nombre de mots contenant `s` dans au moins une rotation circulaire.
    """
    ans = 0  # Compteur pour le nombre de mots où le motif est trouvé

    for r in words:
        found = False  # Indique si le motif a été trouvé dans ce mot
        len_r = len(r)  # Longueur du mot courant
        len_s = len(s)  # Longueur de la chaîne à rechercher

        # Pour chaque position de départ dans le mot r
        for start in range(len_r):
            flag = True  # Indique si le motif correspond depuis la position actuelle

            # Pour chaque caractère du motif s
            for k in range(len_s):
                # Calcul de la position circulaire dans r
                ri = (start + k) % len_r
                # Si le caractère ne correspond pas, motif non trouvé à cette position
                if r[ri] != s[k]:
                    flag = False
                    break  # Sortir de la boucle, la correspondance a échoué

            # Si tous les caractères correspondent, on a trouvé le motif dans cette rotation
            if flag:
                ans += 1
                found = True
                break  # On arrête la recherche dans ce mot ; on ne compte qu'une fois par mot

    return ans

# Partie principale du programme

if __name__ == "__main__":
    # Lire l'entrée utilisateur pour la chaîne s
    s = raw_input("Entrez la chaîne à rechercher : ")
    # Lire l'entrée utilisateur pour le nombre de mots
    n = input("Entrez le nombre de mots à vérifier : ")
    # Initialiser la liste des mots
    words = []

    # Lire chaque mot et l'ajouter à la liste
    for _ in range(n):
        r = raw_input("Entrez un mot : ")
        words.append(r)

    # Appeler la fonction et afficher le résultat
    result = count_cyclic_occurrences(s, n, words)
    print result  # Affiche le nombre de mots contenant s dans une rotation circulaire