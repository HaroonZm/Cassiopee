n = int(input())  # Nombre de clés
p = list(map(float, input().split()))  # Probabilités des clés p_1 ... p_n
q = list(map(float, input().split()))  # Probabilités des clés fantômes q_0 ... q_n

# On va utiliser la programmation dynamique pour calculer le coût minimal attendu d'un arbre binaire de recherche optimal selon l'algorithme classique.

# Initialisation de matrices carrées (n+1)x(n+1)
# e[i][j] : coût attendu minimal pour sous-arbre contenant les clés Ki+1 ... Kj (i entre 0 et n, j entre i-1 et n)
# w[i][j] : somme des probabilités p et q entre i et j (incluant p_i+1 ... p_j et q_i ... q_j)
# root[i][j] : racine optimale pour sous-arbre Ki+1 ... Kj (non utilisée ici car on veut que l'espérance)

e = [[0.0]*(n+1) for _ in range(n+1)]
w = [[0.0]*(n+1) for _ in range(n+1)]

# Initialisation des coûts et poids pour les arbres vides (i == j)
for i in range(n+1):
    e[i][i] = q[i]  # Quand il n'y a pas de clé, le coût est la probabilité du dummy key d_i
    w[i][i] = q[i]

# Calcul du coût minimal attendu pour des intervalles de clé croissants
for length in range(1, n+1):  # longueur des sous-arbres considérés
    for i in range(n - length + 1):
        j = i + length
        # Calculer la somme des probabilités pour cet intervalle (i .. j)
        w[i][j] = w[i][j-1] + p[j-1] + q[j]
        # Trouver la racine k optimale dans [i+1 .. j]
        # On doit minimiser e[i][k-1] + e[k][j] + w[i][j]
        # On initialise e[i][j] avec une grande valeur
        e[i][j] = float('inf')
        for r in range(i+1, j+1):
            cost = e[i][r-1] + e[r][j] + w[i][j]
            if cost < e[i][j]:
                e[i][j] = cost

# e[0][n] contient le coût minimal attendu pour l'arbre complet avec toutes les clés

# Affichage avec 8 chiffres après la virgule pour respecter la précision requise
print(f"{e[0][n]:.8f}")