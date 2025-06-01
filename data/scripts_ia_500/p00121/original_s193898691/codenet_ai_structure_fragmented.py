D = {}
R = range(8)

def condition_i_0(p):
    return p % 4 < 3

def condition_i_1(p):
    return p % 4 > 0

def condition_i_2(p):
    return p < 4

def condition_i_3(p):
    return p > 3

def get_dp_for_i_0(p):
    if condition_i_0(p):
        return 1
    return 0

def get_dp_for_i_1(p):
    if condition_i_1(p):
        return -1
    return 0

def get_dp_for_i_2(p):
    if condition_i_2(p):
        return 4
    return 0

def get_dp_for_i_3(p):
    if condition_i_3(p):
        return -4
    return 0

def f1(i, p):
    if i == 0:
        return get_dp_for_i_0(p)
    elif i == 1:
        return get_dp_for_i_1(p)
    elif i == 2:
        return get_dp_for_i_2(p)
    elif i == 3:
        return get_dp_for_i_3(p)
    else:
        return 0

def get_initial_state():
    return list(R)

def get_index_of_zero(state):
    return state.index(0)

def swap_positions(state, p1, p2):
    new_state = state[:]
    new_state[p1], new_state[p2] = new_state[p2], new_state[p1]
    return new_state

def state_to_tuple(state):
    return tuple(state)

def should_continue(dp):
    return dp == 0

def is_state_known(state_tuple):
    return state_tuple in D

def add_state_to_search(sp, state):
    sp.append(state)

def record_state(state_tuple, cost):
    D[state_tuple] = cost

def pop_state_from_search(sp):
    return sp.pop(0)

def get_cost_of_state(state_tuple):
    return D[state_tuple]

def initialize_D():
    global D
    D = { tuple(R): 0 }

def initialize_search_path():
    return [ get_initial_state() ]

def process_state(sp):
    while sp:
        state = pop_state_from_search(sp)
        cost = get_cost_of_state(state_to_tuple(state))
        zero_pos = get_index_of_zero(state)
        process_moves(state, cost, zero_pos, sp)

def process_moves(state, cost, zero_pos, sp):
    for i in range(4):
        dp = f1(i, zero_pos)
        if should_continue(dp):
            continue
        new_state = swap_positions(state, zero_pos, zero_pos + dp)
        new_state_tuple = state_to_tuple(new_state)
        if is_state_known(new_state_tuple):
            continue
        add_state_to_search(sp, new_state)
        record_state(new_state_tuple, cost + 1)

def f():
    initialize_D()
    sp = initialize_search_path()
    process_state(sp)

import sys

def read_input_line(line):
    return list(map(int, line.split()))

def main():
    f()
    for line in sys.stdin:
        state = read_input_line(line)
        print(get_cost_of_state(state_to_tuple(state)))

main()