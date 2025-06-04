n = 40

# Construisons un graphe en deux parties :
# - Un clique K20 complet (tous connectés entre eux)
# - Un ensemble indépendant I20 (aucune arête entre eux)
# Puis, on connecte chaque sommet de I20 à tous les sommets de K20.
# Ce graphe aura une grande différence entre A(G) et E(G) car l'algorithme de Jiro a tendance à choisir peu dans le clique et peu du côté indépendant en même temps.

adj = [['N'] * n for _ in range(n)]

# Construire le clique K20 (indices 0 à 19)
for i in range(20):
    for j in range(i + 1, 20):
        adj[i][j] = 'Y'
        adj[j][i] = 'Y'

# Connecter chaque sommet de I20 (indices 20 à 39) à tous les sommets de K20
for i in range(20, 40):
    for j in range(20):
        adj[i][j] = 'Y'
        adj[j][i] = 'Y'

# La diagonale reste 'N' pour pas de self-loop

print(n)
for i in range(n):
    print("".join(adj[i]))