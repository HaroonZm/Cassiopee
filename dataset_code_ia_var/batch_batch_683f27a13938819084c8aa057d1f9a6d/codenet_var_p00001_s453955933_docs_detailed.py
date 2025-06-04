def get_mountain_heights():
    """
    Demande à l'utilisateur de saisir les hauteurs de 10 montagnes et les stocke dans une liste.
    Retourne cette liste de hauteurs (en chaînes de caractères).
    """
    # Liste vide pour stocker les hauteurs saisies par l'utilisateur
    height = []

    # Boucle pour 10 itérations (une par montagne)
    for apple in range(10):
        # Demande à l'utilisateur de saisir la hauteur de la montagne en cours
        mountain = input()
        # Insère la valeur saisie juste avant la dernière position de la liste
        # (équivalent à append si la liste n'a pas encore d'élément)
        height.insert(-1, mountain)
    
    return height

def sort_heights_descending(heights):
    """
    Trie la liste des hauteurs en ordre décroissant (du plus grand au plus petit).
    Modifie la liste sur place.
    
    Args:
        heights (list): Liste des hauteurs des montagnes (chaînes de caractères ou entiers).
    """
    # Trie la liste dans l'ordre croissant
    heights.sort()
    # Inverse la liste pour obtenir l'ordre décroissant
    heights.reverse()

def print_top_three_heights(heights):
    """
    Affiche les trois plus grandes hauteurs de la liste.
    
    Args:
        heights (list): Liste triée des hauteurs des montagnes (ordre décroissant attendu).
    """
    # Affiche le plus grand élément (indice 0)
    print(heights[0])
    # Affiche le deuxième plus grand (indice 1)
    print(heights[1])
    # Affiche le troisième plus grand (indice 2)
    print(heights[2])

if __name__ == "__main__":
    # Récupère les 10 hauteurs saisies par l'utilisateur
    height_list = get_mountain_heights()
    # Trie les hauteurs dans l'ordre décroissant
    sort_heights_descending(height_list)
    # Affiche les trois plus grandes hauteurs
    print_top_three_heights(height_list)