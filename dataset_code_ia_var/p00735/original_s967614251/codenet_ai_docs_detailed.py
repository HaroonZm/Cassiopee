def generate_candidate_list(limit):
    """
    Génère une liste de candidats S2 et un tableau indicateur S jusqu'à une limite donnée.
    
    Les éléments de S2 sont des entiers de la forme 7*i +/- 1 qui ne sont pas marqués comme -1
    dans le tableau S (c'est-à-dire qui n'ont pas été éliminés comme multiples d'autres candidats).

    Args:
        limit (int): La borne supérieure pour générer les candidats.

    Returns:
        tuple: Un tableau indicateur S et une liste de candidats S2.
    """
    # Tableau indiquant si un nombre a été éliminé (valeur -1) ou non (valeur 0)
    S = [0 for _ in range(limit)]
    # Liste des candidats valides correspondant à la condition donnée
    S2 = []
    # Liste des valeurs à ajouter ou soustraire à 7*i
    A = [-1, 1]
    
    # On parcourt les multiples de 7 pour générer les candidats possibles
    for i in range(1, limit // 7 + 1):
        d = 7 * i
        for a in A:
            da = d + a
            # On vérifie que da est dans la limite et qu'il n'a pas déjà été éliminé
            if da < limit and S[da] == 0:
                S2.append(da)  # On ajoute le candidat à la liste S2
                # On élimine les multiples de da en les marquant dans S
                for j in range(2, limit // 2):
                    if da * j >= limit:
                        break
                    S[da * j] = -1
    return S, S2


def afficher_diviseurs_candidats(n, S2):
    """
    Affiche tous les éléments de S2 qui sont des diviseurs de n et qui sont ≤ n.
    Le résultat est affiché sous la forme "n: div1 div2 ...".

    Args:
        n (int): Le nombre pour lequel chercher les diviseurs dans S2.
        S2 (list): Liste des candidats pour la division.
    """
    # Recherche tous les candidats de S2 qui divisent n et qui ne dépassent pas n
    diviseurs = [str(x) for x in S2 if n % x == 0 and x <= n]
    print(f"{n}:", ' '.join(diviseurs))


def boucle_interactive(S2):
    """
    Boucle interactive pour permettre à l'utilisateur de saisir des entiers n,
    puis d'afficher pour chacun la liste des candidats de S2 qui sont des diviseurs de n.
    La boucle s'arrête si l'utilisateur saisit 1.

    Args:
        S2 (list): La liste des candidats générés à utiliser pour le test de divisibilité.
    """
    while True:
        # Lecture d'un entier depuis l'entrée utilisateur
        n = int(input())
        if n == 1:
            # Fin de la boucle si l'utilisateur saisit 1
            break
        afficher_diviseurs_candidats(n, S2)


def main():
    """
    Fonction principale qui initialise les structures de données
    puis lance la boucle interactive pour l'affichage des diviseurs.
    """
    # Définition de la limite supérieure pour le calcul des candidats et du tableau S
    LIMIT = 300000
    # Génération des listes S et S2
    S, S2 = generate_candidate_list(LIMIT)
    # Démarrage de la boucle interactive avec la liste de candidats S2
    boucle_interactive(S2)


if __name__ == "__main__":
    main()