# Demander à l'utilisateur de saisir un entier, qui sera stocké dans la variable N
# Cette valeur représente généralement le nombre d'éléments dans un tableau ou une liste
N = int(input())

# Demander à l'utilisateur de saisir une ligne de N entiers séparés par des espaces
# La fonction input() renvoie une chaîne de caractères que l'on découpe en morceaux avec split()
# map(int, ...) transforme chaque morceau de chaîne en entier
# Enfin, on transforme le résultat de map en une liste d'entiers avec list()
C = list(map(int, input().split()))

# Définir une constante MOD à 1_000_000_007 (un milliard sept)
# Ce nombre premier est couramment utilisé pour éviter les débordements lors de
# grands calculs dans des problèmes algorithmiques, en gardant les résultats dans un intervalle raisonnable
MOD = 1_000_000_007

# Préparer une liste B qui contiendra les puissances de 2 modulo MOD
# Cette liste aura une taille de N+1, suffisamment grande pour contenir de B[0] à B[N]
# On initialise tous les éléments de B à 0 en utilisant une compréhension de liste
B = [0 for _ in range(N+1)]

# La première puissance de 2 (2^0) est toujours 1, donc on initialise B[0] à 1
B[0] = 1

# Cette boucle calcule les puissances de 2 de 1 à N inclus
# Pour chaque i de 1 à N, on calcule B[i] comme étant B[i-1] multiplié par 2
# Ensuite, on prend le résultat modulo MOD pour garder la valeur dans l'intervalle [0, MOD-1]
for i in range(1, N+1):
    B[i] = B[i-1] * 2
    # Le symbole %= est une forme abrégée pour B[i] = B[i] % MOD
    B[i] %= MOD

# On trie la liste C par ordre croissant avec la méthode sort()
# Cela facilite certains calculs ultérieurs où l'ordre des éléments est important
C.sort()

# Initialiser la variable ans à 0, qui contiendra le résultat final
ans = 0

# Parcourir tous les entiers n de 1 à N inclus (attention à l'indice, car les listes commencent à 0 en Python)
for n in range(1, N+1):
    # Pour chaque élément, on effectue un calcul complexe basé sur la tâche algorithmique
    # Il s'agit d'une somme pondérée par des puissances de 2, adaptée à la position de l'élément C[n-1]
    # Explication du calcul pour chaque terme :
    # - C[n-1] : on récupère le (n-1)-ème élément car C est indexée à partir de 0
    # - (N-n) : représente le nombre d'éléments "restants" après la position n
    # - B[N-n-1] et B[N-n] : puissances de 2 spécifiques selon la position
    # - B[n-1] : puissance de 2 selon le début du tableau
    # - Chaque terme est multiplié et la somme est accumulée dans ans
    ans += C[n-1] * ((N-n) * B[N-n-1] + B[N-n]) * B[n-1]
    # On prend aussi le résultat modulo MOD à chaque itération pour éviter le débordement
    ans %= MOD

# On multiplie ans par B[N] (c'est-à-dire 2 puissance N modulo MOD)
# Cela correspond souvent à une normalisation ou à une répartition sur tous les sous-ensembles possibles d'une liste de taille N
ans *= B[N]
# Encore une fois, on applique le modulo pour sécuriser la valeur finale
ans %= MOD

# Afficher la réponse finale à l'utilisateur avec la fonction print()
print(ans)

# -----------------------------------------------------
# Partie commentée (à titre d'explication ou de tentative alternative)
"""
# Initialiser une liste D de taille N pour stocker la somme cumulée des éléments de C
# D[0] sera simplement le premier élément de C
D = [0 for _ in range(N)] #累積和

# Initialisation de la première valeur de D
D[0] = C[0]

# Boucle de 1 à N-1 pour calculer à chaque fois la somme cumulée jusqu'à la position actuelle
for i in range(1, N):
    D[i] = D[i-1] + C[i]

# Afficher la liste triée C (à des fins de vérification ou de débogage)
print(C)

# Initialisation de la variable ans à 0 pour une nouvelle somme (éventuellement pour une approche alternative)
ans = 0

# Boucle sur j de 1 à N inclus pour accumuler des produits de la forme D[j-1] * B[j-1]
for j in range(1, N+1):
    ans += D[j-1] * B[j-1]
    print(D[j-1] * B[j-1])
"""
# Fin du code avec explications détaillées