# Prend une entrée utilisateur et la convertit en un entier.
# Cela représente le nombre de pierres, ou d'étapes, dans le problème.
N = int(input()) # Exemple : si l'utilisateur entre '4', alors N vaudra 4.

# Prend une seule ligne d'entrée utilisateur contenant N nombres séparés par des espaces.
# Split divise la chaîne en une liste de chaînes, chacune étant un nombre.
# map applique la fonction int() à chaque chaîne pour convertir chaque nombre en entier.
# La liste finale, h_list, contient la hauteur de chaque pierre.
# Exemple : pour l'entrée '10 30 20 40', h_list sera [10, 30, 20, 40].
h_list = list(map(int, input().split()))

# Initialise la liste dp (programming dynamique) qui va contenir le coût minimal pour atteindre chaque pierre.
# On crée une liste vide pour chaque position (N positions), en prévision de remplir chaque élément plus tard.
dp = [[] for _ in range(N)]

# Fixe le coût pour atteindre la première pierre (indice 0).
# Comme on commence ici, aucun saut n'est nécessaire, donc le coût est 0.
dp[0] = 0

# Calcule et assigne le coût pour atteindre la deuxième pierre (indice 1).
# On ne peut venir qu'à partir de la pierre précédente (indice 0).
# La différence de hauteur est prise en valeur absolue car le coût ne peut pas être négatif.
dp[1] = abs(h_list[1] - h_list[0])

# Boucle sur les pierres de la troisième (indice 2) à la dernière (indice N-1).
for i in range(2, N):
    # Deux façons d'arriver sur la pierre i :
    # 1. Depuis la pierre (i-1) → coût "dp[i-1] + abs(h_list[i] - h_list[i-1])"
    # 2. Depuis la pierre (i-2) → coût "dp[i-2] + abs(h_list[i] - h_list[i-2])"
    # On prend le minimum des deux pour obtenir le coût minimum pour atteindre la pierre i.
    dp[i] = min(
        dp[i-2] + abs(h_list[i] - h_list[i-2]),
        dp[i-1] + abs(h_list[i] - h_list[i-1])
    )

# Affiche à l'écran la valeur du dernier élément de la liste dp, c'est-à-dire le coût minimal pour atteindre la dernière pierre.
print(dp[-1])