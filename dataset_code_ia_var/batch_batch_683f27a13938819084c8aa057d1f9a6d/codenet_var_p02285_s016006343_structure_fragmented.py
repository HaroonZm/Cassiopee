class Node:
    def __init__(self, key, left, right, parent):
        self.key = key
        self.left = left
        self.right = right
        self.p = parent

    def __repr__(self):
        return str(self.key)

def set_parent(z, y):
    z.p = y

def is_left_smaller(z, x):
    return z.key < x.key

def is_right_bigger(z, x):
    return z.key >= x.key

def update_T(T, z):
    T = z
    print(T)
    return T

def attach_left(y, z):
    y.left = z

def attach_right(y, z):
    y.right = z

def insert_search_loop(x, z):
    y = None
    while x is not None:
        y = x
        if is_left_smaller(z, x):
            x = x.left
        else:
            x = x.right
    return y

def insert(T, z):
    y = insert_search_loop(T, z)
    set_parent(z, y)
    if y is None:
        T = update_T(T, z)
    elif is_left_smaller(z, y):
        attach_left(y, z)
    else:
        attach_right(y, z)
    return T

def is_none(x):
    return x is None

def find_key(x, k):
    return k == x.key

def print_yes():
    print("yes")

def print_no():
    print("no")

def move_left(x):
    return x.left

def move_right(x):
    return x.right

def less_than_key(k, x):
    return k < x.key

def find_loop(x, k, show):
    while not is_none(x):
        if find_key(x, k):
            if show:
                print_yes()
            return x
        if less_than_key(k, x):
            x = move_left(x)
        else:
            x = move_right(x)
    print_no()
    return None

def find(T, k, show):
    return find_loop(T, k, show)

def right_is_none(x):
    return x.right is None

def go_to_parent(x):
    return x.p

def is_right_child(x, y):
    return x == y.right

def get_scu_from_right(x):
    x = x.right
    y = None
    while x is not None:
        y = x
        x = x.left
    return y

def get_scu_parent_loop(x, y):
    while is_right_child(x, y) and y is not None:
        x = y
        y = go_to_parent(x)
    return y

def getScu(x):
    if right_is_none(x):
        y = go_to_parent(x)
        return get_scu_parent_loop(x, y)
    return get_scu_from_right(x)

def is_leaf(x):
    return x.left is None and x.right is None

def is_left_none(x):
    return x.left is None

def is_right_none(x):
    return x.right is None

def parent_key_lower(x):
    return x.p.key < x.key

def detach_parent_right(x):
    x.p.right = None

def detach_parent_left(x):
    x.p.left = None

def assign_node_attrs(x, y):
    x.key = y.key
    x.right = y.right
    x.left = y.left

def delete_leaf(x):
    if parent_key_lower(x):
        detach_parent_right(x)
    else:
        detach_parent_left(x)

def delete_single_left(x):
    y = x.right
    assign_node_attrs(x, y)

def delete_single_right(x):
    y = x.left
    assign_node_attrs(x, y)

def delete_with_scu(T, x):
    y = getScu(x)
    delete(T, y)
    x.key = y.key

def delete_node(T, x):
    if is_leaf(x):
        delete_leaf(x)
    elif is_left_none(x):
        delete_single_left(x)
    elif is_right_none(x):
        delete_single_right(x)
    else:
        delete_with_scu(T, x)

def delete(T, x):
    if x is None:
        return
    delete_node(T, x)

def preorder_traverse(x):
    if is_none(x):
        return []
    return preorder_traverse(x.left) + [x] + preorder_traverse(x.right)

def printPreorder(x):
    lst = preorder_traverse(x)
    for node in lst:
        print(" ", end='')
        print(node, end='')

def midorder_traverse(x):
    if is_none(x):
        return []
    return [x] + midorder_traverse(x.left) + midorder_traverse(x.right)

def printMidorder(x):
    lst = midorder_traverse(x)
    for node in lst:
        print(" ", end='')
        print(node, end='')

def printal(x):
    printPreorder(x)
    print()
    printMidorder(x)
    print()

def read_int():
    return int(input())

def read_command():
    return input().split()

def first_init_node(Q):
    return Node(int(Q[1]), None, None, None)

def iterative_commands_loop(N, T):
    for _ in range(N-1):
        Q = read_command()
        process_command(Q, T)

def process_command(Q, T):
    if Q[0] == "print":
        printal(T[0])
    elif Q[0] == "find":
        find(T[0], int(Q[1]), True)
    elif Q[0] == "delete":
        to_delete = find(T[0], int(Q[1]), False)
        delete(T[0], to_delete)
    else:
        node = Node(int(Q[1]), None, None, None)
        T[0] = insert(T[0], node)

def main():
    N = read_int()
    Q = read_command()
    T = [first_init_node(Q)]
    iterative_commands_loop(N, T)

main()