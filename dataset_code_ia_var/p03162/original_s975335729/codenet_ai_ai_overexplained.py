import sys  # Importe le module sys, qui fournit diverses fonctionnalités liées au système d'exploitation, comme accéder à stdin (entrée standard)

input = sys.stdin.readline  # Définit 'input' comme un alias pour sys.stdin.readline, qui lit une ligne complète à partir de l'entrée standard (ex: input clavier ou fichier redirigé)

def main():
    # Lit le premier entier qui représente le nombre de jours ou d'étapes (selon le contexte du problème)
    N = int(input())  # Appelle la fonction 'input' pour obtenir une ligne, puis la convertit en entier avec int()
    
    # Crée une liste 'h' contenant N sous-listes, chacune de 3 entiers, récupérés sur N lignes d'entrée
    # Utilise une compréhension de liste pour répéter l'opération N fois
    h = [ list(map(int, input().split())) for _ in range(N) ]
    # - 'input().split()' : lit une ligne puis coupe selon les espaces pour produire une liste de chaînes
    # - 'map(int, ...)' : applique la conversion en entier à chaque chaîne de la liste
    # - 'list(...)' : transforme le résultat du map en liste
    # - La compréhension de liste répète ça N fois, donc h sera une liste de listes, structure 2D

    # Crée une table (liste de listes) 'dp' pour la programmation dynamique, initialisée à 0
    # dp[i][j] représente le score maximal jusqu'au jour i si l'action 'j' est choisie pour le jour i
    dp = [ [0] * 3 for _ in range(N) ]  # Pour chaque jour crée une liste de 3 zéros (une pour chaque action possible)

    # Initialise le premier jour : le score maximum si on choisit chaque action (0,1,2) le premier jour est simplement h[0][i]
    for i in range(3):
        dp[0][i] = h[0][i]  # On ne peut rien accumuler avant le premier jour, donc on prend la valeur directement

    # Remplit la table dp pour chaque jour à partir du deuxième jour
    for i in range(1, N):  # Pour chaque jour de 1 à N-1 (le 0 a déjà été fait)
        for k in range(3):  # Pour chaque action possible ce jour
            # On ne peut pas faire la même action que la veille, donc on considère les deux autres actions précédentes
            # (k+1)%3 et (k+2)%3 donnent les deux autres actions de manière cyclique (0,1,2)
            # On prend le maximum des deux possibilités d'accumulation
            dp[i][k] = max(
                dp[i-1][(k+1)%3] + h[i][k],  # On choisit la première autre action le jour d'avant
                dp[i-1][(k+2)%3] + h[i][k]   # On choisit la seconde autre action le jour d'avant
            )
            # Ainsi, on choisit la meilleure option qui respecte la contrainte

    # Affiche le score maximal possible sur tous les jours, en considérant toutes les actions le dernier jour
    print(max(dp[N-1]))  # On prend le maximum parmi les 3 actions possibles le dernier jour (dp[N-1])

# Ceci permet de ne lancer la fonction main que si le script est exécuté directement, pas importé comme module
if __name__ == "__main__":
    main()  # Appelle la fonction principale pour démarrer le programme