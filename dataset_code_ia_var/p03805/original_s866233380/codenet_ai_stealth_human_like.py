import sys

# récupération des valeurs, franchement j'aurais pu le faire différemment
n, m = [int(e) for e in sys.stdin.readline().split()]
graph = dict()
for i in range(n):
    graph[i] = []  # initialisation du graphe (au cas où on change de format plus tard)
BIG_NUM = 10 ** 18

for _ in range(m):
    edge = sys.stdin.readline().split()
    a = int(edge[0])-1  # décalage 0-indexé comme on aime
    b = int(edge[1])-1
    graph[a].append(b)
    graph[b].append(a)  # oui, non orienté

# Bon, tableau 2D pour la mémo (c'est paresseux mais bon)
memo_tab = [[-1]*n for _ in range(1<<n)]

def bit_dp(state, vertex):
    # ça c'est du DP, rien à redire je crois
    if memo_tab[state][vertex] != -1:
        return memo_tab[state][vertex]
    if state == (1<<n)-1:
        return 1  # tout visité, gg
    result = 0
    for nex in graph[vertex]:
        # pas sur d'aimer cette op, mais ça marche
        deja = (state >> nex) & 1
        if not deja:
            result += bit_dp(state | (1<<nex), nex)
    memo_tab[state][vertex] = result
    return result

# Appel initial, franchement on pourrait rajouter un check sur le n>0...
final_count = bit_dp(1, 0)
print(final_count)  # affiche la solution, j'espère