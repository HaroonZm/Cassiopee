def read_input():
    return map(int, input().split())

def read_array():
    return list(map(int, input().split()))

def create_initial_list(m):
    return [0] * (m + 2)

def process_diff_list(a, m, l):
    for i, j in zip(a, a[1:]):
        handle_diff_case(i, j, m, l)

def handle_diff_case(i, j, m, l):
    if j > i + 1:
        update_increase_case(i, j, l)
    elif i > j:
        update_decrease_case(i, j, m, l)

def update_increase_case(i, j, l):
    l[j + 1] -= 1
    l[i + 2] += 1

def update_decrease_case(i, j, m, l):
    if i <= m - 2:
        l[i + 2] += 1
        l[m + 1] -= 1
        l[1] += 1
        l[j + 1] -= 1
    else:
        l[i + 2 - m] += 1
        l[j + 1] -= 1

def accumulate_list(l):
    from itertools import accumulate
    return list(accumulate(l))

def process_answer(a, m, l):
    ans = 0
    l1 = 0
    for i, j in zip(a, a[1:]):
        ans, l1 = update_answer(i, j, m, l, ans, l1)
    return ans, l1

def update_answer(i, j, m, l, ans, l1):
    if j > i:
        ans += j - i
        l[j + 1] -= (j - i - 1)
    else:
        l1 += m - i
        ans += m + j - i
        l[j + 1] -= (m + j - i - 1)
    return ans, l1

def set_first_list_element(l, l1):
    l[1] = l1

def main():
    n, m = read_input()
    a = read_array()
    l = create_initial_list(m)
    process_diff_list(a, m, l)
    l = accumulate_list(l)
    ans, l1 = process_answer(a, m, l)
    set_first_list_element(l, l1)
    l = accumulate_list(l)
    output_result(ans, l, m)

def output_result(ans, l, m):
    print(ans - max(l[1:m + 1]))

main()