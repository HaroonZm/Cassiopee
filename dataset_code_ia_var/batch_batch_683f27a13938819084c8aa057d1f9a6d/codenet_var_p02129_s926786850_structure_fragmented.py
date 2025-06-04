def read_input():
    N = int(input())
    moves = []
    for _ in range(N):
        moves.append(list(map(int, input().split())))
    return N, moves

def get_state_changes(init, A):
    state = init[:]
    for a in A:
        state = process_move(state, a)
    return state

def process_move(state, a):
    if a:
        return swap_1_2(state)
    else:
        return swap_0_1(state)
    
def swap_1_2(state):
    s = state[:]
    s[1], s[2] = s[2], s[1]
    return s

def swap_0_1(state):
    s = state[:]
    s[0], s[1] = s[1], s[0]
    return s

def get_state_index(S, state):
    for i, s in enumerate(S):
        if s == state:
            return i
    return -1

def check_counts_and_store(j, C, L, P, state):
    C[j] += 1
    if C[j] >= L[j]:
        early_yes_exit()
    P.append(state)

def early_yes_exit():
    print('yes')
    exit(0)

def early_no_exit():
    print('no')
    exit(0)

def apply_permutation_order(P, init):
    from itertools import permutations
    all_perms = get_all_permutations(P)
    for perm in all_perms:
        if apply_moves_sequence(init[:], perm):
            early_yes_exit()
    early_no_exit()

def get_all_permutations(P):
    from itertools import permutations
    return permutations(P)

def apply_moves_sequence(state, sequence):
    for move in sequence:
        state = apply_single_move_list(state, move)
    return is_final_state(state)

def apply_single_move_list(state, move):
    return [state[move[0]], state[move[1]], state[move[2]]]

def is_final_state(state):
    return state == [0, 1, 2]

def main():
    N, moves = read_input()
    C = [0] * 6
    S = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    L = [1, 2, 2, 3, 3, 2]
    P = []
    init = [0, 1, 2]
    for move in moves:
        w, *A = move
        state = get_state_changes(init, A)
        j = get_state_index(S, state)
        check_counts_and_store(j, C, L, P, state)
    apply_permutation_order(P, init)

main()