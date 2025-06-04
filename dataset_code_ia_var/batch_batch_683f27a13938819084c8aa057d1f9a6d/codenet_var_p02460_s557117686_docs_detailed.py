def process_commands():
    """
    Lit un nombre d'opérations depuis l'entrée utilisateur, puis traite chaque opération pour modifier ou interroger un dictionnaire.
    Les opérations sont :
        - "0 key value" : attribue la valeur 'value' à la clé 'key' dans le dictionnaire.
        - "2 key"      : attribue la valeur 0 à la clé 'key' dans le dictionnaire.
        - "1 key"      : affiche la valeur associée à la clé 'key', ou affiche 0 si la clé n'existe pas.
    """
    d = {}  # Dictionnaire utilisé pour stocker les paires clé-valeur.
    n = int(input())  # Nombre total d'opérations à lire.

    # Parcours de chaque opération fournie par l'utilisateur.
    for _ in range(n):
        a = input().split()  # Lecture et découpage de la ligne d'entrée en liste
        x = a[1]             # 'x' représente toujours la clé sur laquelle opérer
        y = a[0]             # 'y' représente le type d'opération (0, 1 ou 2)

        if y == "0":
            # Opération d'affectation d'une nouvelle valeur à une clé.
            # Format de la commande : "0 key value"
            d[x] = a[2]
        elif y == "2":
            # Opération qui affecte la valeur 0 à une clé.
            # Format de la commande : "2 key"
            d[x] = 0
        else:
            # Opération d'interrogation de la valeur associée à la clé.
            # Format de la commande : "1 key"
            # Si la clé n'existe pas, afficher 0
            print(d[x] if x in d else 0)

# Lancement de la fonction principale si ce fichier est exécuté comme script principal
if __name__ == "__main__":
    process_commands()