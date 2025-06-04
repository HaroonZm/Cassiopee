import sys

class Node:
    parent = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return "({},{},{},{})".format(self.key, self.parent, self.left, self.right)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return self.left is None and self.right is None

    def has_one_child(self):
        if self.is_leaf():
            return False
        elif (self.left is None) and (self.right is not None):
            return self.right
        elif (self.left is not None) and (self.right is None):
            return self.left
        else:
            return False

    def has_two_child(self):
        return (self.left is not None) and (self.right is not None)

root_node_no = None

def get_left_child(node):
    return node.left

def get_right_child(node):
    return node.right

def set_left_child(node, key):
    node.left = key

def set_right_child(node, key):
    node.right = key

def get_parent(node):
    return node.parent

def set_parent(node, key):
    node.parent = key

def cmp_node_key_less(node1, key):
    return node1.key < key

def cmp_node_key_greater(node1, key):
    return node1.key > key

def update_root(nodes, key):
    global root_node_no
    root_node_no = key
    nodes[key] = Node(key)

def insert(nodes: dict, in_node: Node):
    global root_node_no
    cur_node_no = root_node_no
    parent_node_no = None
    while not _check_while_insert_stop(cur_node_no):
        parent_node_no = cur_node_no
        cur_node_no = _update_cur_node_no(nodes, in_node.key, cur_node_no)
    _set_inserted_parent(in_node, parent_node_no)
    if _check_create_new_root(root_node_no):
        _do_insert_new_root(in_node)
    else:
        _do_insert_descendant(nodes, in_node, parent_node_no)
    _update_nodes_dict(nodes, in_node)

def _check_while_insert_stop(cur_node_no):
    return cur_node_no is None

def _update_cur_node_no(nodes, in_key, cur_node_no):
    if in_key < cur_node_no:
        return get_left_child(nodes[cur_node_no])
    else:
        return get_right_child(nodes[cur_node_no])

def _set_inserted_parent(in_node, parent_node_no):
    set_parent(in_node, parent_node_no)

def _check_create_new_root(root_node_no):
    return root_node_no is None

def _do_insert_new_root(in_node):
    global root_node_no
    root_node_no = in_node.key

def _do_insert_descendant(nodes, in_node, parent_node_no):
    if in_node.key < parent_node_no:
        set_left_child(nodes[parent_node_no], in_node.key)
    else:
        set_right_child(nodes[parent_node_no], in_node.key)

def _update_nodes_dict(nodes, in_node):
    nodes[in_node.key] = in_node

def inorder_tree_walk(nodes, node_no, inorder):
    _inorder_helper(nodes, node_no, inorder)

def _inorder_helper(nodes, node_no, inorder):
    if _inorder_base_case(node_no):
        return
    _inorder_helper(nodes, get_left_child(nodes[node_no]), inorder)
    _add_inorder(inorder, node_no)
    _inorder_helper(nodes, get_right_child(nodes[node_no]), inorder)

def _inorder_base_case(node_no):
    return node_no is None

def _add_inorder(inorder, node_no):
    inorder.append(node_no)

def preorder_tree_walk(nodes, node_no, preorder):
    _preorder_helper(nodes, node_no, preorder)

def _preorder_helper(nodes, node_no, preorder):
    if _preorder_base_case(node_no):
        return
    _add_preorder(preorder, node_no)
    _preorder_helper(nodes, get_left_child(nodes[node_no]), preorder)
    _preorder_helper(nodes, get_right_child(nodes[node_no]), preorder)

def _preorder_base_case(node_no):
    return node_no is None

def _add_preorder(preorder, node_no):
    preorder.append(node_no)

def find(nodes, tgt_node_no):
    return _find_helper(nodes, tgt_node_no)

def _find_helper(nodes, tgt_node_no):
    cur_node_no = root_node_no
    while not _find_while_stop(cur_node_no):
        cur_node = nodes[cur_node_no]
        if _find_key_match(cur_node, tgt_node_no):
            return True
        elif _find_go_left(tgt_node_no, cur_node):
            cur_node_no = get_left_child(cur_node)
        else:
            cur_node_no = get_right_child(cur_node)
    return False

def _find_while_stop(cur_node_no):
    return cur_node_no is None

def _find_key_match(cur_node, tgt_node_no):
    return cur_node.key == tgt_node_no

def _find_go_left(tgt_node_no, cur_node):
    return tgt_node_no < cur_node.key

def switch_child_of_parent(nodes: dict, del_node: Node, switch_node_no):
    _switch_child(nodes, del_node, switch_node_no)

