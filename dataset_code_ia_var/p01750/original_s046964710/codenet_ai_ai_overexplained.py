import sys  # Importe le module sys pour interagir avec les flux d'entrée et de sortie standard

# On définit des alias pour plus de rapidité et de clarté
readline = sys.stdin.readline  # 'readline' devient une référence à la méthode d'entrée standard
write = sys.stdout.write      # 'write' devient une référence à la méthode de sortie standard

# On définit une fonction appelée solve qui contiendra toute notre logique principale
def solve():
    MOD = 10**9 + 7  # On définit une grande constante pour faire des opérations modulo, très courante en programmation compétitive

    # On lit un entier D à partir de l'entrée standard, ce sera probablement le nombre de portes ou de dimensions, selon le problème
    D = int(readline())  # 'int' convertit la chaîne lue en nombre entier

    # On construit une liste L contenant D entiers, chacun lu individuellement
    # 'for i in range(D)' va itérer D fois (i va de 0 à D-1)
    L = [int(readline()) for i in range(D)]  # Ceci est une compréhension de liste, chaque 'int(readline())' lit un entier

    # On lit un autre entier S à partir de l'entrée standard
    S = int(readline())

    # On initialise une liste appelée 'dp' (abréviation de 'dynamic programming'), de taille S+1, remplie de 0s
    # Cette liste va servir à mémoriser certaines valeurs intermédiaires pour éviter des recalculs inutiles
    dp = [0] * (S + 1) 

    # On définit une condition initiale : le nombre de façons d'atteindre la somme S est 1
    dp[S] = 1

    # Cette première boucle va itérer sur chacun des D éléments
    for i in range(D):
        # L'élément courant de la liste L, qui pourrait représenter une longueur, un poids, etc.
        l = L[i]
        # Pour chaque valeur de i allant de l à S inclus (c'est-à-dire du pas 'l' jusqu'à 'S')
        # Note importante : on va manipuler le tableau 'dp' à l'envers pour ne pas interférer avec les valeurs courantes
        for i in range(l, S + 1):
            # On retire de dp[i-l] la valeur de dp[i]. Cela permet de mettre à jour les façons d'obtenir la somme i-l
            dp[i - l] -= dp[i]

    # On initialise la variable qui contiendra la réponse finale
    ans = 0

    # On parcourt chaque indice de 0 à S (inclus)
    for i in range(S + 1):
        # On calcule (i puissance D) modulo MOD, et on le multiplie par dp[i]
        # pow(x, y, z) calcule (x^y) % z de façon efficace
        # On ajoute cette quantité à notre réponse finale
        ans += pow(i, D, MOD) * dp[i]

    # On s'assure que la réponse finale est bien dans l'intervalle [0, MOD-1]
    ans %= MOD

    # On affiche le résultat avec un saut de ligne, en formatant l'entier sous forme de chaîne de caractères
    write("%d\n" % ans)

# On appelle la fonction solve ici afin d'exécuter le programme quand ce script est lancé
solve()