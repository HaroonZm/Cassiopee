def read_int():
    return int(input())

def read_line():
    return input()

def parse_mask_line(line):
    parts = list(map(int, line.split()))
    k = parts[0]
    list_b = parts[1:]
    return k, list_b

def bit_mask_from_indices(list_b):
    mask = 0
    for i in range(len(list_b)):
        mask = add_bit_to_mask(mask, list_b[i])
    return mask

def add_bit_to_mask(mask, index):
    return mask + power_of_two(index)

def power_of_two(i):
    return 2 ** i

def build_list_mask(n):
    list_mask = []
    for _ in range(n):
        line = read_line()
        k, list_b = parse_mask_line(line)
        mask = bit_mask_from_indices(list_b)
        list_mask.append(mask)
    return list_mask

def get_command():
    return input().split()

def get_command_and_num(lst):
    command = lst[0]
    m = int(lst[1])
    return command, m

def test_bit(bit_flag, i):
    return (bit_flag & power_of_two(i)) != 0

def print_test_bit(bit_flag, i):
    if test_bit(bit_flag, i):
        print(1)
    else:
        print(0)

def set_mask(bit_flag, mask):
    return bit_flag | mask

def clear_mask(bit_flag, mask):
    return bit_flag & ~mask

def flip_mask(bit_flag, mask):
    return bit_flag ^ mask

def all_mask(bit_flag, mask):
    return (bit_flag & mask) == mask

def print_all_mask(bit_flag, mask):
    if all_mask(bit_flag, mask):
        print(1)
    else:
        print(0)

def any_mask(bit_flag, mask):
    return (bit_flag & mask) != 0

def print_any_mask(bit_flag, mask):
    if any_mask(bit_flag, mask):
        print(1)
    else:
        print(0)

def none_mask(bit_flag, mask):
    return (bit_flag & mask) == 0

def print_none_mask(bit_flag, mask):
    if none_mask(bit_flag, mask):
        print(1)
    else:
        print(0)

def count_mask_bits(bit_flag, mask):
    return bin(bit_flag & mask).count("1")

def print_count_mask(bit_flag, mask):
    print(count_mask_bits(bit_flag, mask))

def val_mask(bit_flag, mask):
    return bit_flag & mask

def print_val_mask(bit_flag, mask):
    print(val_mask(bit_flag, mask))

def process_command(command, m, list_mask, bit_flag):
    if command == "0":
        print_test_bit(bit_flag, m)
        return bit_flag
    elif command == "1":
        bit_flag = set_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "2":
        bit_flag = clear_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "3":
        bit_flag = flip_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "4":
        print_all_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "5":
        print_any_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "6":
        print_none_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "7":
        print_count_mask(bit_flag, list_mask[m])
        return bit_flag
    elif command == "8":
        print_val_mask(bit_flag, list_mask[m])
        return bit_flag
    else:
        raise Exception("Unknown command")

def process_queries(q, list_mask):
    bit_flag = 0
    for _ in range(q):
        args = get_command()
        command, m = get_command_and_num(args)
        bit_flag = process_command(command, m, list_mask, bit_flag)
    return

def main():
    n = read_int()
    list_mask = build_list_mask(n)
    q = read_int()
    process_queries(q, list_mask)

main()