def _switch_child(nodes, del_node, switch_node_no):
    if _check_is_left_child(nodes, del_node):
        set_left_child(nodes[get_parent(del_node)], switch_node_no)
    elif _check_is_right_child(nodes, del_node):
        set_right_child(nodes[get_parent(del_node)], switch_node_no)

def _check_is_left_child(nodes, del_node):
    parent_node = nodes[get_parent(del_node)]
    return parent_node.left == del_node.key

def _check_is_right_child(nodes, del_node):
    parent_node = nodes[get_parent(del_node)]
    return parent_node.right == del_node.key

def delete_node(nodes: dict, delete_node_no: int):
    del_node = _get_delete_node(nodes, delete_node_no)
    if _delete_is_leaf(del_node):
        _delete_leaf(nodes, del_node)
    elif not _delete_has_two_child(del_node):
        _delete_one_child(nodes, del_node)
    else:
        _delete_two_child(nodes, del_node)
    _delete_node_from_dict(nodes, delete_node_no)

def _get_delete_node(nodes, delete_node_no):
    return nodes[delete_node_no]

def _delete_is_leaf(del_node):
    return del_node.is_leaf()

def _delete_has_two_child(del_node):
    return del_node.has_two_child()

def _delete_leaf(nodes, del_node):
    switch_child_of_parent(nodes, del_node, None)

def _delete_one_child(nodes, del_node):
    child = del_node.has_one_child()
    switch_child_of_parent(nodes, del_node, child)
    set_parent(nodes[child], del_node.parent)

def _delete_two_child(nodes, del_node):
    inorder = []
    inorder_tree_walk(nodes, del_node.right, inorder)
    swap_node = Node(inorder[0])
    switch_child_of_parent(nodes, del_node, swap_node.key)
    _relink_swap_node(nodes, swap_node, del_node)
    _relink_left_parent(nodes, swap_node)
    _relink_right_if_needed(nodes, swap_node, del_node)
    delete_node(nodes, swap_node.key)
    nodes[swap_node.key] = swap_node

def _relink_swap_node(nodes, swap_node, del_node):
    set_parent(swap_node, del_node.parent)
    set_left_child(swap_node, del_node.left)

def _relink_left_parent(nodes, swap_node):
    set_parent(nodes[swap_node.left], swap_node.key)

def _relink_right_if_needed(nodes, swap_node, del_node):
    if _swap_key_is_right(del_node, swap_node):
        set_right_child(swap_node, None)
    else:
        set_right_child(swap_node, del_node.right)
        set_parent(nodes[swap_node.right], swap_node.key)

def _swap_key_is_right(del_node, swap_node):
    return swap_node.key == del_node.right

def _delete_node_from_dict(nodes, delete_node_no):
    del nodes[delete_node_no]

def main():
    num_com = _get_num_commands()
    commands = _get_commands()
    nodes = _init_nodes()
    _process_commands(num_com, commands, nodes)

def _get_num_commands():
    return int(input())

def _get_commands():
    return sys.stdin.readlines()

def _init_nodes():
    return {}

def _process_commands(num_com, commands, nodes):
    for i in range(num_com):
        _process_single_command(commands[i], nodes)

def _process_single_command(command, nodes):
    if _is_insert_command(command):
        _handle_insert(command, nodes)
    elif _is_print_command(command):
        _handle_print(nodes)
    elif _is_find_command(command):
        _handle_find(command, nodes)
    elif _is_delete_command(command):
        _handle_delete(command, nodes)

def _is_insert_command(command):
    return command[0] == 'i'

def _is_print_command(command):
    return command[0] == 'p'

def _is_find_command(command):
    return command[0] == 'f'

def _is_delete_command(command):
    return command[0] == 'd'

def _get_insert_key(command):
    return int(command[7:])

def _get_find_key(command):
    return int(command[5:])

def _get_delete_key(command):
    return int(command[7:])

def _handle_insert(command, nodes):
    insert(nodes, Node(_get_insert_key(command)))

def _handle_print(nodes):
    _handle_inorder_print(nodes)
    _handle_preorder_print(nodes)

def _handle_inorder_print(nodes):
    inorder = []
    inorder_tree_walk(nodes, root_node_no, inorder)
    print(" " + " ".join(map(str, inorder)))

def _handle_preorder_print(nodes):
    preorder = []
    preorder_tree_walk(nodes, root_node_no, preorder)
    print(" " + " ".join(map(str, preorder)))

def _handle_find(command, nodes):
    if find(nodes, _get_find_key(command)):
        print('yes')
    else:
        print('no')

def _handle_delete(command, nodes):
    delete_node(nodes, _get_delete_key(command))

main()