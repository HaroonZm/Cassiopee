def read_int():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def read_query():
    return tuple(map(int, input().split()))

def read_queries(q):
    return [read_query() for _ in range(q)]

def compute_sorted_list(lst):
    return sorted(lst)

def count_diff(a_lst, comp):
    return sum([a_lst[i] != comp[i] for i in range(len(a_lst))])

def is_sorted(diff):
    return diff == 0

def swap_elements(lst, x, y):
    lst[x], lst[y] = lst[y], lst[x]

def compute_decrement(a_lst, comp, x, y):
    before = (a_lst[x] == comp[x]) + (a_lst[y] == comp[y])
    after = (a_lst[x] == comp[y]) + (a_lst[y] == comp[x])
    return after - before

def process_queries(a_lst, comp, queries, diff):
    n = len(a_lst)
    for i in range(len(queries)):
        x, y = queries[i]
        x -= 1
        y -= 1
        decrement = compute_decrement(a_lst, comp, x, y)
        diff += decrement
        if is_sorted(diff):
            print(i + 1)
            return
        swap_elements(a_lst, x, y)
    print(-1)

def main():
    n = read_int()
    a_lst = read_list()
    q = read_int()
    queries = read_queries(q)
    comp = compute_sorted_list(a_lst)
    diff = count_diff(a_lst, comp)
    if is_sorted(diff):
        print(0)
    else:
        process_queries(a_lst, comp, queries, diff)

main()