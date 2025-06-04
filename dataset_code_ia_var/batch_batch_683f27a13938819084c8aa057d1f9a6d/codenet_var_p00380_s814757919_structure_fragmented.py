def read_int():
    return int(input())

def read_int_list():
    return [int(i) for i in input().split()]

def get_sorted_copy(lst):
    return sorted(lst)

def count_differences(lst1, lst2):
    count = 0
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            count += 1
    return count

def is_sorted(judge):
    return judge == 0

def swap_elements(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp

def evaluate_single_position(a, sort_a, index):
    return a[index] == sort_a[index]

def adjust_judge_after_swap(a, sort_a, x, y, prev_judge):
    judge = prev_judge
    before_x = evaluate_single_position(a, sort_a, x)
    before_y = evaluate_single_position(a, sort_a, y)
    swap_elements(a, x, y)
    after_x = evaluate_single_position(a, sort_a, x)
    after_y = evaluate_single_position(a, sort_a, y)
    judge = prev_judge

    if after_x and not before_x:
        judge -= 1
    if not after_x and before_x:
        judge += 1
    if after_y and not before_y:
        judge -= 1
    if not after_y and before_y:
        judge += 1
    return judge

def process_queries(a, sort_a, Q, judge):
    for i in range(Q):
        x, y = read_int_list()
        x -= 1
        y -= 1
        before_x = evaluate_single_position(a, sort_a, x)
        before_y = evaluate_single_position(a, sort_a, y)
        swap_elements(a, x, y)
        after_x = evaluate_single_position(a, sort_a, x)
        after_y = evaluate_single_position(a, sort_a, y)
        if after_x and not before_x:
            judge -= 1
        if not after_x and before_x:
            judge += 1
        if after_y and not before_y:
            judge -= 1
        if not after_y and before_y:
            judge += 1
        if is_sorted(judge):
            print(i + 1)
            return
    print(-1)

def print_if_sorted(judge):
    if is_sorted(judge):
        print(0)
        return True
    return False

def solve():
    N = read_int()
    a = read_int_list()
    Q = read_int()
    sort_a = get_sorted_copy(a)
    judge = count_differences(a, sort_a)
    if print_if_sorted(judge):
        return
    process_queries(a, sort_a, Q, judge)

if __name__ == '__main__':
    solve()