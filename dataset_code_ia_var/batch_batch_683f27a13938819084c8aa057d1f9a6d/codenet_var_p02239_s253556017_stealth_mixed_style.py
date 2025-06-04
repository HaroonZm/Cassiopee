n = int(input())

adjacency = {1: []}
for idx in range(1, n+1):
    tokens = input().split()
    neighbors = list(map(int, tokens[2:]))
    adjacency[idx] = neighbors

searched = dict()
for i in range(1, n+1):
    searched[i] = False

dist = [-1] * (n + 1)
dist[0] = None

def breadth_first(root):
    searched[root] = True
    dist[root] = 0
    curr_level = [root]
    level = 0
    while len(curr_level):
        tmp = []
        level += 1
        for node in curr_level:
            for next_node in adjacency[node]:
                if not searched[next_node]:
                    searched[next_node] = True
                    dist[next_node] = level
                    tmp.append(next_node)
        curr_level = tmp

(lambda f: f(1))(breadth_first)

i = 1
while i <= n:
    print(i, dist[i])
    i += 1