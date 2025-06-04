MASK = (1 << 64) - 1

x = 0
M = []

def get_mask_value(m):
    return M[m]

def mask_for_bits(B):
    return sum(1 << b for b in B)

def test_bit(i):
    global x
    return +(x & (1 << i) > 0)

def set_value_mask(m):
    global x
    v = get_mask_value(m)
    x |= v

def clear_value_mask(m):
    global x
    v = get_mask_value(m)
    x = (x | v) ^ v

def flip_value_mask(m):
    global x
    v = get_mask_value(m)
    x ^= v

def all_value_mask(m):
    v = get_mask_value(m)
    return +(x & v == v)

def any_value_mask(m):
    v = get_mask_value(m)
    return +(x & v > 0)

def none_value_mask(m):
    v = get_mask_value(m)
    return +(x & v == 0)

def count_value_mask(m):
    v = get_mask_value(m)
    return bin(x & v).count('1')

def val_value_mask(m):
    v = get_mask_value(m)
    return x & v

def fmap_init():
    return [
        test_bit,
        set_value_mask,
        clear_value_mask,
        flip_value_mask,
        all_value_mask,
        any_value_mask,
        none_value_mask,
        count_value_mask,
        val_value_mask,
    ]

def parse_mask_definition():
    parts = input().split()
    k = int(parts[0])
    B = list(map(int, parts[1:]))
    return k, B

def add_mask(B):
    M.append(mask_for_bits(B))

def parse_query_line():
    return list(map(int, input().split()))

def process_query_line(vals):
    t, *cmd = vals
    func = fmap[t]
    res = func(*cmd)
    if res is not None:
        return res
    return None

def query(Q):
    for _ in range(Q):
        vals = parse_query_line()
        res = process_query_line(vals)
        if res is not None:
            yield res

def read_N():
    return int(input())

def read_Q():
    return int(input())

def init_masks(N):
    for _ in range(N):
        _, B = parse_mask_definition()
        add_mask(B)

def main():
    global fmap
    fmap = fmap_init()
    N = read_N()
    init_masks(N)
    Q = read_Q()
    results = query(Q)
    print(*results, sep='\n')

main()