import sys

def read_input():
    """
    Lit les lignes de l'entrée standard, supprime les espaces en début et fin,
    puis divise chaque ligne en un mot et un nombre.
    Retourne une liste de tuples (mot, nombre).
    """
    items = []
    for line in sys.stdin.readlines():
        line = line.strip()  # Supprime les espaces en début/fin de ligne
        word, num = line.split()  # Sépare la ligne en mot et nombre
        items.append((word, int(num)))  # Ajoute le tuple (mot, nombre entier)
    return items

def build_dictionary(items):
    """
    Construit un dictionnaire à partir d'une liste de tuples (mot, nombre).
    Les clés sont les mots et les valeurs sont des listes d'entiers.
    Args:
        items (list of tuples): Liste des couples (mot, nombre).
    Returns:
        dict: Dictionnaire avec le mot en clé et liste des nombres en valeur.
    """
    dictionary = dict()
    for word, num in items:
        if word not in dictionary:
            dictionary[word] = []  # Initialise la liste si mot non présent
        dictionary[word].append(num)  # Ajoute le nombre à la liste du mot
    return dictionary

def print_dictionary(dictionary):
    """
    Affiche le contenu du dictionnaire.
    Trie les mots par ordre alphabétique et affiche, pour chaque mot, 
    les entiers associés triés dans l'ordre croissant.
    Args:
        dictionary (dict): Dictionnaire à afficher.
    """
    for key in sorted(dictionary.keys()):
        print(key)
        print(" ".join(map(str, sorted(dictionary[key]))))

def main():
    """
    Fonction principale qui lance le processus :
    - Lecture de l'entrée standard,
    - Construction du dictionnaire,
    - Affichage des résultats.
    """
    items = read_input()
    dictionary = build_dictionary(items)
    print_dictionary(dictionary)

if __name__ == "__main__":
    main()