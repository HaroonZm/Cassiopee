V = int(input())
graph = [input() for _ in range(V)]

visited = [False] * V

def dfs(u):
    stack = [u]
    count = 0
    visited[u] = True
    while stack:
        node = stack.pop()
        count += 1
        for v in range(V):
            if graph[node][v] == 'Y' and not visited[v]:
                visited[v] = True
                stack.append(v)
    return count

components = []
for i in range(V):
    if not visited[i]:
        c = dfs(i)
        components.append(c)

# nombre d'arêtes à ajouter pour connecter tous les composants = nombre_de_composants -1
edges_to_add = len(components) - 1

# si edges_to_add est impair => Taro gagne, sinon Hanako gagne
if edges_to_add % 2 == 1:
    print("Taro")
else:
    print("Hanako")