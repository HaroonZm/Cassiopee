import sys  # Importe le module 'sys' qui fournit l'accès à certaines variables et fonctions système

# Augmente la limite de récursion maximale autorisée dans Python à un million (10 puissance 6)
# Cela permet de gérer des appels récursifs profonds qui pourraient dépasser la limite par défaut (~1000)
sys.setrecursionlimit(10**6)

# Affecte à 'readline' la méthode 'sys.stdin.readline', utilisée pour lire une ligne de l'entrée standard (clavier ou redirection de fichier)
readline = sys.stdin.readline
# Affecte à 'read' la méthode 'sys.stdin.read', utilisée pour lire tout le flux de l'entrée standard en une seule chaîne de caractères
read = sys.stdin.read

# Lecture des entiers à partir de l'entrée standard et conversion en liste d'entiers
# La première valeur correspond à 'n', les suivantes forment la liste 'c'
n, *c = [int(i) for i in read().split()]
# Trie la liste 'c' dans l'ordre décroissant (du plus grand au plus petit)
c.sort(reverse=True)

# Définit une constante 'MOD' pour effectuer des opérations modulo 10^9+7, un grand nombre premier utilisé pour éviter les dépassements d'entiers
MOD = 10**9 + 7

# Initialise la variable 'ans' à 0. Cette variable va accumuler la somme finale selon une formule donnée
ans = 0

# Parcourt chaque élément de la liste 'c' ainsi que son indice correspondant
for i, ci in enumerate(c):
    # Pour chaque élément, calcule (indice+2) fois la valeur correspondante, puis applique le modulo MOD
    # Cette opération empêche la valeur de dépasser une certaine limite fixée par MOD et empêche les débordements d'entiers
    ans += (i + 2) * ci % MOD
    # Applique à nouveau le modulo après l'addition pour garantir que 'ans' reste dans la plage correcte
    ans %= MOD

# Calcule la puissance de 2 à l'exposant (2*n-2) modulo MOD avec la fonction intégrée 'pow' qui supporte le modulo en troisième argument
# Multiplie ce résultat par 'ans', applique le modulo à nouveau pour la dernière fois afin d'obtenir le résultat final
resultat = ans * pow(2, 2 * n - 2, MOD) % MOD

# Affiche le résultat sur la sortie standard (habituellement l'écran du terminal)
print(resultat)