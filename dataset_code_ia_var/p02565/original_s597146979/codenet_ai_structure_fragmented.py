import sys
import io
import os
import networkx as nx

def extend_sys_path():
    sys.path.append("/home/contestant/.local/lib/python3.8/site-packages")

def create_input_reader():
    return io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def parse_first_line(input):
    return [int(x) for x in input().split()]

def parse_flag_positions(N, input):
    result = []
    for _ in range(N):
        result.append([int(x) for x in input().split()])
    return result

def create_nodes(graph, N):
    for i in range(2 * N):
        graph.add_node(i)

def add_edge(graph, u, v):
    graph.add_edge(u, v)

def process_constraint_x1_x2(i, j, x1, x2, D, graph, N):
    if abs(x1 - x2) < D:
        add_edge(graph, i, j + N)

def process_constraint_x1_y2(i, j, x1, y2, D, graph):
    if abs(x1 - y2) < D:
        add_edge(graph, i, j)

def process_constraint_y1_x2(i, j, y1, x2, D, graph, N):
    if abs(y1 - x2) < D:
        add_edge(graph, i + N, j + N)

def process_constraint_y1_y2(i, j, y1, y2, D, graph, N):
    if abs(y1 - y2) < D:
        add_edge(graph, i + N, j)

def process_pair_constraints(i, j, N, XY, D, graph):
    if i == j:
        return
    x1, y1 = XY[i]
    x2, y2 = XY[j]
    process_constraint_x1_x2(i, j, x1, x2, D, graph, N)
    process_constraint_x1_y2(i, j, x1, y2, D, graph)
    process_constraint_y1_x2(i, j, y1, x2, D, graph, N)
    process_constraint_y1_y2(i, j, y1, y2, D, graph, N)

def construct_graph(N, XY, D):
    graph = nx.DiGraph()
    create_nodes(graph, N)
    for i in range(N):
        for j in range(N):
            process_pair_constraints(i, j, N, XY, D, graph)
    return graph

def check_SCC_conflict(comp, N):
    for x in comp:
        if (x < N and x + N in comp) or (x >= N and x - N in comp):
            return True
    return False

def assign_component(comp, assignment, N):
    for x in comp:
        if x not in assignment:
            assignment[x] = True
            opposite = (x + N) % (2 * N)
            assignment[opposite] = False

def process_SCCs(SCC, N):
    assignment = {}
    for comp in SCC:
        if check_SCC_conflict(comp, N):
            print("No")
            exit()
        assign_component(comp, assignment, N)
    return assignment

def output_result(assignment, N, XY):
    print("Yes")
    for i in range(N):
        print(XY[i][0] if assignment[i] else XY[i][1])

def main():
    extend_sys_path()
    input = create_input_reader()
    N, D = parse_first_line(input)
    XY = parse_flag_positions(N, input)
    graph = construct_graph(N, XY, D)
    SCC = nx.algorithms.components.strongly_connected_components(graph)
    assignment = process_SCCs(SCC, N)
    output_result(assignment, N, XY)

main()