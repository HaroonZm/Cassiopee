class List:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def insert(self, value):
        node = self._create_node(value)
        self._setup_prev_and_next(node)
        self._update_previous_node_next(node)
        self._set_prev(node)
        return node

    def _create_node(self, value):
        return self.__class__(value)

    def _setup_prev_and_next(self, node):
        node.prev, node.next = self.prev, self

    def _update_previous_node_next(self, node):
        if self.prev is not None:
            self.prev.next = node

    def _set_prev(self, node):
        self.prev = node

    def delete(self):
        p, n = self._get_prev_and_next()
        self._detach()
        self._relink_neighbors(p, n)
        return n

    def _get_prev_and_next(self):
        return self.prev, self.next

    def _detach(self):
        self.prev, self.next = None, None

    def _relink_neighbors(self, p, n):
        if p is None:
            self._set_n_prev_none(n)
        else:
            self._link_prev_and_next(p, n)

    def _set_n_prev_none(self, n):
        n.prev = None

    def _link_prev_and_next(self, p, n):
        n.prev, p.next = p, n

    def move(self, i):
        return self._move_node(i)

    def _move_node(self, i):
        node = self
        if i > 0:
            node = self._move_forward(node, i)
        else:
            node = self._move_backward(node, -i)
        return node

    def _move_forward(self, node, steps):
        for _ in range(steps):
            node = node.next
        return node

    def _move_backward(self, node, steps):
        for _ in range(steps):
            node = node.prev
        return node

    def __iter__(self):
        return self._get_iterator()

    def _get_iterator(self):
        return List.ListIterator(self)

    class ListIterator:
        def __init__(self, node):
            self.node = self._move_to_head(node)

        def _move_to_head(self, node):
            while node.prev is not None:
                node = node.prev
            return node

        def __iter__(self):
            return self

        def __next__(self):
            return self._get_next_value()

        def _get_next_value(self):
            val = self._get_node_value()
            if self._is_end(val):
                raise StopIteration
            self._advance()
            return val

        def _get_node_value(self):
            return self.node.value

        def _is_end(self, val):
            return val is None

        def _advance(self):
            self.node = self.node.next

def run():
    n = _get_input_as_int()
    li = _create_empty_list()
    _execute_commands(n, li)

def _get_input_as_int():
    return int(input())

def _create_empty_list():
    return List()

def _execute_commands(n, li):
    for _ in range(n):
        command = _get_command_input()
        li = _process_command(command, li)
    _print_list_values(li)

def _get_command_input():
    return input()

def _process_command(command, li):
    if _is_insert_command(command):
        return _handle_insert_command(command, li)
    elif _is_move_command(command):
        return _handle_move_command(command, li)
    elif _is_delete_command(command):
        return _handle_delete_command(li)
    else:
        _raise_invalid_command_exception()

def _is_insert_command(command):
    return command.startswith('0')

def _is_move_command(command):
    return command.startswith('1')

def _is_delete_command(command):
    return command.startswith('2')

def _handle_insert_command(command, li):
    value = _parse_int_from_command(command)
    return li.insert(value)

def _handle_move_command(command, li):
    move_value = _parse_int_from_command(command)
    return li.move(move_value)

def _handle_delete_command(li):
    return li.delete()

def _parse_int_from_command(command):
    return int(command[2:])

def _raise_invalid_command_exception():
    raise ValueError('invalid command')

def _print_list_values(li):
    for v in li:
        _print_value(v)

def _print_value(v):
    print(v)

if __name__ == '__main__':
    run()