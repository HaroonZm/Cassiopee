def disjoint_set_init(size):
    return [i for i in range(size)]

def disjoint_set_find_parent(ds_parents, node_idx):
    while ds_parents[node_idx] != node_idx:
        ds_parents[node_idx] = ds_parents[ds_parents[node_idx]]
        node_idx = ds_parents[node_idx]
    return node_idx

def disjoint_set_union(ds_parents, node_a_idx, node_b_idx):
    root_a = disjoint_set_find_parent(ds_parents, node_a_idx)
    root_b = disjoint_set_find_parent(ds_parents, node_b_idx)
    if root_a != root_b:
        ds_parents[root_a] = root_b

def disjoint_set_same(ds_parents, node_a_idx, node_b_idx):
    return disjoint_set_find_parent(ds_parents, node_a_idx) == disjoint_set_find_parent(ds_parents, node_b_idx)

def fibonacci_sequence_generate(limit_count=1000, modulo=1001):
    fib_sequence = []
    fib_prev = 1
    fib_curr = 1
    while len(fib_sequence) < limit_count:
        fib_next = (fib_prev + fib_curr) % modulo
        fib_prev = fib_curr
        fib_curr = fib_next
        fib_sequence.append(fib_next)
    return fib_sequence

if __name__ == '__main__':
    try:
        precomputed_fibs = fibonacci_sequence_generate()
        while True:
            vertex_count, diff_threshold = map(int, input().strip().split())
            fib_values = precomputed_fibs[:vertex_count]
            ds_parents = disjoint_set_init(vertex_count)

            for node_idx_i in range(vertex_count):
                for node_idx_j in range(node_idx_i + 1, vertex_count):
                    if abs(fib_values[node_idx_i] - fib_values[node_idx_j]) < diff_threshold:
                        disjoint_set_union(ds_parents, node_idx_i, node_idx_j)

            set_dict = {}
            for idx in range(vertex_count):
                root = disjoint_set_find_parent(ds_parents, idx)
                if root in set_dict:
                    set_dict[root].append(fib_values[idx])
                else:
                    set_dict[root] = [fib_values[idx]]

            print(len(set_dict))

    except EOFError:
        pass