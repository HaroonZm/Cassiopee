from bisect import bisect_left, bisect_right, insort_left

def read_query_count():
    return int(input())

def read_query():
    return input().split()

def is_insert_query(query):
    return query[0] == '0'

def is_search_query(query):
    return query[0] == '1'

def is_delete_query(query):
    return query[0] == '2'

def is_range_query(query):
    return not (query[0] in ['0', '1', '2'])

def handle_insert(dictionary, keytbl, key, value):
    if key not in dictionary:
        insert_key_sorted(keytbl, key)
    dictionary[key] = value

def handle_search(dictionary, key):
    return dictionary[key] if key in dictionary else 0

def handle_delete(dictionary, key):
    if key in dictionary:
        dictionary[key] = 0

def insert_key_sorted(keytbl, key):
    insort_left(keytbl, key)

def handle_range_query(dictionary, keytbl, left, right):
    lidx = find_left_index(keytbl, left)
    ridx = find_right_index(keytbl, right, lidx)
    print_range(dictionary, keytbl, lidx, ridx)

def find_left_index(keytbl, left):
    return bisect_left(keytbl, left)

def find_right_index(keytbl, right, lidx):
    return bisect_right(keytbl, right, lidx)

def print_range(dictionary, keytbl, lidx, ridx):
    for j in range(lidx, ridx):
        print_if_positive(dictionary, keytbl[j])

def print_if_positive(dictionary, key):
    if dictionary[key] > 0:
        print(key, dictionary[key])

def main():
    dictionary = {}
    keytbl = []
    q = read_query_count()
    for _ in range(q):
        query = read_query()
        key = query[1]
        if is_insert_query(query):
            val = int(query[2])
            handle_insert(dictionary, keytbl, key, val)
        elif is_search_query(query):
            print(handle_search(dictionary, key))
        elif is_delete_query(query):
            handle_delete(dictionary, key)
        elif is_range_query(query):
            handle_range_query(dictionary, keytbl, query[1], query[2])

main()