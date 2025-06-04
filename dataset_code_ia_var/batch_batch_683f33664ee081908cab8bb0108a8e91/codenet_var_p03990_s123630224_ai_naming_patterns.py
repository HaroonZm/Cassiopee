import sys
sys.setrecursionlimit(2147483647)

CONST_INF = float("inf")
CONST_MOD = 10**9 + 7

read_input = lambda: sys.stdin.readline().rstrip()

def main():
    node_count, start_a_idx, start_b_idx = map(int, read_input().split())
    start_a_idx -= 1
    start_b_idx -= 1

    graph_tree1 = [[] for _ in range(node_count)]
    graph_tree2 = [[] for _ in range(node_count)]

    for _ in range(node_count - 1):
        node_u, node_v = map(int, read_input().split())
        node_u -= 1
        node_v -= 1
        graph_tree1[node_u].append(node_v)
        graph_tree1[node_v].append(node_u)

    for _ in range(node_count - 1):
        node_u, node_v = map(int, read_input().split())
        node_u -= 1
        node_v -= 1
        graph_tree2[node_u].append(node_v)
        graph_tree2[node_v].append(node_u)

    parent_list = [None] * node_count
    parent_list[start_b_idx] = start_b_idx
    tree2_depth = [None] * node_count
    tree2_depth[start_b_idx] = 0
    queue_tree2 = [start_b_idx]

    while queue_tree2:
        curr_node = queue_tree2.pop()
        for neighbor in graph_tree2[curr_node]:
            if tree2_depth[neighbor] is not None:
                continue
            tree2_depth[neighbor] = tree2_depth[curr_node] + 1
            parent_list[neighbor] = curr_node
            queue_tree2.append(neighbor)

    winning_pos_list = [0] * node_count
    for curr_node in range(node_count):
        for neighbor in graph_tree1[curr_node]:
            if (parent_list[curr_node] == neighbor or 
                parent_list[neighbor] == curr_node or 
                parent_list[curr_node] == parent_list[neighbor] or 
                parent_list[parent_list[curr_node]] == neighbor or 
                parent_list[parent_list[neighbor]] == curr_node):
                continue
            winning_pos_list[neighbor] = 1
            winning_pos_list[curr_node] = 1

    result_max_depth = tree2_depth[start_a_idx]
    tree1_depth = [None] * node_count
    tree1_depth[start_a_idx] = 0
    queue_tree1 = [start_a_idx]

    while queue_tree1:
        curr_node = queue_tree1.pop()
        if winning_pos_list[curr_node]:
            print(-1)
            return
        for neighbor in graph_tree1[curr_node]:
            if tree1_depth[neighbor] is not None:
                continue
            tree1_depth[neighbor] = tree1_depth[curr_node] + 1
            result_max_depth = max(result_max_depth, tree2_depth[neighbor])
            if tree1_depth[neighbor] < tree2_depth[neighbor]:
                queue_tree1.append(neighbor)

    print(2 * result_max_depth)

main()