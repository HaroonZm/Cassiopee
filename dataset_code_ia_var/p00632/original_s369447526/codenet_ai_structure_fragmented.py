bignum = 1000000000000

def get_directions():
    return [[1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]]

def direction_down():
    return get_directions()[0]

def direction_up():
    return get_directions()[1]

def direction_right():
    return get_directions()[2]

def direction_left():
    return get_directions()[3]

def direction_stay():
    return get_directions()[4]

def is_within_bounds(x, y, H, W):
    return 0 <= x < H and 0 <= y < W

def is_movable(loc, d, H, W):
    return is_within_bounds(loc[0] + d[0], loc[1] + d[1], H, W)

def vec_sum(loc, d):
    return [loc[0] + d[0], loc[1] + d[1]]

def decode_ghost_command(cn):
    if cn == 5:
        return direction_stay()
    if cn == 2:
        return direction_down()
    if cn == 4:
        return direction_left()
    if cn == 6:
        return direction_right()
    if cn == 8:
        return direction_up()
    raise ValueError("Unknown ghost command: {}".format(cn))

def read_dimensions():
    return map(int, raw_input().split())

def init_grid_and_locations(H, W):
    L = []
    F = [[bignum for i in range(W)] for j in range(H)]
    Aloc = [0, 0]
    Bloc = [0, 0]
    for h in range(H):
        row = raw_input()
        L.append(row)
        set_start_if_found(L, h, row, 'A', Aloc)
        set_start_if_found(L, h, row, 'B', Bloc)
    update_square(F, Aloc, 0)
    return L, F, Aloc, Bloc

def set_start_if_found(L, h, row, char, loc):
    idx = row.find(char)
    if idx != -1:
        loc[0] = h
        loc[1] = idx

def update_square(F, loc, ac):
    F[loc[0]][loc[1]] = ac

def get_neighbors(loc, H, W):
    dirs = get_directions()
    neighbors = []
    for d in dirs:
        if is_movable(loc, d, H, W):
            neighbors.append(vec_sum(loc, d))
    return neighbors

def bfs(L, F, Aloc, H, W):
    nf = [Aloc[:]]
    ac = 1
    while len(nf) > 0:
        nnf = []
        for loc in nf:
            propagate_neighbors(L, F, loc, H, W, ac, nnf)
        nf = nnf[:]
        ac += 1

def propagate_neighbors(L, F, loc, H, W, ac, nnf):
    dirs = get_directions()
    for d in dirs:
        process_neighbor(L, F, loc, d, H, W, ac, nnf)

def process_neighbor(L, F, loc, d, H, W, ac, nnf):
    if is_movable(loc, d, H, W):
        v = vec_sum(loc, d)
        if can_visit_cell(L, F, v, ac):
            update_square(F, v, ac)
            nnf.append(v)

def can_visit_cell(L, F, v, ac):
    row, col = v
    return F[row][col] > ac and L[row][col] != '#'

def read_commands():
    return raw_input()

def initialize_command_visited(cmd, H, W):
    return [[[0 for i in range(W)] for j in range(H)] for k in range(len(cmd))]

def command_cycle_length(cmd):
    return len(cmd)

def print_impossible():
    print 'impossible'

def print_result(ans, Bloc):
    print ans, ' '.join(str(b) for b in Bloc)

def reached_before(C, cm, Bloc, H, W, ans):
    return C[cm][Bloc[0]][Bloc[1]] == 1 and ans > H * W

def mark_visited(C, cm, Bloc):
    C[cm][Bloc[0]][Bloc[1]] = 1

def parse_command_char(cmd, cm):
    return int(cmd[cm])

def try_move_bloc(Bloc, d, H, W):
    if is_movable(Bloc, d, H, W):
        Bloc[:] = vec_sum(Bloc, d)
    return Bloc

def found_A(F, Bloc, ans):
    return F[Bloc[0]][Bloc[1]] <= ans

def update_command_index(cm, cmd):
    cm += 1
    if cm >= len(cmd):
        cm = 0
    return cm

def advance_turn(ans):
    return ans + 1

def main_loop():
    while True:
        params = list(read_dimensions())
        H = params[0]
        if H == 0:
            break
        W = params[1]
        L, F, Aloc, Bloc = init_grid_and_locations(H, W)
        bfs(L, F, Aloc, H, W)
        cmd = read_commands()
        C = initialize_command_visited(cmd, H, W)
        cm = 0
        ans = 1
        while True:
            if reached_before(C, cm, Bloc, H, W, ans):
                print_impossible()
                break
            mark_visited(C, cm, Bloc)
            cn = parse_command_char(cmd, cm)
            d = decode_ghost_command(cn)
            Bloc = try_move_bloc(Bloc, d, H, W)
            if found_A(F, Bloc, ans):
                print_result(ans, Bloc)
                break
            cm = update_command_index(cm, cmd)
            ans = advance_turn(ans)

main_loop()