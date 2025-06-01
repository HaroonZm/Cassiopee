class Node(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.left = None
        self.right = None
        self.initialize_children()

    def initialize_children(self):
        if self.is_terminal_condition():
            self.set_children_none()
        else:
            self.create_children()

    def is_terminal_condition(self):
        return (self.condition_one() or self.condition_two() or self.condition_three())

    def condition_one(self):
        return self.a <= 3 and self.b == 5

    def condition_two(self):
        return self.a == 5 and self.b <= 3

    def condition_three(self):
        return (self.a, self.b) in ((5, 5), (6, 4), (4, 6))

    def set_children_none(self):
        self.left = None
        self.right = None

    def create_children(self):
        self.left = Node(self.a + 1, self.b)
        self.right = Node(self.a, self.b + 1)

    def prints(self):
        self.print_coordinates()

    def print_coordinates(self):
        print "%d %d" % (self.a, self.b)


def parse(n, a, b, s):
    if is_target_node(n, a, b):
        print_path(s)
    else:
        if has_left_child(n):
            parse_left(n, a, b, s)
            parse_right(n, a, b, s)

def is_target_node(n, a, b):
    return n.a == a and n.b == b

def print_path(s):
    print s

def has_left_child(n):
    return n.left is not None

def parse_left(n, a, b, s):
    s1 = append_A(s)
    parse(n.left, a, b, s1)

def parse_right(n, a, b, s):
    s2 = append_B(s)
    parse(n.right, a, b, s2)

def append_A(s):
    return s + 'A'

def append_B(s):
    return s + 'B'


def read_input():
    return map(int, raw_input().split())

def main():
    read = read_input()
    n = create_root_node()
    st = create_empty_string()
    parse(n, read[0], read[1], st)

def create_root_node():
    return Node(0, 0)

def create_empty_string():
    return ""

main()