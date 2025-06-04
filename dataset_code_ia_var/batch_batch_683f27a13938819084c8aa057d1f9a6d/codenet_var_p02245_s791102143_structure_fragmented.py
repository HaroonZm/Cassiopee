import queue
from sys import stdin

def get_adjacent_positions():
    return (
        (1,3),     # 0
        (0,2,4),   # 1
        (1,5),     # 2
        (0,4,6),   # 3
        (1,3,5,7), # 4
        (2,4,8),   # 5
        (3,7),     # 6
        (4,6,8),   # 7
        (5,7)      # 8
    )

def create_state(board, space, prev):
    return State(board, space, prev)

def copy_board(board):
    return board[:]

def swap_with_space(board, space, i):
    new_board = copy_board(board)
    new_board[space] = new_board[i]
    new_board[i] = 0
    return new_board

def board_to_tuple(board):
    return tuple(board)

def is_in_table(table, key):
    return key in table

def add_to_table(table, key):
    table[key] = True

def get_end_board():
    return [1,2,3,4,5,6,7,8,0]

def is_end(board, end):
    return board == end

def find_zero(board):
    return board.index(0)

def put_in_queue(q, state):
    q.put(state)

def get_from_queue(q):
    return q.get()

def queue_empty(q):
    return q.empty()

def create_queue():
    return queue.Queue()

def initialize_table():
    return {}

def should_continue():
    return True

def increment_count(count_ref):
    count_ref[0] += 1

def recursive_print_ans(state, count_ref):
    if state is not None:
        increment_count(count_ref)
        recursive_print_ans(state.prev, count_ref)
    return count_ref[0]

def print_answer(state):
    count_ref = [-1]
    return recursive_print_ans(state, count_ref)

class State:
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev

def process_neighbors(a, adjacent, q, table, end):
    for i in get_adjacent_indices(adjacent, a.space):
        b = prepare_swapped_board(a, i)
        key = board_to_tuple(b)
        if is_in_table(table, key):
            continue
        c = create_state(b, i, a)
        if is_end(b, end):
            return print_answer(c)
        put_in_queue(q, c)
        add_to_table(table, key)
    return None

def get_adjacent_indices(adjacent, space):
    return adjacent[space]

def prepare_swapped_board(a, i):
    return swap_with_space(a.board, a.space, i)

def manage_queue(q, table, end, adjacent):
    while not queue_empty(q):
        a = get_from_queue(q)
        result = process_neighbors(a, adjacent, q, table, end)
        if result is not None:
            return result
    return None

def bf_search(start, end):
    adjacent = get_adjacent_positions()
    q = create_queue()
    space = find_zero(start)
    initial_state = create_state(start, space, None)
    put_in_queue(q, initial_state)
    table = initialize_table()
    add_to_table(table, board_to_tuple(start))
    result = manage_queue(q, table, end, adjacent)
    return result

def read_start():
    return [ int(n) for _ in range(3) for n in stdin.readline().split() ]

def main():
    start = read_start()
    end = get_end_board()
    if is_end(start, end):
        print(0)
    else:
        print(bf_search(start, end))

if __name__ == "__main__":
    main()