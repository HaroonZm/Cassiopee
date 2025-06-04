def main():
    """
    Fonction principale qui lit les paramètres N et M, puis exécute M commandes sur une table.
    La table est une liste de N listes, chacune pouvant recevoir des entiers.
    Deux types de commandes :
      - Ajouter un entier à la sous-liste la moins remplie.
      - Retirer et afficher le premier élément de la sous-liste numéro 'num'.
    """
    # Lecture des entiers N (nombre de sous-listes) et M (nombre de commandes)
    N, M = [int(i) for i in input().split()]

    # Initialisation de la table : une liste de N listes vides
    table = [[] for _ in range(N)]

    # Traitement des M commandes
    for _ in range(M):
        # Lecture de la commande et du nombre associé
        command, num = [int(i) for i in input().split()]

        if command == 0:
            # Commande 0 : retirer et afficher le premier élément de la sous-liste numéro 'num'
            # On retire l'élément à l'indice 0 de la sous-liste d'indice num-1 (décalage car indices commencent à 0)
            print(table[num - 1].pop(0))
        else:
            # Commande 1 : ajouter 'num' à la sous-liste la moins remplie
            # On recherche la sous-liste ayant la taille minimale
            min_size = float('inf')
            min_id = -1
            for i in range(N):
                if len(table[i]) < min_size:
                    min_size = len(table[i])
                    min_id = i
            # Ajout de 'num' à la sous-liste trouvée
            table[min_id].append(num)

if __name__ == "__main__":
    main()