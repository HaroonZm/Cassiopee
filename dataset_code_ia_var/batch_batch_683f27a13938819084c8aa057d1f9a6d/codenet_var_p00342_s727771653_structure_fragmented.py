def read_n():
    return int(input())

def read_A():
    return list(map(int, input().split()))

def sort_desc(lst):
    return sorted(lst, reverse=True)

def find_first_index_excl(indices, excluded):
    idx = 0
    n = len(indices)
    while idx in excluded and idx < n:
        idx += 1
    return idx

def find_second_index_excl(indices, excluded):
    idx = 0
    n = len(indices)
    while idx in excluded and idx < n:
        idx += 1
    return idx

def calc_expr(A, i, j, p, q):
    return (A[p] + A[q]) / (A[i] - A[j])

def update_ans(ans, val):
    return max(ans, val)

def process_pair(A, n, i, j, ans):
    excluded_p = [i, j]
    p = find_first_index_excl(range(n), excluded_p)
    excluded_q = [i, j, p]
    q = find_second_index_excl(range(n), excluded_q)
    value = calc_expr(A, i, j, p, q)
    return update_ans(ans, value)

def iterate_all_pairs(A, n):
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = process_pair(A, n, i, j, ans)
    return ans

def print_result(ans):
    print("%.6f" % ans)

def main():
    n = read_n()
    A = read_A()
    A = sort_desc(A)
    ans = iterate_all_pairs(A, n)
    print_result(ans)

main()