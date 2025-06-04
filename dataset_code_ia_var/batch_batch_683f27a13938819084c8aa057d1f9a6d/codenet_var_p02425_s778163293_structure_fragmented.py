def read_query():
    return [int(x) for x in input().split()]

def get_temp(bit_index):
    return 1 << bit_index

def check_bit(n, temp):
    if (n & temp) == 0:
        print(0)
    else:
        print(1)
    return n

def set_bit(n, temp):
    return n | temp

def clear_bit(n, temp, mask):
    return n & (~temp & mask)

def toggle_bit(n, temp):
    return n ^ temp

def is_all_set(n, mask):
    if n == mask:
        print(1)
    else:
        print(0)
    return n

def is_any_set(n, mask):
    if n & mask > 0:
        print(1)
    else:
        print(0)
    return n

def is_none_set(n):
    if n == 0:
        print(1)
    else:
        print(0)
    return n

def count_bits(n):
    temp = n
    one = 1
    counter = 0
    for i in range(64):
        if one & temp == 1:
            counter += 1
        temp = temp >> 1
    print(counter)
    return n

def print_value(n):
    print(n)
    return n

def process_query(query, n, mask):
    if query[0] == 0:
        temp = get_temp(query[1])
        n = check_bit(n, temp)
    elif query[0] == 1:
        temp = get_temp(query[1])
        n = set_bit(n, temp)
    elif query[0] == 2:
        temp = get_temp(query[1])
        n = clear_bit(n, temp, mask)
    elif query[0] == 3:
        temp = get_temp(query[1])
        n = toggle_bit(n, temp)
    elif query[0] == 4:
        n = is_all_set(n, mask)
    elif query[0] == 5:
        n = is_any_set(n, mask)
    elif query[0] == 6:
        n = is_none_set(n)
    elif query[0] == 7:
        n = count_bits(n)
    elif query[0] == 8:
        n = print_value(n)
    return n

def main_loop(q, mask):
    n = 0
    for _ in range(q):
        query = read_query()
        n = process_query(query, n, mask)

def main():
    q = int(input())
    MASK = (1 << 64) - 1
    main_loop(q, MASK)

main()