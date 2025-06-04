from typing import List

class Node:
    __slots__ = ['prev', 'next', 'data']

    def __init__(self, prev, next, data) -> None:
        self.prev = prev
        self.next = next
        self.data = data

def create_node(prev, next, data) -> Node:
    return Node(prev, next, data)

def link_nodes(prev: Node, next: Node):
    prev.next = next
    next.prev = prev

def set_prev(node: Node, prev: Node):
    node.prev = prev

def set_next(node: Node, next: Node):
    node.next = next

def set_data(node: Node, data):
    node.data = data

def assign_cur(new_node: Node) -> Node:
    return new_node

def insert_value(x: int, cur: Node) -> Node:
    prev_node = get_prev(cur)
    new_node = create_node(prev_node, cur, x)
    set_next(prev_node, new_node)
    set_prev(cur, new_node)
    return assign_cur(new_node)

def get_prev(cur: Node) -> Node:
    return cur.prev

def get_next(cur: Node) -> Node:
    return cur.next

def move_right(cur: Node, steps: int) -> Node:
    for _ in range(steps):
        cur = get_next(cur)
    return cur

def move_left(cur: Node, steps: int) -> Node:
    for _ in range(steps):
        cur = get_prev(cur)
    return cur

def move_pointer(x: int, cur: Node) -> Node:
    if x > 0:
        return move_right(cur, x)
    else:
        return move_left(cur, -x)

def erase_node(cur: Node) -> Node:
    next_node = get_next(cur)
    prev_node = get_prev(cur)
    set_next(prev_node, next_node)
    set_prev(next_node, prev_node)
    return assign_cur(next_node)

def read_int() -> int:
    return int(input())

def parse_input_line() -> List[int]:
    return list(map(int, input().split()))

def create_root() -> Node:
    return create_node(None, None, None)

def create_first_node(root: Node) -> Node:
    node = create_node(root, None, None)
    set_next(root, node)
    set_prev(node, root)
    return node

def process_query(op: int, value: List[int], cur: Node) -> Node:
    if op == 0:
        return insert_value(value[0], cur)
    elif op == 1:
        return move_pointer(value[0], cur)
    elif op == 2:
        return erase_node(cur)
    else:
        return cur

def traverse_and_collect(root: Node) -> List[int]:
    ans: List[int] = []
    it = get_next(root)
    while get_next(it):
        ans.append(it.data)
        it = get_next(it)
    return ans

def print_elements(elements: List[int]):
    for elem in elements:
        print(elem)

def main():
    num_query = read_int()
    root = create_root()
    cur = create_first_node(root)
    for _ in range(num_query):
        inputs = parse_input_line()
        op, *value = inputs[0], inputs[1:]
        cur = process_query(op, value, cur)
    elements = traverse_and_collect(root)
    print_elements(elements)

if __name__ == "__main__":
    main()