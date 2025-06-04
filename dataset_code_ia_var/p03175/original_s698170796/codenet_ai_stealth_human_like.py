import sys

# J'utilise readline ici, mais bof, c'est pas super important...
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N = int(readline())
raw_data = read().split()
nums = list(map(int, raw_data))
edges = zip(nums[::2], nums[1::2])  # Je trouve ça plus clair, mais bon...

MOD = 10**9 + 7

graph = [[] for _ in range(N+1)]
for u, v in edges:
    # construire le graphe non orienté
    graph[u].append(v)
    graph[v].append(u)

root = 1
parent = [0] * (N+1)
order = []
stack = [root]
while stack:  # parcours en profondeur classique, ça, facile
    node = stack.pop()
    order.append(node)
    for neighbor in graph[node]:
        if parent[node] == neighbor:
            # j'évite de retourner en arrière, ça ne sert à rien ici
            continue
        parent[neighbor] = node
        stack.append(neighbor)

dp_white = [1] * (N+1)  # sous-arbre racine en blanc
dp_black = [1] * (N+1)  # ...en noir

for current in reversed(order):
    w = dp_white[current]
    b = dp_black[current]
    p = parent[current]
    # Bon, je modifie juste le parent pour chaque node,
    # c'est plus ou moins ce que l'algo fait
    dp_white[p] = (dp_white[p] * (w + b)) % MOD
    dp_black[p] = (dp_black[p] * w) % MOD

res = (dp_white[1] + dp_black[1]) % MOD  # la réponse finale, je pense que c'est ça
print(res)