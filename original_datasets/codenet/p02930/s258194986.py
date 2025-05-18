input = raw_input

N = int(input())

levels = [[0 for j in range(501)] for i in range(501)]

nums = [0 for i in range(501)]
nums[2] = 1
nums[3] = 2

graphs = [None for i in range(501)]
graph2 = [[None, None, None], [None, None, 1], [None, 1, None]]
graphs[2] = graph2
graph3 = [[None for i in range(3+1)] for j in range(3+1)]
graph3[1][2] = 2
graph3[1][3] = 1
graph3[2][1] = 2
graph3[2][3] = 1
graph3[3][1] = 1
graph3[3][2] = 1
graphs[3] = graph3

def get_graph(cur_graph, nodes):
    n_nodes = len(nodes)

    old_graph = graphs[n_nodes]
    #print(old_graph, cur_graph, n_nodes)
    new_nodes = nodes
    old_nodes = list(range(1, n_nodes+1))

    for i, new_node1 in enumerate(new_nodes):
        old_node1 = i + 1
        for j2, new_node2 in enumerate(new_nodes[i+1:]):
            j = i + j2 + 1
            #if i == j:
            #    continue
            old_node2 = j + 1
            #print(new_node1, new_node2, old_node1, old_node2)
            cur_graph[new_node1][new_node2] = old_graph[old_node1][old_node2] + 1

    return cur_graph

for n in range(4, N+1):
    n1 = n // 2 
    n2 = n1

    if n % 2 == 1:
        n1 += 1

    nodes1 = [i for i in range(1, n1+1)]
    nodes2 = [i for i in range(n1+1, n+1)]

    cur_graph = [[None for i in range(n+1)] for j in range(n+1)]
    for node1 in nodes1:
        for node2 in nodes2:
            cur_graph[node1][node2] = 1
            cur_graph[node2][node1] = 1

    nums[n] = 1 + max(nums[n1], nums[n2])

    min_level = 2
    cur_graph = get_graph(cur_graph, nodes1)
    cur_graph = get_graph(cur_graph, nodes2)

    graphs[n] = cur_graph

cur_graph = graphs[N]
for i in range(1, N+1):
    out_txt = " ".join([str(cur_graph[i][j]) for j in range(i+1, N+1)])
    print(out_txt)
#out = nums[N]