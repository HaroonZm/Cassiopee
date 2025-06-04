import bisect

def initialize_lists():
    return [], [], [], 0

def bisect_left_in_list(D, key):
    return bisect.bisect_left(D, key)

def bisect_right_in_list(D, key):
    return bisect.bisect_right(D, key)

def update_existing_key(M, N, y, x):
    M[y][1] = x
    N[y] = x

def insert_new_key_at_y(M, D, N, y, key, x):
    M.insert(y, [key, x])
    D.insert(y, key)
    N.insert(y, x)

def increment_count(count):
    return count + 1

def insert(M, D, N, count, key, x):
    y = bisect_left_in_list(D, key)
    if is_key_at_y(D, y, count, key):
        update_existing_key(M, N, y, x)
    else:
        insert_new_key_at_y(M, D, N, y, key, x)
        count = increment_count(count)
    return M, D, N, count

def is_key_at_y(D, y, count, key):
    return y < count and D[y] == key

def print_value(value):
    print(value)

def get(D, N, count, key):
    y = bisect_left_in_list(D, key)
    if is_key_at_y(D, y, count, key):
        print_value(N[y])
    else:
        print_value(0)

def remove_at_y(M, D, N, y):
    M.pop(y)
    D.pop(y)
    N.pop(y)

def decrement_count(count):
    return count - 1

def erase(M, D, N, count, key):
    y = bisect_left_in_list(D, key)
    if is_key_at_y(D, y, count, key):
        remove_at_y(M, D, N, y)
        count = decrement_count(count)
    return M, D, N, count

def should_dump_entries(e, s):
    return (e - s) > 0

def print_entry(key, value):
    print(key + " " + str(value))

def dump_entries(M, s, e):
    for i in range(s, e):
        print_entry(M[i][0], M[i][1])

def dump(M, D, N, L, R):
    s = bisect_left_in_list(D, L)
    e = bisect_right_in_list(D, R)
    if should_dump_entries(e, s):
        dump_entries(M, s, e)

def parse_query():
    return list(map(str, input().split()))

def convert_first_query_element_to_int(query):
    query[0] = int(query[0])
    return query

def handle_insert_query(M, D, N, count, query):
    return insert(M, D, N, count, query[1], int(query[2]))

def handle_get_query(D, N, count, query):
    get(D, N, count, query[1])

def handle_erase_query(M, D, N, count, query):
    return erase(M, D, N, count, query[1])

def handle_dump_query(M, D, N, query):
    dump(M, D, N, query[1], query[2])

def process_query(M, D, N, count, query):
    if query[0] == 0:
        M, D, N, count = handle_insert_query(M, D, N, count, query)
    elif query[0] == 1:
        handle_get_query(D, N, count, query)
    elif query[0] == 2:
        M, D, N, count = handle_erase_query(M, D, N, count, query)
    else:
        handle_dump_query(M, D, N, query)
    return M, D, N, count

def read_number_of_queries():
    return int(input())

def main_loop():
    M, D, N, count = initialize_lists()
    q = read_number_of_queries()
    for _ in range(q):
        query = parse_query()
        query = convert_first_query_element_to_int(query)
        M, D, N, count = process_query(M, D, N, count, query)

main_loop()