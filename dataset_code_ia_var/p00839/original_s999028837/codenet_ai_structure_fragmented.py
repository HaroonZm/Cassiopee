def read_exchange(file_input, y):
    exch1 = []
    exch2 = []
    exch3 = []
    for _ in range(y):
        p, P, space, q, Q = file_input.readline().rstrip()
        p = int(p)
        q = int(q)
        classify_exchange(p, P, q, Q, exch1, exch2, exch3)
    return exch1, exch2, exch3

def classify_exchange(p, P, q, Q, exch1, exch2, exch3):
    if P == 'E':
        if Q == 'W':
            exch1.append((p, q))
        else:
            exch2.append((p, q))
    else:
        if Q == 'E':
            exch1.append((q, p))
        else:
            exch3.append((q, p))

def read_initial_state(file_input, x):
    init = []
    for _ in range(x):
        s = file_input.readline().rstrip()
        init.append('' if s == '-' else s)
    return init

def build_state_record(init):
    key = '|'.join(init)
    return {key: 0}

def build_state_list(init):
    return [init]

def read_all_initials(file_input, x):
    fwd_init = read_initial_state(file_input, x)
    fwd_rec = build_state_record(fwd_init)
    forwrad = build_state_list(fwd_init)
    bk_init = read_initial_state(file_input, x)
    bk_rec = build_state_record(bk_init)
    backward = build_state_list(bk_init)
    return fwd_init, fwd_rec, forwrad, bk_init, bk_rec, backward

def do_exchange(trains, exch, mode):
    for l1, l2 in exch:
        tmp_trains = trains[:]
        coupled = get_coupled(trains, l1, l2, mode)
        for i in range(len(coupled) + 1):
            update_trains(tmp_trains, coupled, i, l1, l2, mode)
            yield tmp_trains[:]

def get_coupled(trains, l1, l2, mode):
    if mode == 1:
        return trains[l1] + trains[l2]
    elif mode == 2:
        return trains[l1] + trains[l2][::-1]
    elif mode == 3:
        return trains[l1][::-1] + trains[l2]

def update_trains(tmp_trains, coupled, i, l1, l2, mode):
    if mode == 1:
        tmp_trains[l1] = coupled[:i]
        tmp_trains[l2] = coupled[i:]
    elif mode == 2:
        tmp_trains[l1] = coupled[:i]
        tmp_trains[l2] = coupled[i:][::-1]
    elif mode == 3:
        tmp_trains[l1] = coupled[:i][::-1]
        tmp_trains[l2] = coupled[i:]

def trains_to_key(trains):
    return '|'.join(trains)

def expand_states(current_states, exch1, exch2, exch3, rec, op_rec, step, forward=True):
    new_states = []
    conflict = find_conflict(current_states, exch1, exch2, exch3, rec, op_rec, step, new_states, forward)
    if conflict is not None:
        return conflict, []
    return None, new_states

def find_conflict(current_states, exch1, exch2, exch3, rec, op_rec, step, new_states, forward):
    for trains in current_states:
        for new_trains in do_exchange(trains, exch1, 1):
            key = trains_to_key(new_trains)
            if add_new_state(key, rec, op_rec, step, new_trains, new_states):
                return resolve_conflict(key, rec, op_rec, step, forward)
        for new_trains in do_exchange(trains, exch2, 2):
            key = trains_to_key(new_trains)
            if add_new_state(key, rec, op_rec, step, new_trains, new_states):
                return resolve_conflict(key, rec, op_rec, step, forward)
        for new_trains in do_exchange(trains, exch3, 3):
            key = trains_to_key(new_trains)
            if add_new_state(key, rec, op_rec, step, new_trains, new_states):
                return resolve_conflict(key, rec, op_rec, step, forward)
    return None

def add_new_state(key, rec, op_rec, step, new_trains, new_states):
    if key not in rec:
        if key in op_rec:
            return True
        rec[key] = step
        new_states.append(new_trains[:])
    return False

def resolve_conflict(key, rec, op_rec, step, forward):
    if forward:
        return op_rec[key] + step
    else:
        return rec[key] + step

def perform_steps(forwrad, backward, exch1, exch2, exch3, fwd_rec, bk_rec):
    for step in range(1, 4):
        result, tmp_forward = expand_states(forwrad, exch1, exch2, exch3, fwd_rec, bk_rec, step, True)
        if result is not None:
            return result
        forwrad = tmp_forward
        if step == 3:
            return 6
        result, tmp_backward = expand_states(backward, exch1, exch2, exch3, bk_rec, fwd_rec, step, False)
        if result is not None:
            return result
        backward = tmp_backward
    return None

def solve(file_input, x, y):
    exch1, exch2, exch3 = read_exchange(file_input, y)
    fwd_init, fwd_rec, forwrad, bk_init, bk_rec, backward = read_all_initials(file_input, x)
    result = perform_steps(forwrad, backward, exch1, exch2, exch3, fwd_rec, bk_rec)
    return result

def read_line_and_parse(f_i):
    return map(int, f_i.readline().split())

def main_loop(f_i):
    while True:
        x, y = read_line_and_parse(f_i)
        if x == 0:
            break
        print(solve(f_i, x, y))

def main():
    from sys import stdin
    f_i = stdin
    main_loop(f_i)

main()