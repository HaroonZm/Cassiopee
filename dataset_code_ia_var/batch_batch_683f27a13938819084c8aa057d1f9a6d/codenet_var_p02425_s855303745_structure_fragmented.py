def get_input_count():
    return int(input())

def init_bits():
    return ["0" for _ in range(64)]

def get_query():
    return input().split()

def get_query_type(query):
    return query[0]

def get_query_index(query):
    return int(query[1])

def check_bit(num, idx):
    return 0 if num[idx] == "0" else 1

def set_bit(num, idx):
    num[idx] = "1"

def reset_bit(num, idx):
    num[idx] = "0"

def flip_bit(num, idx):
    num[idx] = "1" if num[idx] == "0" else "0"

def is_all_one(num):
    return "1" if num.count("1") == 64 else "0"

def is_one_or_more_one(num):
    return "1" if num.count("1") >= 1 else "0"

def is_all_zero(num):
    return "1" if num.count("1") == 0 else "0"

def count_one(num):
    return num.count("1")

def bits_to_decimal(num):
    return int("".join(num[::-1]), 2)

def process_query(query, num):
    q_type = get_query_type(query)
    if q_type == "0":
        idx = get_query_index(query)
        print(check_bit(num, idx))
    elif q_type == "1":
        idx = get_query_index(query)
        set_bit(num, idx)
    elif q_type == "2":
        idx = get_query_index(query)
        reset_bit(num, idx)
    elif q_type == "3":
        idx = get_query_index(query)
        flip_bit(num, idx)
    elif q_type == "4":
        print(is_all_one(num))
    elif q_type == "5":
        print(is_one_or_more_one(num))
    elif q_type == "6":
        print(is_all_zero(num))
    elif q_type == "7":
        print(count_one(num))
    elif q_type == "8":
        print(bits_to_decimal(num))

def main_loop(n, num):
    for _ in range(n):
        query = get_query()
        process_query(query, num)

def main():
    n = get_input_count()
    num = init_bits()
    main_loop(n, num)

main()