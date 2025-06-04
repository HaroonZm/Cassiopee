class Node(object):
    root = None

    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None

    @classmethod
    def insert(cls, z):
        y = cls._find_insert_parent(z)
        cls._link_parent_child(y, z)

    @classmethod
    def _find_insert_parent(cls, z):
        y = None
        x = cls.root
        while cls._node_exists(x):
            y = x
            if cls._is_left_child(z, x):
                x = x.left
            else:
                x = x.right
        z.parent = y
        return y

    @staticmethod
    def _node_exists(x):
        return x is not None

    @staticmethod
    def _is_left_child(z, x):
        return z.key < x.key

    @classmethod
    def _link_parent_child(cls, y, z):
        if cls._is_root(y):
            cls.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    @staticmethod
    def _is_root(y):
        return y is None

    @classmethod
    def find(cls, k):
        x = cls.root
        return cls._iterate_find(x, k)

    @classmethod
    def _iterate_find(cls, x, k):
        while cls._continue_find(x, k):
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    @staticmethod
    def _continue_find(x, k):
        return x is not None and k != x.key

    @classmethod
    def walk_preorder(cls, node):
        cls._visit_preorder(node)

    @classmethod
    def _visit_preorder(cls, node):
        cls._print_node_key(node)
        if node.left is not None:
            cls._visit_preorder(node.left)
        if node.right is not None:
            cls._visit_preorder(node.right)

    @staticmethod
    def _print_node_key(node):
        print(' {0}'.format(node.key), end='')

    @classmethod
    def walk_inorder(cls, node):
        cls._visit_inorder(node)

    @classmethod
    def _visit_inorder(cls, node):
        if node.left is not None:
            cls._visit_inorder(node.left)
        cls._print_node_key(node)
        if node.right is not None:
            cls._visit_inorder(node.right)

    @classmethod
    def delete_node(cls, z):
        y = cls._get_node_to_delete(z)
        x = cls._get_child_for_relink(y)
        cls._relink_parent_child(y, x)
        if y != z:
            cls._replace_key(z, y)

    @classmethod
    def _get_node_to_delete(cls, z):
        if cls._has_single_child(z):
            return z
        else:
            return Node.get_successor(z)

    @staticmethod
    def _has_single_child(z):
        return z.left is None or z.right is None

    @classmethod
    def _get_child_for_relink(cls, y):
        if y.left is not None:
            return y.left
        else:
            return y.right

    @classmethod
    def _relink_parent_child(cls, y, x):
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            Node.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

    @staticmethod
    def _replace_key(z, y):
        z.key = y.key

    @classmethod
    def get_successor(cls, x):
        if cls._has_right_child(x):
            return Node.get_minimum(x.right)
        else:
            return cls._find_successor_upwards(x)

    @staticmethod
    def _has_right_child(x):
        return x.right is not None

    @classmethod
    def _find_successor_upwards(cls, x):
        y = x.parent
        while cls._has_parent_and_is_right_child(x, y):
            x = y
            y = y.parent
        return y

    @staticmethod
    def _has_parent_and_is_right_child(x, y):
        return y is not None and x == y.right

    @classmethod
    def get_minimum(cls, x):
        while cls._has_left_child(x):
            x = x.left
        return x

    @staticmethod
    def _has_left_child(x):
        return x.left is not None

    def get_type(self):
        if self._is_node_root():
            return 'root'
        elif self._is_leaf():
            return 'leaf'
        else:
            return 'internal node'

    def _is_node_root(self):
        return self.parent is None

    def _is_leaf(self):
        return self.left is None and self.right is None

    def get_depth(self):
        if self._is_node_root():
            return 0
        else:
            return self._count_parents()

    def _count_parents(self):
        depth = 1
        t = self.parent
        while t.parent is not None:
            t = t.parent
            depth += 1
        return depth

    def get_height(self):
        if self._has_cached_height():
            return self.height
        self.height = self._calculate_height()
        return self.height

    def _has_cached_height(self):
        return self.height is not None

    def _calculate_height(self):
        h_left = self._get_left_height()
        h_right = self._get_right_height()
        return max(h_left, h_right)

    def _get_left_height(self):
        if self.left is not None:
            return self.left.get_height() + 1
        return 0

    def _get_right_height(self):
        if self.right is not None:
            return self.right.get_height() + 1
        return 0

    def get_degree(self):
        degree = 0
        if self.left is not None:
            degree += 1
        if self.right is not None:
            degree += 1
        return degree

    def get_sibling(self):
        if self._is_node_root():
            return -1
        p = self.parent
        if self._is_left_sibling(p):
            return p.left
        if self._is_right_sibling(p):
            return p.right

    def _is_left_sibling(self, p):
        return p.left != self and p.left is not None

    def _is_right_sibling(self, p):
        return p.right != self and p.right is not None

def process_node_data(node_data):
    for inst in node_data:
        _process_node_instruction(inst)

def _process_node_instruction(inst):
    if _is_print(inst):
        _do_print()
    elif _is_insert(inst):
        _do_insert(inst)
    elif _is_find(inst):
        _do_find(inst)
    elif _is_delete(inst):
        _do_delete(inst)

def _is_print(inst):
    return inst[0] == 'print'

def _is_insert(inst):
    return inst[0] == 'insert'

def _is_find(inst):
    return inst[0] == 'find'

def _is_delete(inst):
    return inst[0] == 'delete'

def _do_print():
    Node.walk_inorder(Node.root)
    print('')
    Node.walk_preorder(Node.root)
    print('')

def _do_insert(inst):
    node_key = int(inst[1])
    new_node = Node(node_key)
    Node.insert(new_node)

def _do_find(inst):
    result = Node.find(int(inst[1]))
    _print_find_result(result)

def _print_find_result(result):
    if result:
        print('yes')
    else:
        print('no')

def _do_delete(inst):
    key_to_delete = int(inst[1])
    result = Node.delete_node(Node.find(key_to_delete))

def flatten(l):
    import collections
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el

def _read_num_of_nodes():
    return int(input())

def _read_node_data(num_of_nodes):
    return [input().split(' ') for _ in range(num_of_nodes)]

def _main():
    num_of_nodes = _read_num_of_nodes()
    node_data = _read_node_data(num_of_nodes)
    process_node_data(node_data)

if __name__ == '__main__':
    _main()