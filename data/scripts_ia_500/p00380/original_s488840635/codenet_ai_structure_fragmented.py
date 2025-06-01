def read_integer():
    return int(input())

def read_int_list():
    return list(map(int, input().split()))

def read_queries(q):
    queries = []
    for _ in range(q):
        queries.append(tuple(map(int, input().split())))
    return queries

def compute_sorted_list(a_lst):
    return sorted(a_lst)

def count_diff(a_lst, comp):
    count = 0
    for i in range(len(a_lst)):
        if a_lst[i] != comp[i]:
            count += 1
    return count

def update_diff(diff, a_lst, comp, x, y):
    diff -= (a_lst[x] == comp[y]) + (a_lst[y] == comp[x]) - (a_lst[x] == comp[x]) - (a_lst[y] == comp[y])
    return diff

def swap_elements(a_lst, x, y):
    a_lst[x], a_lst[y] = a_lst[y], a_lst[x]

def process_queries(n, a_lst, q, query, comp):
    diff = count_diff(a_lst, comp)
    if diff == 0:
        print(0)
        return
    for i in range(q):
        x, y = query[i]
        x, y = adjust_indices(x, y)
        diff = update_diff(diff, a_lst, comp, x, y)
        if diff == 0:
            print(i + 1)
            return
        swap_elements(a_lst, x, y)
    print(-1)

def adjust_indices(x, y):
    return x - 1, y - 1

def main():
    n = read_integer()
    a_lst = read_int_list()
    q = read_integer()
    query = read_queries(q)
    comp = compute_sorted_list(a_lst)
    process_queries(n, a_lst, q, query, comp)

main()