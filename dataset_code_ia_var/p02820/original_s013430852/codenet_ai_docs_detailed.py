def run(N, K, R, S, P, T):
    """
    Calcule le score maximal dans un jeu type pierre-papier-ciseaux avec des restrictions d'usage des coups.

    Args:
        N (int): Nombre de parties dans le jeu.
        K (int): Nombre d'intervalles d'interdiction, c'est-à-dire on ne peut pas répéter le même coup toutes les K parties.
        R (int): Points gagnés en jouant 'pierre' (contre 'ciseaux').
        S (int): Points gagnés en jouant 'ciseaux' (contre 'papier').
        P (int): Points gagnés en jouant 'papier' (contre 'pierre').
        T (str): Chaîne de caractères de longueur N représentant les coups de l'adversaire pour chaque tour.
                 Les caractères possibles sont 'r' (pierre), 's' (ciseaux), 'p' (papier).

    Returns:
        int: Le score maximal pouvant être obtenu en respectant les contraintes.
    """

    ans = 0     # Variable pour stocker le score total accumulé.
    main = ''   # Chaîne utilisée pour mémoriser les coups déjà joués par le joueur (pour l'interdiction de répétition).

    # Parcourt chaque tour du jeu
    for i in range(len(T)):
        t = T[i]   # Coup de l'adversaire à ce tour

        if i < K:
            # Pour les K premiers tours, comme il n'y a pas de coup précédent à vérifier, on joue le meilleur coup.
            if t == 'r':
                # L'adversaire joue 'pierre', donc on joue 'papier' (gagne P points).
                ans += P
                main += 'p'
            elif t == 's':
                # L'adversaire joue 'ciseaux', donc on joue 'pierre' (gagne R points).
                ans += R
                main += 'r'
            elif t == 'p':
                # L'adversaire joue 'papier', donc on joue 'ciseaux' (gagne S points).
                ans += S
                main += 's'
        else:
            # À partir du (K+1)ème tour, vérifier si on a déjà joué le même coup K tours avant.
            pre_t = main[i - K]  # Coup joué il y a K tours

            # On joue normalement le meilleur coup, sauf si c'est le même que celui joué il y a K tours.
            if t == 'r' and pre_t != 'p':
                ans += P
                main += 'p'
            elif t == 's' and pre_t != 'r':
                ans += R
                main += 'r'
            elif t == 'p' and pre_t != 's':
                ans += S
                main += 's'
            else:
                # Si le coup optimal a déjà été joué il y a K tours, on ne peut pas le rejouer.
                # On choisit de ne rien faire ce tour, représenté par un espace.
                main += ' '
    return ans

def main():
    """
    Fonction principale chargée de la saisie des paramètres et de l'affichage du score maximal.
    Lit les entrées standard au format spécifié, appelle la fonction run et affiche la sortie.
    """
    # Lecture des paramètres N (nombre de tours) et K (intervalles d'interdiction)
    N, K = map(int, input().split())
    # Lecture des scores correspondant aux coups 'pierre', 'ciseaux', 'papier'
    R, S, P = map(int, input().split())
    # Lecture du coup de l'adversaire sous forme de chaîne de caractères
    T = input()
    # Calcule et affiche le score maximal
    print(run(N, K, R, S, P, T))

if __name__ == '__main__':
    # Point d'entrée du script : appelle la fonction principale
    main()