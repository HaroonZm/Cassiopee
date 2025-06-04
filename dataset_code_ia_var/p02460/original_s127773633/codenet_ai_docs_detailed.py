def process_commands(commands):
    """
    Traite une liste de commandes pour effectuer des opérations sur un dictionnaire.
    
    Chaque commande est une liste contenant des chaînes:
    - '0 key value' : Ajoute ou met à jour la clé avec la valeur donnée.
    - '1 key'      : Affiche la valeur associée à la clé, ou '0' si elle n'existe pas.
    - '2 key'      : Supprime la clé du dictionnaire si elle existe.
    
    Args:
        commands (list of list of str): Liste où chaque élément est une liste de chaînes correspondant à une commande.
    Returns:
        None
    """
    data = {}  # Dictionnaire pour stocker les paires clé/valeur.

    for cmd in commands:
        # Si la commande est '0', on ajoute ou met à jour une entrée dans le dictionnaire.
        if cmd[0] == "0":
            data[cmd[1]] = cmd[2]
        # Si la commande est '1', on affiche la valeur si la clé existe, sinon '0'.
        elif cmd[0] == "1":
            if cmd[1] in data:
                print(data[cmd[1]])
            else:
                print("0")
        # Si la commande est autre (ici '2'), on supprime la clé si elle existe dans le dictionnaire.
        else:
            if cmd[1] in data:
                del data[cmd[1]]

def main():
    """
    Point d'entrée du programme. Lit les entrées utilisateur, prépare la liste de commandes,
    puis appelle la fonction de traitement des commandes.
    
    L'utilisateur est d'abord invité à saisir le nombre de commandes,
    puis chaque commande sur une nouvelle ligne.
    """
    n = int(input())  # Nombre de commandes à traiter
    commands = []

    # Récupération de toutes les commandes fournies par l'utilisateur.
    for _ in range(n):
        line = input()
        cmd = line.split()  # Découpe la ligne d'entrée en liste de chaînes
        commands.append(cmd)
    
    # Appel de la fonction principal de traitement avec la liste récupérée.
    process_commands(commands)

if __name__ == '__main__':
    main()