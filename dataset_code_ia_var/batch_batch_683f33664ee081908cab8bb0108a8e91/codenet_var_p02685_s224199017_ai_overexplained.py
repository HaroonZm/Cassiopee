def main():
    # Définition de la constante N qui servira de taille maximale des tableaux de factorielle
    N = 200002  # N est fixé à 200002 car on doit pouvoir calculer toutes les combinaisons jusqu'à ce nombre.
    # Définition de la constante MOD qui servira à prendre les résultats des opérations modulo MOD,
    # ce qui évite le dépassement de capacité et est courant dans les problèmes de combinatoire modulaire.
    MOD = 998244353  # Ce nombre est un grand nombre premier, souvent utilisé en programmation compétitive.

    # Lecture de trois entiers à partir de l'entrée standard. La fonction input() lit une ligne depuis l'entrée.
    # split() sépare la chaîne en sous-chaînes selon les espaces.
    # map(int, ...) convertit chaque sous-chaîne en entier.
    # n, m, k sont donc trois entiers extraits de cette ligne.
    n, m, k = map(int, input().split())

    # Initialisation de deux listes :
    # fact sert à stocker les factorielles (n!) pour tous n jusqu'à N-1
    # finv sert à stocker les inverses multiplicatifs des factorielles (fact[n]^(-1) modulo MOD)
    # On les initialise avec des 1 par défaut.
    fact = [1] * N  # Liste de taille N, initialisée avec des 1
    finv = [1] * N  # Même chose pour les inverses

    # Calcul des factorielles modulo MOD pour tous les i de 1 à N-1
    for i in range(1, N):
        # La factorielle de i est la factorielle de (i-1) multipliée par i
        # On prend le résultat modulo MOD à chaque étape pour éviter les dépassements
        fact[i] = fact[i - 1] * i % MOD

    # Calcul de l'inverse multiplicatif de la factorielle la plus grande (fact[N-1])
    # Ceci utilise le petit théorème de Fermat car MOD est premier.
    # pow(a, b, c) calcule (a**b)%c efficacement même pour de grands nombres.
    finv[N - 1] = pow(fact[N - 1], MOD - 2, MOD)

    # Calcul des inverses multiplicatifs des factorielles pour tous les i de N-2 à 0 dans l'ordre décroissant
    for i in range(N - 2, -1, -1):
        # L'inverse de fact[i] se calcule à partir de l'inverse de fact[i+1]
        # Multiplié par (i+1) car fact[i+1] = fact[i] * (i+1)
        # On garde tout modulo MOD
        finv[i] = finv[i + 1] * (i + 1) % MOD

    # Définition d'une fonction de calcul du coefficient binomial "n choose r"
    # C(n, r) représente le nombre de façons de choisir r éléments parmi n (combinaison)
    def C(n, r):
        # Le coefficient binomial C(n, r) se calcule par n!/(r!*(n-r)!)
        # Ici, on utilise les tables pré-calculées pour un calcul rapide sous modulo
        # La multiplication des inverses simule une division sous modulo premier.
        return fact[n] * finv[r] * finv[n - r] % MOD

    # Initialisation de la réponse : on élève m à la puissance n, puis on prend le résultat modulo MOD
    # Cela représente toutes les possibilités avant prise en compte de contraintes supplémentaires.
    ans = pow(m, n, MOD)

    # Boucle pour corriger la réponse de base en soustrayant certaines configurations
    # La boucle va de r = 1 à r = n - k - 1 inclus (car range s'arrête avant le second argument)
    for r in range(1, n - k):
        # Pour chaque r de cet intervalle, on doit retrancher un certain nombre de configurations
        # Ces configurations sont calculées à l'aide du coefficient binomial, d'une puissance de m,
        # et d'une puissance de (m-1), le tout multiplié et pris modulo MOD
        soustraction = C(n - 1, r - 1) * m * pow(m - 1, r - 1, MOD)
        # On soustrait ce terme à la réponse actuelle, tout en assurant le modulo MOD pour rester dans les bornes
        ans -= soustraction
        # Pour s'assurer que ans reste dans l'intervalle [0, MOD-1], on applique le modulo après chaque soustraction
        ans %= MOD  # Cela corrige aussi le cas où ans deviendrait négatif

    # Affichage final du résultat : print() envoie la valeur de ans à la sortie standard
    print(ans)

# Appel de la fonction principale : c'est le point d'entrée du programme
main()