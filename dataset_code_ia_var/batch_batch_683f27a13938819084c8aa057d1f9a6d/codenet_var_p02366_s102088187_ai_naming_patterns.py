import sys
sys.setrecursionlimit(100000)

num_vertices, num_edges = map(int, input().split())
adjacency_list = [[] for _ in range(num_vertices)]
for _ in range(num_edges):
    start_vertex, end_vertex = map(int, input().split())
    adjacency_list[start_vertex].append(end_vertex)
    adjacency_list[end_vertex].append(start_vertex)

dfs_prenumber = [None for _ in range(num_vertices)]
dfs_parent = [None for _ in range(num_vertices)]
dfs_lowest_ancestor = [None for _ in range(num_vertices)]
dfs_visited = [False for _ in range(num_vertices)]

def dfs_articulation(node_index=0, parent_index=-1, visit_order=0):
    dfs_prenumber[node_index] = visit_order
    dfs_lowest_ancestor[node_index] = visit_order
    visit_order += 1
    dfs_visited[node_index] = True

    for neighbor in adjacency_list[node_index]:
        if not dfs_visited[neighbor]:
            dfs_parent[neighbor] = node_index
            dfs_articulation(neighbor, node_index, visit_order)
            dfs_lowest_ancestor[node_index] = min(dfs_lowest_ancestor[node_index], dfs_lowest_ancestor[neighbor])
        elif neighbor != parent_index:
            dfs_lowest_ancestor[node_index] = min(dfs_lowest_ancestor[node_index], dfs_prenumber[neighbor])

dfs_articulation()

articulation_points_set = set()

for vertex in range(1, num_vertices):
    parent_vertex = dfs_parent[vertex]
    if dfs_prenumber[parent_vertex] <= dfs_lowest_ancestor[vertex]:
        articulation_points_set.add(parent_vertex)

if dfs_parent.count(0) >= 2:
    articulation_points_set.add(0)
else:
    articulation_points_set.discard(0)

articulation_points_list = list(articulation_points_set)
articulation_points_list.sort()

if articulation_points_list:
    print(*articulation_points_list, sep='\n')