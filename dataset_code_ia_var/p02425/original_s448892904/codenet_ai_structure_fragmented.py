def get_input():
    return int(input())

def get_mask():
    return 2 ** 64 - 1

def get_x_init():
    return 0

def input_command():
    return list(map(int, input().split()))

def parse_command(cmd):
    return cmd[0], cmd[1:]

def is_bit_set(value, i):
    return int((value & (1 << i)) > 0)

def set_bit(value, i):
    return value | (1 << i)

def clear_bit(value, i):
    if value & (1 << i):
        return value ^ (1 << i)
    return value

def flip_bit(value, i):
    return value ^ (1 << i)

def check_all(value, mask):
    return int(value & mask == mask)

def check_any(value, mask):
    return int(value & mask > 0)

def check_none(value, mask):
    return int(value & mask == 0)

def count_ones(value):
    return bin(value).count("1")

def print_if_not_none(ans):
    if ans is not None:
        print(ans)

def get_x_value(value):
    return value

def exec_command(idx, args, value, mask):
    if idx == 0:
        return is_bit_set(value, *args), value
    elif idx == 1:
        new_value = set_bit(value, *args)
        return None, new_value
    elif idx == 2:
        new_value = clear_bit(value, *args)
        return None, new_value
    elif idx == 3:
        new_value = flip_bit(value, *args)
        return None, new_value
    elif idx == 4:
        return check_all(value, mask), value
    elif idx == 5:
        return check_any(value, mask), value
    elif idx == 6:
        return check_none(value, mask), value
    elif idx == 7:
        return count_ones(value), value
    elif idx == 8:
        return get_x_value(value), value
    else:
        return None, value

def process_queries(q, mask, value):
    for _ in range(q):
        cmd = input_command()
        idx, args = parse_command(cmd)
        ans, value = exec_command(idx, args, value, mask)
        print_if_not_none(ans)
    return value

def main():
    q = get_input()
    mask = get_mask()
    value = get_x_init()
    value = process_queries(q, mask, value)

main()