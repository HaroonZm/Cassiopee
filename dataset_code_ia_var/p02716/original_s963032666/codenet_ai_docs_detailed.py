import sys

# Utilisation de la lecture rapide de l'entrée standard
input = sys.stdin.buffer.readline

def main():
    """
    Fonction principale qui calcule une certaine valeur optimale (probablement maximum de sous-séquences selon des règles particulières)
    d'après une séquence d'entiers, à l'aide d'une Programmation Dynamique personnalisée.

    Entrée : 
        Sur la première ligne, un entier N (taille de la séquence)
        Sur la deuxième ligne, N entiers séparés par des espaces

    Sortie :
        Affiche la valeur maximale calculée selon le problème posé (voir logique du dp).

    Note :
        Le tableau de DP dp[i][x][y] peut stocker à la fois des scores maximaux et des états booléens pour reconstituer la solution.
    """

    N = int(input())
    # Lecture de la séquence de N entiers
    a = list(map(int, input().split()))
    # Constante définissant une valeur initiale très basse (pour maximisation)
    INF = -10**15

    # Initialisation du tableau de programmation dynamique
    # dp[i] a deux états principaux dp[i][0] et dp[i][1], chacun contenant deux valeurs (score, flag/état)
    # - dp[i][0][0] : Meilleur score pour une configuration 1
    # - dp[i][0][1] : Meilleur score pour une configuration 2
    # - dp[i][1][0|1] : Booléens ou états permettant de retracer la décision
    dp = [[[INF, INF], [False, False]] for _ in range(N)]

    # Initialisation de l'état de base pour le premier élément
    dp[0][0][0] = 0               # Score de base sans rien prendre
    dp[0][0][1] = a[0]            # Prendre le premier élément
    dp[0][1][1] = True            # Configuration valide d'avoir choisi le premier élément

    if N > 1:
        dp[1][0][0] = 0           # Base: ne rien prendre jusqu'à 1
        # Si le deuxième est plus grand, le prendre, sinon rester au maximum
        if a[0] < a[1]:
            dp[1][0][1] = a[1]
            dp[1][1][1] = True
        else:
            dp[1][0][1] = a[0]

    # Boucle principale de la Programmation Dynamique
    for i in range(2, N):
        if i % 2 != 0:
            # Cas lorsque i est impair
            # Met à jour dp[i][0][0] par rapport à la valeur précédente
            dp[i][0][0] = dp[i-1][0][0]
            # Essayez d'améliorer dp[i][0][0] en prenant l'élément courant en plus du meilleur cas deux étapes avant
            if dp[i][0][0] < dp[i-2][0][0] + a[i]:
                dp[i][0][0] = dp[i-2][0][0] + a[i]
                dp[i][1][0] = True

            # Met à jour dp[i][0][1] à partir de la valeur précédente
            dp[i][0][1] = dp[i-1][0][1]
            # Teste une nouvelle prise, mais uniquement si le flag correspondant est False
            if dp[i-1][1][0] == False:
                if dp[i][0][1] < dp[i-1][0][0] + a[i]:
                    dp[i][0][1] = dp[i-1][0][0] + a[i]
                    dp[i][1][1] = True
            # Teste une amélioration qui saute une case
            if dp[i][0][1] < dp[i-2][0][1] + a[i]:
                dp[i][0][1] = dp[i-2][0][1] + a[i]
                dp[i][1][1] = True

        else:
            # Cas lorsque i est pair
            # Met à jour dp[i][0][0] à partir du chemin configuration 2
            dp[i][0][0] = dp[i-1][0][1]
            # Teste d'ajouter l'élément courant s'il n'a pas été déjà validé
            if dp[i-1][1][0] == False:
                if dp[i][0][0] < dp[i-1][0][0] + a[i]:
                    dp[i][0][0] = dp[i-1][0][0] + a[i]
                    dp[i][1][0] = True
            # Teste d'améliorer en sautant une case antérieure
            if dp[i][0][0] < dp[i-2][0][0] + a[i]:
                dp[i][0][0] = dp[i-2][0][0] + a[i]
                dp[i][1][0] = True
            # Met à jour la config 2 en sautant une case
            dp[i][0][1] = dp[i-2][0][1] + a[i]
            # Teste d'améliorer à partir du chemin précédent, seulement si le flag n'a pas encore été validé
            if dp[i-1][1][1] == False:
                if dp[i][0][1] < dp[i-1][0][1] + a[i]:
                    dp[i][0][1] = dp[i-1][0][1] + a[i]
            dp[i][1][1] = True

    # Affichage final selon la parité de N 
    # (si N est pair on imprime la config 2, sinon la config 1)
    if N % 2 == 0:
        print(dp[-1][0][1])
    else:
        print(dp[-1][0][0])

if __name__ == "__main__":
    main()