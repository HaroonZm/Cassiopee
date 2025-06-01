def init_sets(size):
    # initialize each element as its own parent
    return [i for i in range(size)]

def find_root(parents, idx):
    while parents[idx] != idx:
        # path compression kinda thing
        parents[idx] = parents[parents[idx]]
        idx = parents[idx]
    return idx

def union_sets(parents, x, y):
    root_x = find_root(parents, x)
    root_y = find_root(parents, y)
    if root_x != root_y:
        parents[root_x] = root_y  # merge

def same_set(parents, x, y):
    return find_root(parents, x) == find_root(parents, y)

def generate_fibs():
    fibs = []
    a, b = 1, 1
    while len(fibs) < 1000:
        c = (a + b) % 1001  # mod to keep numbers small
        fibs.append(c)
        a, b = b, c
    return fibs

if __name__ == "__main__":
    try:
        fib_sequence = generate_fibs()
        while True:
            line = input().strip()
            if not line:
                continue
            V, d = map(int, line.split())
            arr = init_sets(V)
            current_fibs = fib_sequence[:V]

            for i in range(V):
                for j in range(i + 1, V):
                    if abs(current_fibs[i] - current_fibs[j]) < d:
                        union_sets(arr, i, j)

            groups = {}
            for i in range(V):
                r = find_root(arr, i)
                if r not in groups:
                    groups[r] = [current_fibs[i]]
                else:
                    groups[r].append(current_fibs[i])

            print(len(groups))

    except EOFError:
        pass