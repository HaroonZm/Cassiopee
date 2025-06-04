def main():
    while True:
        n, m = read_input_data()
        if n == 0:
            break
        tbl = read_table(m)
        run_problem(n, m, tbl)

def read_input_data():
    values = input().split()
    return int(values[0]), int(values[1])

def read_table(m):
    return [list(map(int, input().split())) for _ in range(m)]

def run_problem(n, m, tbl):
    f = make_flag_list(m)
    global_tmp = [0] * 12
    best_length = [0]
    best_path = [[]]
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if not different_nodes(a, b):
                continue
            for i in range(m):
                if edge_unused_and_connects(f, tbl, i, a, b):
                    use_edge(f, i)
                    set_tmp_start(global_tmp, a, b)
                    combi(
                        k=2, a=b, w=tbl[i][2], n=n, m=m, tbl=tbl, f=f,
                        tmp=global_tmp, best_length=best_length, best_path=best_path
                    )
                    unuse_edge(f, i)
    print_result(best_length, best_path)

def make_flag_list(m):
    return [0] * m

def different_nodes(a, b):
    return a != b

def edge_unused_and_connects(f, tbl, i, a, b):
    return (not f[i]) and connects(tbl[i], a, b)

def connects(edge, a, b):
    return (edge[0] == a and edge[1] == b) or (edge[0] == b and edge[1] == a)

def use_edge(f, i):
    f[i] = 1

def unuse_edge(f, i):
    f[i] = 0

def set_tmp_start(tmp, a, b):
    tmp[0] = a
    tmp[1] = b

def combi(k, a, w, n, m, tbl, f, tmp, best_length, best_path):
    for b in range(1, n + 1):
        if not different_nodes(b, a):
            continue
        for i in range(m):
            if edge_unused_and_connects(f, tbl, i, a, b):
                use_edge(f, i)
                set_tmp_elem(tmp, k, b)
                combi(k + 1, b, w + tbl[i][2], n, m, tbl, f, tmp, best_length, best_path)
                unuse_edge(f, i)
    update_best(w, k, tmp, best_length, best_path)

def set_tmp_elem(tmp, k, b):
    tmp[k] = b

def update_best(w, k, tmp, best_length, best_path):
    if w > best_length[0]:
        best_length[0] = w
        best_path[0] = tmp[:k]

def print_result(best_length, best_path):
    print(best_length[0])
    print(*best_path[0])

main()