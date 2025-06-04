# Prendre deux entiers en entrée séparés par un espace, puis les convertir en entiers grâce à map(). L'utilisateur saisit la valeur de n et m, que l'on utilise dans la suite du programme.
n, m = map(int, input().split(' '))  # Par exemple, si on entre "10 3", alors n=10, m=3

# Définir une constante entière Mod valant 10**9 + 7, utilisée pour tous les calculs modulo afin d'éviter des débordements d'entiers et pour respecter les contraintes des problèmes courants.
Mod = 1000000007

# Calculer la racine carrée de n avec l'opérateur d'exponentiation '**' et 0.5. 
# Prendre la partie entière en utilisant int(), puis ajouter 1. 
# Ce spl correspond à la borne supérieure pour une division, utilisée dans la construction suivante.
spl = int(n ** 0.5) + 1

# On construit une liste f en deux étapes :
# 1. Créer une liste contenant les entiers de 0 à spl-1 (inclus). 
# 2. Créer une autre liste contenant, pour chaque i de 1 à spl-1, le résultat de la division entière n//i. 
#    Ensuite, on inverse cette deuxième liste avec [::-1] (c'est pourquoi ça se termine par les plus petits quotients).
# 3. On concatène les deux listes pour obtenir la liste f.
first_part = [i for i in range(spl)]  # Liste contenant [0, 1, ..., spl-1]
second_part = [n // i for i in range(1, spl)]  # Liste contenant les quotients n//i pour i de 1 à spl-1
second_part_reversed = second_part[::-1]  # Inverser la liste pour une utilisation ultérieure
f = first_part + second_part_reversed  # On concatène les listes pour obtenir la liste finale f

# Calculer la longueur de la liste f et la stocker dans k.
# C'est égal à 2*spl-1 car first_part fait spl éléments et second_part fait spl-1 éléments. 
k = 2 * spl - 1

# Initialiser une liste 'dp' de taille k.
# La liste 'dp' commence par un 0 suivi de (k-1) fois la valeur 1.
# C'est-à-dire, dp[0]=0 et dp[1]=dp[2]=...=dp[k-1]=1.
dp = [0] + [1] * (k - 1)

# Démarre une boucle qui va s'exécuter m fois, en incrémentant i à chaque itération de la boucle.
for i in range(m):

    # Initialiser une nouvelle liste dp2 de taille k, contenant uniquement des 0.
    # Cette liste va contenir les nouveaux calculs pour l'itération courante de la boucle.
    dp2 = [0] * k

    # Boucler sur les positions j de 1 à k-1 (inclus).
    for j in range(1, k):

        # Calcul intermédiaire :
        # - dp2[j-1] : Le terme calculé précédemment, permet un cumul (dp2 est censé représenter des totaux accumulés).
        # - dp[k-j] : Un élément bien particulier de dp, calculé à partir de l'indice k-j.
        # - (f[j] - f[j-1]) : Différence entre deux valeurs consécutives de la liste f.
        # - On multiplie dp[k-j] par (f[j] - f[j-1]).
        # - On additionne cela à dp2[j-1].
        # - Le tout modulo Mod, pour rester dans les bornes d'entiers et respecter des contraintes algorithmiques.
        dp2[j] = (dp2[j-1] + dp[k-j] * (f[j] - f[j-1])) % Mod

    # À la fin de cette boucle imbriquée, on prépare dp pour l'itération suivante de la boucle principale 
    # en écrasant la référence précédente avec la nouvelle liste calculée dp2.
    dp = dp2

# Après avoir exécuté la boucle principale m fois, le résultat final se trouve dans la dernière valeur de dp (dp[k-1]).
# On affiche ce résultat avec print(). Cela donnera la réponse au problème.
print(dp[k-1])