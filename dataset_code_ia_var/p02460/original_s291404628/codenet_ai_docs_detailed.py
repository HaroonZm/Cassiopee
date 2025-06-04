def process_queries():
    """
    Lis un nombre d'opérations, puis exécute des instructions de manipulation d'un dictionnaire.
    - Fonctionne comme un simulateur de table de hachage simple avec mise, récupération et suppression.
    Entrée:
        - Un entier q (nombre de requêtes)
        - Pour chaque requête:
            - "0 key value": ajoute/actualise la clé 'key' avec la valeur 'value'
            - "1 key": affiche la valeur liée à 'key' si elle existe, sinon affiche 0
            - "2 key": supprime la clé 'key' du dictionnaire si elle existe
    Sortie: affiche les résultats des instructions de type "1"
    """
    # Nombre de requêtes à traiter
    q = int(input())
    # Dictionnaire pour stocker paires clé/valeur
    dict_data = {}
    # Boucle sur chaque requête
    for _ in range(q):
        # Lecture de la requête et découpage en éléments de la liste
        command = input().split()
        # Si la commande est "0", on ajoute ou modifie la clé avec la nouvelle valeur
        if command[0] == "0":
            key = command[1]
            value = command[2]
            dict_data[key] = value
        # Si la commande est "1", on affiche la valeur correspondante à la clé si elle existe, sinon 0
        elif command[0] == "1":
            key = command[1]
            if key in dict_data:
                print(dict_data[key])
            else:
                print(0)
        # Si la commande est "2", on supprime la clé du dictionnaire si elle existe
        elif command[0] == "2":
            key = command[1]
            if key in dict_data:
                del dict_data[key]

# Appel de la fonction pour traiter les requêtes
process_queries()