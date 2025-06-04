def shuffle(word, length):
    """
    Réorganise un mot en déplaçant les 'length' premiers caractères
    à la fin du mot.

    Args:
        word (str): Le mot à réorganiser.
        length (int): Le nombre de caractères à déplacer du début à la fin.

    Returns:
        str: Le mot transformé avec les premiers 'length' caractères à la fin.
    """
    # Convertir le mot en liste de caractères pour manipulation facile
    li = list(word)
    # Obtenir les 'length' premiers caractères
    ad = li[0:length]
    # Ajouter ces caractères à la fin de la liste
    li += ad
    # Supprimer les 'length' premiers caractères d'origine
    del li[0:length]
    # Recréer la chaîne à partir de la liste modifiée et la retourner
    return ''.join(li)

# Boucle principale, continue à lire jusqu'à ce que l'utilisateur saisisse '-'
while True:
    # Lire la saisie utilisateur pour le mot à traiter
    string = input()
    if string == '-':
        # Arrêter le programme si l'utilisateur entre '-'
        break
    # Lire le nombre d'opérations de réorganisation à réaliser
    num = int(input())
    # Pour chaque opération
    for i in range(num):
        # Lire le nombre de caractères à déplacer pour cette opération
        rn = int(input())
        # Réorganiser le mot selon le nombre de caractères spécifié
        string = shuffle(string, rn)
    # Afficher le résultat final après toutes les opérations
    print(string)