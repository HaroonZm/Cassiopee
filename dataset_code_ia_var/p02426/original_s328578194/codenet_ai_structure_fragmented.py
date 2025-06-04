def create_bits():
    return [0] * 64

def read_int():
    return int(input())

def read_mask_line():
    return list(map(int, input().split()))

def process_masks(num_mask):
    masks = [[] for _ in range(num_mask)]
    for idx in range(num_mask):
        line = read_mask_line()
        add_mask_entry(masks, idx, line)
    return masks

def add_mask_entry(masks, idx, line):
    k = line[0]
    v = line[1:]
    for value in v:
        append_mask_value(masks, idx, value)

def append_mask_value(masks, idx, value):
    masks[idx].append(value)

def process_queries(num_query, masks, bits):
    for _ in range(num_query):
        line = list(map(int, input().split()))
        dispatch_query(line, bits, masks)

def dispatch_query(line, bits, masks):
    op = line[0]
    v = line[1:]
    if op == 0:
        do_query_op0(bits, v)
    elif op == 1:
        do_query_op1(bits, masks, v)
    elif op == 2:
        do_query_op2(bits, masks, v)
    elif op == 3:
        do_query_op3(bits, masks, v)
    elif op == 4:
        do_query_op4(bits, masks, v)
    elif op == 5:
        do_query_op5(bits, masks, v)
    elif op == 6:
        do_query_op6(bits, masks, v)
    elif op == 7:
        do_query_op7(bits, masks, v)
    else:
        do_query_else(bits, masks, v)

def do_query_op0(bits, v):
    i = v[0]
    if is_bit_set(bits, i):
        print(1)
    else:
        print(0)

def is_bit_set(bits, idx):
    return bits[idx] == 1

def do_query_op1(bits, masks, v):
    for m_idx in get_mask_indices(masks, v[0]):
        set_bit(bits, m_idx)

def do_query_op2(bits, masks, v):
    for m_idx in get_mask_indices(masks, v[0]):
        clear_bit(bits, m_idx)

def do_query_op3(bits, masks, v):
    for m_idx in get_mask_indices(masks, v[0]):
        toggle_bit(bits, m_idx)

def do_query_op4(bits, masks, v):
    all_flg = 1
    for m_idx in get_mask_indices(masks, v[0]):
        all_flg *= bits[m_idx]
    print(1 if all_flg else 0)

def do_query_op5(bits, masks, v):
    any_flg = 0
    for m_idx in get_mask_indices(masks, v[0]):
        any_flg += bits[m_idx]
    print(1 if any_flg else 0)

def do_query_op6(bits, masks, v):
    none_flg = 0
    for m_idx in get_mask_indices(masks, v[0]):
        none_flg += bits[m_idx]
    print(1 if not none_flg else 0)

def do_query_op7(bits, masks, v):
    count = count_bits_in_mask(bits, masks, v[0])
    print(count)

def do_query_else(bits, masks, v):
    ans = make_ans_bits(bits, masks, v[0])
    bin_str = bits_to_str(ans)
    print(int(bin_str, 2))

def get_mask_indices(masks, idx):
    return masks[idx]

def set_bit(bits, idx):
    bits[idx] = 1

def clear_bit(bits, idx):
    bits[idx] = 0

def toggle_bit(bits, idx):
    bits[idx] = 1 if bits[idx] == 0 else 0

def count_bits_in_mask(bits, masks, idx):
    count = 0
    for m_idx in get_mask_indices(masks, idx):
        count += bits[m_idx]
    return count

def make_ans_bits(bits, masks, idx):
    ans = [0] * 64
    for m_idx in get_mask_indices(masks, idx):
        ans[m_idx] = bits[m_idx]
    return ans

def bits_to_str(bits_arr):
    return "".join([str(elem) for elem in bits_arr[::-1]])

def main():
    bits = create_bits()
    num_mask = read_int()
    masks = process_masks(num_mask)
    num_query = read_int()
    process_queries(num_query, masks, bits)

if __name__ == "__main__":
    main()