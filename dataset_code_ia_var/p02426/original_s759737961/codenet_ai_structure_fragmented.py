def init_flag():
    return [0 for _ in range(64)]

def get_zero():
    return 0

def get_one():
    return 1

def get_element(lst, idx):
    return lst[idx]

def print_element(element):
    print(element)

def Test(flag, i):
    idx = i
    val = get_element(flag, idx)
    print_element(val)

def set_one(flag, idx):
    flag[idx] = get_one()

def Set(flag, m):
    for idx in m:
        set_one(flag, idx)
    return flag

def set_zero(flag, idx):
    flag[idx] = get_zero()

def Clear(flag, m):
    for idx in m:
        set_zero(flag, idx)
    return flag

def flip_value(flag, idx):
    if flag[idx] == get_zero():
        set_one(flag, idx)
    else:
        set_zero(flag, idx)

def Flip(flag, m):
    for idx in m:
        flip_value(flag, idx)
    return flag

def get_flag_vals(flag, m):
    return [flag[idx] for idx in m]

def is_all_true(lst):
    return all(lst) == True

def is_any_true(lst):
    return any(lst) == True

def is_none_true(lst):
    return not any(lst) == True

def output_one():
    print(1)

def output_zero():
    print(0)

def All(flag, m):
    vals = get_flag_vals(flag, m)
    if is_all_true(vals):
        output_one()
    else:
        output_zero()

def Any(flag, m):
    vals = get_flag_vals(flag, m)
    if is_any_true(vals):
        output_one()
    else:
        output_zero()

def none(flag, m):
    vals = get_flag_vals(flag, m)
    if is_none_true(vals):
        output_one()
    else:
        output_zero()

def count_ones(lst):
    return lst.count(1)

def Count(flag, m):
    vals = get_flag_vals(flag, m)
    cnt = count_ones(vals)
    print(cnt)

def get_power_of_two(i):
    return 2 ** i

def get_flag_index_contrib(flag, i):
    return flag[i] * get_power_of_two(i)

def Val(flag, m):
    a = 0
    for i in m:
        a += get_flag_index_contrib(flag, i)
    print(a)

def read_int():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def extract_mask_items(lst):
    return lst[1:]

def process_mask_input(n):
    mask = []
    for _ in range(n):
        lst = read_int_list()
        items = extract_mask_items(lst)
        mask.append(items)
    return mask

def process_query(flag, mask):
    query = read_int_list()
    qtype = query[0]
    if qtype == 0:
        Test(flag, query[1])
    elif qtype == 1:
        return Set(flag, mask[query[1]])
    elif qtype == 2:
        return Clear(flag, mask[query[1]])
    elif qtype == 3:
        return Flip(flag, mask[query[1]])
    elif qtype == 4:
        All(flag, mask[query[1]])
    elif qtype == 5:
        Any(flag, mask[query[1]])
    elif qtype == 6:
        none(flag, mask[query[1]])
    elif qtype == 7:
        Count(flag, mask[query[1]])
    else:
        Val(flag, mask[query[1]])
    return flag

def main():
    flag = init_flag()
    n = read_int()
    mask = process_mask_input(n)
    q = read_int()
    for _ in range(q):
        res = process_query(flag, mask)
        if res is not None:
            flag = res

main()