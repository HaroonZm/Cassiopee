def process_commands():
    """
    Gère une série de commandes pour manipuler un dictionnaire en fonction des entrées utilisateur.
    
    Les commandes suivent le format suivant :
      - '0 key value' : Ajoute la paire clé-valeur au dictionnaire (avec la valeur convertie en entier).
      - '1 key'      : Affiche la valeur associée à la clé si elle existe, sinon affiche 0.
      - 'autre key'  : Supprime la clé du dictionnaire si elle existe (toute commande autre que '0' ou '1').
    """

    # Demande à l'utilisateur combien de commandes il souhaite saisir
    n = int(input())
    dic = {}  # Initialise un dictionnaire vide pour stocker les paires clé-valeur

    for i in range(n):
        # Récupère la commande et ses arguments depuis l'entrée standard
        q, *args = map(str, input().split())

        # Gère la clé : args[0] doit contenir la clé à manipuler
        key = args[0]

        # Si la commande est '0', ajoute ou met à jour la clé avec la valeur donnée
        if q == "0":
            val = int(args[1])  # La valeur (argument 2) est convertie en int
            dic[key] = val      # Ajoute ou met à jour la paire clé-valeur dans le dictionnaire

        # Si la commande est '1', affiche la valeur associée à la clé, ou 0 si absente
        elif q == "1":
            if key in dic.keys():
                print(dic[key])  # Affiche la valeur si la clé existe
            else:
                print(0)         # Affiche 0 si la clé n'existe pas

        # Toute autre commande supprime la clé si elle existe
        else:
            if key in dic:
                dic.pop(key)     # Supprime la clé du dictionnaire si elle existe
            else:
                pass             # Sinon, ne fait rien

# Démarre le traitement des commandes lorsque le script est exécuté
process_commands()