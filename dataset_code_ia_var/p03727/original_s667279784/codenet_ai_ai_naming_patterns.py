import queue

node_count = int(input())
duplicate_edge_queue = queue.Queue()
adjacency_sets = [set() for _ in range(node_count + 1)]

for edge_index in range(2 * node_count - 2):
    node_u, node_v = map(int, input().split())
    if node_v in adjacency_sets[node_u]:
        duplicate_edge_queue.put((node_u, node_v))
    else:
        adjacency_sets[node_u].add(node_v)
        adjacency_sets[node_v].add(node_u)

parent = [i for i in range(node_count + 1)]

def find_root(node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find_root(parent[node])
        return parent[node]

while not duplicate_edge_queue.empty():
    node_u, node_v = map(find_root, duplicate_edge_queue.get())
    if node_u == node_v:
        continue
    if len(adjacency_sets[node_u]) < len(adjacency_sets[node_v]):
        node_u, node_v = node_v, node_u
    adjacency_sets[node_u].remove(node_v)
    adjacency_sets[node_v].remove(node_u)
    for neighbor in list(adjacency_sets[node_v]):
        adjacency_sets[neighbor].remove(node_v)
        if node_u in adjacency_sets[neighbor]:
            duplicate_edge_queue.put((node_u, neighbor))
        else:
            adjacency_sets[node_u].add(neighbor)
            adjacency_sets[neighbor].add(node_u)
    adjacency_sets[node_v].clear()
    parent[node_v] = node_u

connected_root = find_root(1)
for check_node in range(2, node_count + 1):
    if find_root(check_node) != connected_root:
        print("NO")
        break
else:
    print("YES")