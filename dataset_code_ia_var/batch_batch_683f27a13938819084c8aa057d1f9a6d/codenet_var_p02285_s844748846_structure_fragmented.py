class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def delete_connect(self, parent, child):
        self._connect_parent_to_child(parent, child)
        self._set_child_parent(child, parent)
    
    def _connect_parent_to_child(self, parent, child):
        if parent:
            if self._parent_goes_left(parent):
                parent.left = child
            else:
                parent.right = child

    def _parent_goes_left(self, parent):
        return parent.val > self.val

    def _set_child_parent(self, child, parent):
        if child:
            child.parent = parent

    def delete(self):
        left, right = self._get_left(), self._get_right()
        if self._no_children(left, right):
            self._do_delete_leaf()
        elif self._only_right_child(left, right):
            self._do_delete_right()
        elif self._only_left_child(left, right):
            self._do_delete_left()
        else:
            self._do_delete_both()

    def _no_children(self, left, right):
        return not left and not right

    def _only_right_child(self, left, right):
        return not left and right

    def _only_left_child(self, left, right):
        return left and not right

    def _do_delete_leaf(self):
        self.delete_connect(self.parent, None)

    def _do_delete_right(self):
        self.delete_connect(self.parent, self.right)

    def _do_delete_left(self):
        self.delete_connect(self.parent, self.left)

    def _do_delete_both(self):
        next_node = self._get_successor()
        self._replace_value(next_node)
        next_node.delete()

    def _get_successor(self):
        return self.right.get_leftmost()

    def _replace_value(self, successor):
        self.val = successor.val

    def _get_left(self):
        return self.left

    def _get_right(self):
        return self.right

    def get_leftmost(self):
        return self._recursive_leftmost()

    def _recursive_leftmost(self):
        if self.left:
            return self.left.get_leftmost()
        return self


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, node: Node):
        if self._need_new_root():
            self._set_new_root(node)
            return
        self._walk_and_insert(node)

    def _need_new_root(self):
        return not self.root

    def _set_new_root(self, node):
        self.root = node

    def _walk_and_insert(self, node):
        cur = self.root
        while True:
            direction = self._choose_direction(node, cur)
            if self._can_move(direction, cur):
                cur = self._move(direction, cur)
                continue
            else:
                self._insert_at_direction(direction, cur, node)
                node.parent = cur
                return

    def _choose_direction(self, node, cur):
        return "right" if node.val > cur.val else "left"

    def _can_move(self, direction, cur):
        return (direction == "right" and cur.right) or (direction == "left" and cur.left)

    def _move(self, direction, cur):
        return cur.right if direction == "right" else cur.left

    def _insert_at_direction(self, direction, cur, node):
        if direction == "right":
            cur.right = node
        else:
            cur.left = node

    def find(self, val):
        return self._find_value(val)

    def _find_value(self, val):
        cur = self.root
        while cur:
            if self._is_equal(cur, val):
                return self._found_yes()
            cur = self._choose_next(cur, val)
        return self._found_no()

    def _is_equal(self, cur, val):
        return cur.val == val

    def _found_yes(self):
        return "yes"

    def _found_no(self):
        return "no"

    def _choose_next(self, cur, val):
        return cur.left if cur.val > val else cur.right

    def find_node(self, val):
        return self._find_node_with_val(val)

    def _find_node_with_val(self, val):
        cur = self.root
        while cur:
            if self._is_equal(cur, val):
                return cur
            cur = self._choose_next(cur, val)
        return None

    def delete(self, val):
        node = self.find_node(val)
        if self._can_delete(node):
            node.delete()

    def _can_delete(self, node):
        return node is not None


def preorder_walk(node, preorder):
    _preorder_walk_recursive(node, preorder)

def _preorder_walk_recursive(node, preorder):
    if not node:
        return
    _preorder_visit(node, preorder)
    _preorder_if_left(node, preorder)
    _preorder_if_right(node, preorder)

def _preorder_visit(node, preorder):
    preorder.append(str(node.val))

def _preorder_if_left(node, preorder):
    if node.left:
        _preorder_walk_recursive(node.left, preorder)

def _preorder_if_right(node, preorder):
    if node.right:
        _preorder_walk_recursive(node.right, preorder)

def inorder_walk(node, inorder):
    _inorder_walk_recursive(node, inorder)

def _inorder_walk_recursive(node, inorder):
    if not node:
        return
    _inorder_if_left(node, inorder)
    _inorder_visit(node, inorder)
    _inorder_if_right(node, inorder)

def _inorder_if_left(node, inorder):
    if node.left:
        _inorder_walk_recursive(node.left, inorder)

def _inorder_visit(node, inorder):
    inorder.append(str(node.val))

def _inorder_if_right(node, inorder):
    if node.right:
        _inorder_walk_recursive(node.right, inorder)

def do_insert(bst, op):
    node = make_node_from_op(op)
    bst.insert(node)

def make_node_from_op(op):
    return Node(int(op[1]))

def do_print(bst):
    preorder, inorder = [], []
    print_results(bst, preorder, inorder)

def print_results(bst, preorder, inorder):
    _compute_traversals(bst.root, preorder, inorder)
    _print_inorder(inorder)
    _print_preorder(preorder)

def _compute_traversals(root, preorder, inorder):
    preorder_walk(root, preorder)
    inorder_walk(root, inorder)

def _print_inorder(inorder):
    print("", " ".join(inorder))

def _print_preorder(preorder):
    print("", " ".join(preorder))

def do_find(bst, op):
    print(_find_value_in_bst(bst, op))

def _find_value_in_bst(bst, op):
    val = int(op[1])
    return bst.find(val)

def do_delete(bst, op):
    val = int(op[1])
    bst.delete(val)

def handle_command(bst, op):
    cmd = op[0]
    if cmd == "insert":
        do_insert(bst, op)
    elif cmd == "print":
        do_print(bst)
    elif cmd == "find":
        do_find(bst, op)
    elif cmd == "delete":
        do_delete(bst, op)

def get_n():
    return int(input())

def get_op():
    return input().strip().split()

def handle_all_ops(bst, n):
    for _ in range(n):
        op = get_op()
        handle_command(bst, op)

def main():
    n = get_n()
    bst = BinarySearchTree()
    handle_all_ops(bst, n)

if __name__ == "__main__":
    main()