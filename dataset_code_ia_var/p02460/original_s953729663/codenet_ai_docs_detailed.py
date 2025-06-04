def process_commands():
    """
    Gère une séquence de commandes sur un dictionnaire en utilisant l'entrée standard.
    Les commandes peuvent être :
    - "0 key value" : Ajoute ou met à jour la clé 'key' avec la valeur entière 'value' dans le dictionnaire.
    - "1 key"      : Affiche la valeur associée à la clé 'key'. Affiche 0 si la clé n'existe pas.
    - Autre        : Supprime la clé 'key' du dictionnaire si elle existe.
    """

    # Lecture du nombre de commandes à traiter
    q = int(input())
    # Initialisation d'un dictionnaire vide pour stocker les paires clé-valeur
    dct = {}

    # Boucle sur chacune des q commandes
    for _ in range(q):
        # Lecture et séparation de la commande en liste de chaînes
        cmmd = input().split()
        # Si la première partie de la commande est "0", on ajoute ou remplace la clé
        if cmmd[0] == "0":
            # Affectation de la valeur entière à la clé spécifiée
            dct[cmmd[1]] = int(cmmd[2])
        # Si la commande est "1 key", on affiche la valeur ou 0 si la clé n'existe pas
        elif cmmd[0] == "1":
            try:
                # Affiche la valeur associée à la clé
                print(dct[cmmd[1]])
            except KeyError:
                # Si la clé n'existe pas, affiche 0
                print(0)
        # Toute autre commande est interprétée comme une suppression de la clé
        else:
            try:
                # Suppression de la clé du dictionnaire
                del dct[cmmd[1]]
            except KeyError:
                # Si la clé n'existe pas, ne rien faire
                pass

# Appel principal de la fonction si ce fichier est exécuté directement
if __name__ == "__main__":
    process_commands()