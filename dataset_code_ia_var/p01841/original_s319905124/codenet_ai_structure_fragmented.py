from sys import setrecursionlimit
setrecursionlimit(10 ** 8)

def read_input():
    return input()

def create_root_array(size=1000):
    return [[-1] * 3 for _ in range(size)]

def get_initialized_source(S):
    return Source(S)

class Source():
    def __init__(self, S):
        self.S = S
        self.pos = 0

def peek_character(S):
    if S.pos < len(S.S):
        return S.S[S.pos]
    return -1

def move_next(S):
    S.pos += 1

def index_increment(i):
    i[0] += 1

def construct_tree(S, A, i):
    move_next(S)
    if end_of_subtree(S):
        move_next(S)
        return -1
    c = fetch_index(i)
    index_increment(i)
    l = get_next_index(i)
    left = construct_tree(S, A, i)
    center = parse_root(S, A)
    index_increment(i)
    r = get_next_index(i)
    right = construct_tree(S, A, i)
    assign_tree_node(A, c, center, l, r)
    move_next(S)
    return c

def end_of_subtree(S):
    return peek_character(S) == ')'

def fetch_index(i):
    return i[0]

def get_next_index(i):
    return i[0]

def assign_tree_node(A, idx, center, l, r):
    A[idx] = [center, l, r]

def parse_root(S, A):
    res = 0
    move_next(S)
    while not is_end_of_center(S):
        res = accumulate_center(res, S)
        move_next(S)
    move_next(S)
    return res

def is_end_of_center(S):
    return peek_character(S) == ']'

def accumulate_center(res, S):
    return res * 10 + int(peek_character(S))

def prepare_source_string(s):
    return '(' + s + ')'

def initialize_tree(S_str, root_array):
    return construct_tree(get_initialized_source(S_str), root_array, [0])

def get_left(A, i):
    return A[i][1]

def get_right(A, i):
    return A[i][2]

def get_center(A, i):
    return A[i][0]

def is_empty_node(A, i):
    return A[i][0] == -1

def node_to_string(value):
    return '[' + str(value) + ']'

def make_empty_subtree():
    return '()'

def recursive_f(i, j, A_root, B_root):
    if is_empty_node(A_root, i) or is_empty_node(B_root, j):
        return make_empty_subtree()
    left_part = recursive_f(get_left(A_root, i), get_left(B_root, j), A_root, B_root)
    center_part = node_to_string(get_center(A_root, i) + get_center(B_root, j))
    right_part = recursive_f(get_right(A_root, i), get_right(B_root, j), A_root, B_root)
    return '(' + left_part + center_part + right_part + ')'

def get_final_output(s):
    return s[1:-1]

def main():
    A = read_input()
    B = read_input()

    A_root = create_root_array()
    B_root = create_root_array()

    S_A = prepare_source_string(A)
    S_B = prepare_source_string(B)

    initialize_tree(S_A, A_root)
    initialize_tree(S_B, B_root)

    result = recursive_f(0, 0, A_root, B_root)
    print(get_final_output(result))


main()