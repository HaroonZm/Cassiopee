def read_input():
    h, w = map(int, input().split())
    return h, w

def should_break(h):
    return not h

def set_decremented(h, w):
    return h - 1, w - 1

def initialize_mp():
    mp = {(0,2,"UU") : 1, (2,0,"RR") : 1, (1,1,"UR") : 1, (1,1,"RU") : 1}
    return mp

def iter_height_range(h):
    return range(h + 1)

def iter_width_range(w):
    return range(w + 1)

def skip_small_positions(i, j):
    return i + j <= 2

def get_mp_value(mp, key):
    return mp.get(key, 0)

def get_existing_mp(mp, key):
    if key in mp:
        return mp[key]
    return 0

def update_uu(mp, i, j):
    value = 0
    value += get_existing_mp(mp, (i, j - 1, 'UU'))
    value += get_existing_mp(mp, (i, j - 1, 'RU'))
    mp[(i, j, 'UU')] = value

def update_rr(mp, i, j):
    value = 0
    value += get_existing_mp(mp, (i - 1, j, 'RR'))
    value += get_existing_mp(mp, (i - 1, j, 'UR'))
    mp[(i, j, 'RR')] = value

def update_ur(mp, i, j):
    value = 0
    value += get_existing_mp(mp, (i - 1, j, 'UU'))
    mp[(i, j, 'UR')] = value

def update_ru(mp, i, j):
    value = 0
    value += get_existing_mp(mp, (i, j - 1, 'RR'))
    mp[(i, j, 'RU')] = value

def process_position(mp, i, j):
    update_uu(mp, i, j)
    update_rr(mp, i, j)
    update_ur(mp, i, j)
    update_ru(mp, i, j)

def process_grid(h, w, mp):
    for i in iter_height_range(h):
        for j in iter_width_range(w):
            if skip_small_positions(i, j):
                continue
            process_position(mp, i, j)

def compute_result(mp, h, w):
    res = get_mp_value(mp, (h, w, 'UU'))
    res += get_mp_value(mp, (h, w, 'UR'))
    res += get_mp_value(mp, (h, w, 'RU'))
    res += get_mp_value(mp, (h, w, 'RR'))
    return res % 100000

def main_loop():
    while True:
        h, w = read_input()
        if should_break(h):
            break
        h, w = set_decremented(h, w)
        mp = initialize_mp()
        process_grid(h, w, mp)
        result = compute_result(mp, h, w)
        print(result)

main_loop()