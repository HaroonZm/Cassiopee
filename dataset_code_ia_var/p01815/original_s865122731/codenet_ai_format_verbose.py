def find_representative(node_index):

    if parent[node_index] == node_index:

        return node_index

    else:

        parent[node_index] = find_representative(parent[node_index])

        return parent[node_index]



def union_sets(node_index_a, node_index_b):

    root_a = find_representative(node_index_a)

    root_b = find_representative(node_index_b)

    if tree_rank[root_a] < tree_rank[root_b]:

        parent[root_a] = root_b

        component_weight[root_b] += component_weight[root_a]

    else:

        parent[root_b] = root_a

        component_weight[root_a] += component_weight[root_b]

        if tree_rank[root_a] == tree_rank[root_b]:

            tree_rank[root_a] += 1



def are_in_same_set(node_index_a, node_index_b):

    return find_representative(node_index_a) == find_representative(node_index_b)



def depth_first_search(current_node, previous_node):

    if node_visited[current_node] or current_node != find_representative(current_node):

        while len(traversal_path) > 0:

            union_sets(1, traversal_path.pop())

        return

    node_visited[current_node] = 1

    traversal_path.append(current_node)

    for adjacent_node in original_graph[current_node]:

        if adjacent_node == previous_node:

            continue

        depth_first_search(adjacent_node, current_node)

    node_visited[current_node] = 0

    if len(traversal_path) > 0 and traversal_path[-1] == current_node:

        traversal_path.pop()



def calculate_max_weight(current_node):

    node_visited[current_node] = 1

    maximum_weight_in_subtree = 0

    for index in range(len(component_graph[current_node])):

        for adjacent in original_graph[component_graph[current_node][index]]:

            if node_visited[find_representative(adjacent)] == 0:

                maximum_weight_in_subtree = max(

                    maximum_weight_in_subtree,

                    calculate_max_weight(find_representative(adjacent))

                )

    return maximum_weight_in_subtree + component_weight[find_representative(current_node)]



import sys

from collections import defaultdict



sys.setrecursionlimit(1000000)

number_of_nodes, number_of_edges = map(int, input().split())

component_weight = [0]

component_weight.extend(list(map(int, input().split())))



original_graph = defaultdict(list)

for _ in range(number_of_edges):

    edge_start, edge_end = map(int, input().split())

    original_graph[edge_start].append(edge_end)

    original_graph[edge_end].append(edge_start)



traversal_path = []

component_graph = [[] for _ in range(number_of_nodes + 1)]

node_visited = [0] * (number_of_nodes + 1)

parent = [node_index for node_index in range(number_of_nodes + 1)]

tree_rank = [0] * (number_of_nodes + 1)



depth_first_search(1, -1)



for node_index in range(1, number_of_nodes + 1):

    component_graph[find_representative(node_index)].append(node_index)



print(calculate_max_weight(find_representative(1)))