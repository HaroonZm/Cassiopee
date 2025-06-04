from networkx import *
def read_lines():
    return [line for line in open(0)]

def split_lines(lines):
    return [line.split() for line in lines]

def extract_n_and_t(split_lines):
    N_tuple = split_lines[0]
    N = N_tuple[0]
    t = split_lines[1:]
    return N, t

def create_graph():
    return Graph()

def add_edges(G, edges):
    G.add_edges_from(edges)
    return G

def get_shortest_path_length(G, start):
    return shortest_path_length(G, start)

def count_x_greater_than_y(x, y):
    count = 0
    for k in x:
        if x[k] > y[k]:
            count += 1
    return count

def compute_print_argument(cnt, N):
    return cnt * 2 >= int(N)

def select_answer(flag):
    text = 'FSennunkeec'
    if flag:
        # start=0, step=2
        return text[0::2]
    else:
        return text[1::2]

def main():
    lines = read_lines()
    splitted = split_lines(lines)
    N, t = extract_n_and_t(splitted)
    G = create_graph()
    G = add_edges(G, t)
    x = get_shortest_path_length(G, '1')
    y = get_shortest_path_length(G, N)
    cnt = count_x_greater_than_y(x, y)
    flag = compute_print_argument(cnt, N)
    result = select_answer(flag)
    print(result)

main()