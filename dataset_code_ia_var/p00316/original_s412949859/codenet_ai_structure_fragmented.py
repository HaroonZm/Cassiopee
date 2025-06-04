def read_initial_values():
    n, m, k = map(int, input().split())
    return n, m, k

def initialize_parent(n):
    return [i for i in range(n)]

def initialize_club(n):
    return [-1 for _ in range(n)]

def find(x, parent):
    if x == parent[x]:
        return x
    ret = find(parent[x], parent)
    parent[x] = ret
    return ret

def read_query():
    t, a, b = map(int, input().split())
    a -= 1
    b -= 1
    return t, a, b

def process_type1(a, b, parent, club):
    p_a = find(a, parent)
    p_b = find(b, parent)
    c_a = club[p_a]
    c_b = club[p_b]
    conflict = False
    if c_a >= 0 and c_b >= 0 and c_a != c_b:
        conflict = True
    if c_a < 0 and c_b >= 0:
        club[p_a] = c_b
    parent[p_b] = p_a
    return conflict

def process_type2(a, b_val, parent, club):
    p_a = find(a, parent)
    conflict = False
    if club[p_a] < 0:
        club[p_a] = b_val
    if club[p_a] >= 0 and club[p_a] != b_val:
        conflict = True
    return conflict

def main():
    n, m, k = read_initial_values()
    parent = initialize_parent(n)
    club = initialize_club(n)

    def process_query(count):
        t, a, b = read_query()
        if t == 1:
            return process_type1(a, b, parent, club)
        else:
            return process_type2(a, b, parent, club)

    terminated = False
    for count in range(1, k + 1):
        conflict = process_query(count)
        if conflict:
            print(count)
            terminated = True
            break
    if not terminated:
        print(0)

main()