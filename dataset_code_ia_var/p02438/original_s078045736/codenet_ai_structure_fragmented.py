import collections

def create_deque():
    return collections.deque()

def create_deques(num_lists):
    return [create_deque() for _ in range(num_lists)]

def format_deque(dq):
    return ' '.join(map(str, dq))

def print_deque(deque_to_print):
    print(format_deque(deque_to_print))

def is_non_empty(deque_obj):
    return bool(deque_obj)

def deque_length_one(deque_obj):
    return len(deque_obj) == 1

def append_to_deque(dq, value):
    dq.append(value)

def appendleft_to_deque(dq, value):
    dq.appendleft(value)

def extend_deque(target, source):
    target.extend(source)

def set_deque(lists, index, dq):
    lists[index] = dq

def reset_deque(lists, index):
    lists[index] = create_deque()

class Splice:
    def __init__(self, num_lists):
        self.lists = create_deques(num_lists)

    def insert(self, t, x):
        self._insert_element(t, x)
        return self

    def _insert_element(self, t, x):
        append_to_deque(self.lists[t], x)

    def dump(self, t):
        self._dump_list(t)

    def _dump_list(self, t):
        print_deque(self.lists[t])

    def splice(self, s, t):
        self._splice_lists(s, t)
        return self

    def _splice_lists(self, s, t):
        if is_non_empty(self.lists[t]):
            self._handle_non_empty_target(s, t)
        else:
            self._set_target_to_source(s, t)
        reset_deque(self.lists, s)

    def _handle_non_empty_target(self, s, t):
        if deque_length_one(self.lists[s]):
            self._append_single_source_to_target(s, t)
        elif deque_length_one(self.lists[t]):
            self._merge_single_target_with_source(s, t)
        else:
            self._extend_target_with_source(s, t)

    def _append_single_source_to_target(self, s, t):
        append_to_deque(self.lists[t], self.lists[s][0])

    def _merge_single_target_with_source(self, s, t):
        appendleft_to_deque(self.lists[s], self.lists[t][0])
        set_deque(self.lists, t, self.lists[s])

    def _extend_target_with_source(self, s, t):
        extend_deque(self.lists[t], self.lists[s])

    def _set_target_to_source(self, s, t):
        set_deque(self.lists, t, self.lists[s])

def parse_initial_input():
    return tuple(map(int, input().split(' ')))

def parse_operation():
    return tuple(map(int, input().split(' ')))

def execute_operation(lists, op):
    if op[0] == 0:
        _op_insert(lists, op)
    elif op[0] == 1:
        _op_dump(lists, op)
    elif op[0] == 2:
        _op_splice(lists, op)

def _op_insert(lists, op):
    lists.insert(op[1], op[2])

def _op_dump(lists, op):
    lists.dump(op[1])

def _op_splice(lists, op):
    lists.splice(op[1], op[2])

def main():
    num_lists, num_op = parse_initial_input()
    lists = Splice(num_lists)
    for _ in range(num_op):
        op = parse_operation()
        execute_operation(lists, op)

main()