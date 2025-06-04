def play_game(n, p):
    """
    Simule le jeu décrit dans le problème :
    – n : nombre de joueurs
    – p : nombre de pierres initiales dans Wan
    La fonction affiche l'indice du joueur qui gagne selon les règles.
    """
    # Initialisation de la liste kouho, qui stocke le nombre de pierres pour chaque joueur.
    kouho = [0] * n
    # Initialisation du nombre de pierres dans la réserve "wan"
    wan = p

    while True:
        # Cette variable booléenne permet de sortir de la boucle une fois le gagnant trouvé
        end = False
        # Itération sur chaque joueur à tour de rôle
        for i in range(n):
            # Si la réserve wan n'est pas vide, on donne une pierre au joueur courant
            if wan > 0:
                kouho[i] += 1
                wan -= 1
                # Vérifie la condition de victoire :
                # Si la réserve est vide ET que le joueur courant possède toutes les pierres
                if wan == 0 and kouho[i] == p:
                    print(i)  # Afficher l'indice du joueur vainqueur
                    end = True  # Déclarer la fin de la partie
                    break
            else:
                # Si la réserve est vide et que le joueur n'a pas gagné,
                # récupérer toutes les pierres du joueur courant et les remettre dans la réserve
                wan += kouho[i]
                kouho[i] = 0
        # Si un gagnant a été trouvé, sortir de la boucle principale
        if end:
            break

def main():
    """
    Fonction principale qui gère l'entrée utilisateur
    et exécute le jeu jusqu'à réception des conditions d'arrêt (0 0).
    """
    while True:
        # Lire l'entrée utilisateur, qui contient n et p
        n, p = map(int, input().split())
        # Si n et p sont tous les deux nuls, arrêter le programme
        if n == 0 and p == 0:
            break
        # Lancer une partie avec les paramètres lus
        play_game(n, p)

# Point d'entrée du script
if __name__ == "__main__":
    main()