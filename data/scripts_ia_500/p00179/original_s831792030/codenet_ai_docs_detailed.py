rgb = set(["r", "g", "b"])

def process_worms():
    """
    Lit des chaînes représentant des vers colorés, puis pour chaque ver,
    cherche le nombre minimal de transformations nécessaires pour obtenir
    un ver dont toutes les lettres sont identiques.

    La transformation consiste à remplacer deux lettres adjacentes différentes
    par deux lettres d'une couleur distincte.

    La fonction affiche pour chaque ver le nombre minimal de transformations
    nécessaires, ou "NA" si ce n'est pas possible en au plus 15 transformations.

    Arrêt de la lecture lorsque l'entrée est "0".
    """
    while True:
        worm = raw_input()  # Lecture de la chaîne entrée par l'utilisateur
        if worm == "0":  # Condition d'arrêt de la boucle principale
            break

        n = len(worm)  # Longueur du ver initial
        que = [worm]  # File pour le parcours en largeur (BFS) des transformations
        ref = set(worm)  # Ensemble pour mémoriser les configurations déjà vues
        L = 1  # Nombre d'éléments actuels dans la file
        cnt = 0  # Compteur du nombre de transformations effectuées
        flag = 0  # Indicateur pour savoir si la condition finale est atteinte

        while True:
            # Parcours des éléments actuels dans la file
            for r in range(L):
                Worm = que.pop(0)  # Récupération du premier élément de la file

                # Si cette configuration a déjà été traitée, on l'ignore
                if Worm in ref:
                    continue
                else:
                    ref.add(Worm)  # Marquer cette configuration comme traitée

                # Vérifier si toutes les lettres sont identiques
                if len(set(Worm)) == 1:
                    flag = 1  # Condition finale atteinte
                    break

                # Parcourir toutes les paires adjacentes de lettres différentes
                for i in range(n - 1):
                    if Worm[i] != Worm[i + 1]:
                        # Créer une nouvelle configuration après transformation
                        worm_copy = Worm[:]
                        # Trouver la couleur différente qui n'est pas dans la paire adjacente
                        nextclr = list(rgb - set(worm_copy[i:i + 2]))[0]
                        # Remplacer les deux lettres adjacentes par deux lettres de nextclr
                        worm_copy = worm_copy[:i] + 2 * nextclr + worm_copy[i + 2:]
                        # Ajouter la nouvelle configuration à la file si elle n'y est pas déjà
                        if worm_copy not in que:
                            que.append(worm_copy)

            L = len(que)  # Mettre à jour la taille de la file pour la prochaine itération

            # Arrêt si condition finale trouvée ou plus d'éléments à traiter
            if flag or L == 0:
                break

            cnt += 1  # Incrémenter le compteur de transformations

            # Limiter la recherche à 15 transformations pour éviter le calcul infini
            if cnt > 15:
                break

        # Afficher le résultat : nombre de transformations ou 'NA' si impossible
        print cnt if flag else "NA"


# Exécution de la fonction principale
process_worms()