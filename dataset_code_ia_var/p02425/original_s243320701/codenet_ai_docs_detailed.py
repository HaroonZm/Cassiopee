def initialize_bit_array(size):
    """
    Crée et retourne une liste (tableau de bits) initialisée à zéro.

    Args:
        size (int): La taille désirée du tableau de bits.

    Returns:
        list: Une liste contenant 'size' éléments, tous initialisés à 0.
    """
    return [0 for _ in range(size)]

def handle_query(bit_array, query):
    """
    Exécute une requête spécifique sur le tableau de bits selon le type d'opération.

    Args:
        bit_array (list): La liste représentant le tableau de bits.
        query (list): Une liste des arguments de la requête,
                      le premier élément étant le code d'opération sous forme de chaîne.

    Returns:
        None
    """
    order = query[0]

    # Opération selon la requête :
    if order == "0":
        # Tester si le bit à l'indice spécifié vaut 1
        print(1 if bit_array[int(query[1])] else 0)
    elif order == "1":
        # Mettre à 1 le bit à l'indice spécifié
        bit_array[int(query[1])] = 1
    elif order == "2":
        # Mettre à 0 le bit à l'indice spécifié
        bit_array[int(query[1])] = 0
    elif order == "3":
        # Basculer (effectuer un XOR avec 1) le bit à l'indice spécifié
        bit_array[int(query[1])] ^= 1
    elif order == "4":
        # Tester si tous les bits du tableau valent 1
        print(1 if all(bit_array) else 0)
    elif order == "5":
        # Tester si au moins un des bits du tableau vaut 1
        print(1 if any(bit_array) else 0)
    elif order == "6":
        # Tester si tous les bits sont à 0
        print(1 if not any(bit_array) else 0)
    elif order == "7":
        # Afficher la somme totale des bits (nombre de bits à 1)
        print(sum(bit_array))
    elif order == "8":
        # Calculer la valeur décimale du tableau interprété comme un nombre binaire
        tmp = 0
        for i in reversed(range(64)):
            tmp += bit_array[i] * 2**i
        print(tmp)

def main():
    """
    Point d'entrée principal du programme.
    Initialise un tableau de bits, lit et exécute les requêtes de l'utilisateur.
    """
    SIZE = 64  # Taille fixe du tableau de bits
    bit_array = initialize_bit_array(SIZE)

    # Lecture du nombre de requêtes à traiter
    num_queries = int(input())
    for _ in range(num_queries):
        # Lecture et découpage de la ligne de requête
        query = input().split()
        # Traitement de la requête
        handle_query(bit_array, query)

if __name__ == "__main__":
    main()