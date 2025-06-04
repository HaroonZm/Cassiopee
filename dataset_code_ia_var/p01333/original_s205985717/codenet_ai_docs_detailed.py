import sys

def solve():
    """
    Boucle principale qui lit des paires de valeurs depuis l'entrée standard et calcule,
    pour chaque paire, une décomposition en billets.

    Tant que l'utilisateur ne saisit pas '0 0', la fonction continue de traiter les entrées.
    Pour chaque entrée, on considère deux entiers v (valeur à payer) et m (montant payé).
    On calcule la différence m - v, puis on décompose cette différence en billets
    de 1000, 500 et 100 unités. Enfin, on affiche le nombre de chaque type de billet.
    """
    while True:
        # Lecture de la ligne d'entrée, séparation des valeurs et conversion en int.
        try:
            v, m = map(int, raw_input().split())
        except EOFError:
            # Si la fin de l'entrée est atteinte, arrêter la boucle
            break

        # Condition d'arrêt lorsque les deux valeurs sont 0
        if v == 0 and m == 0:
            return

        # Initialisation des compteurs pour chaque type de billet
        r1, r5, r10 = 0, 0, 0

        # Calcul du montant à rendre
        re = m - v

        # Calcul du nombre de billets de 1000
        r10 = re // 1000
        # Mise à jour du reste après avoir retiré les billets de 1000
        re %= 1000

        # Calcul du nombre de billets de 500
        r5 = re // 500
        # Mise à jour du reste après avoir retiré les billets de 500
        re %= 500

        # Calcul du nombre de billets de 100
        r1 = re // 100

        # Affichage du résultat sous la forme "nb_100 nb_500 nb_1000"
        print(str(r1) + " " + str(r5) + " " + str(r10))

if __name__ == "__main__":
    # Lancement de la fonction principale si ce fichier est exécuté comme script principal
    solve()