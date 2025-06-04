def get_most_frequent_inputs():
    """
    Lit des entiers en entrée depuis l'utilisateur jusqu'à ce qu'une exception survienne (comme EOF ou entrée invalide).
    Compte la fréquence d'apparition de chaque entier.
    Affiche tous les entiers qui apparaissent avec la fréquence maximale (un par ligne, en ordre croissant).
    """
    # Dictionnaire pour stocker la fréquence de chaque entier saisi
    frequency_dict = {}

    # Variable pour garder en mémoire la fréquence maximale atteinte par un entier
    max_frequency = 1

    # Lecture des entrées utilisateur jusqu'à interruption (par une exception)
    while True:
        try:
            # Lecture d'un entier depuis l'entrée standard
            user_input = int(input())
            # Si l'entier n'est pas encore dans le dictionnaire, l'ajouter avec fréquence 1
            if user_input not in frequency_dict:
                frequency_dict[user_input] = 1
            else:
                # Sinon, incrémenter la fréquence de cet entier
                frequency_dict[user_input] += 1
                # Vérifier si cette nouvelle fréquence dépasse la fréquence maximale
                if max_frequency < frequency_dict[user_input]:
                    max_frequency = frequency_dict[user_input]
        except:
            # On quitte la boucle lors d'une exception (saisie non convertible ou EOF)
            break

    # Trier les éléments du dictionnaire par valeur clé (entiers), du plus petit au plus grand
    sorted_items = sorted(frequency_dict.items())

    # Parcourir tous les (entier, fréquence) et afficher l'entier si sa fréquence est maximale
    for number, count in sorted_items:
        if count == max_frequency:
            print(number)

if __name__ == "__main__":
    get_most_frequent_inputs()