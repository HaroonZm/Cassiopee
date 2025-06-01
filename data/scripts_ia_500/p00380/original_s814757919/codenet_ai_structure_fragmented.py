def read_integer():
    return int(input())

def read_list_of_integers():
    return [int(i) for i in input().split()]

def sort_list(lst):
    return sorted(lst)

def count_mismatches(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def swap_elements(a, x, y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp

def update_judge_on_swap(a, sort_a, x, y, judge):
    if a[x] == sort_a[x] and a[y] != sort_a[x]:
        judge -= 1
    if a[x] != sort_a[x] and a[y] == sort_a[x]:
        judge += 1
    if a[y] == sort_a[y] and a[x] != sort_a[y]:
        judge -= 1
    if a[y] != sort_a[y] and a[x] == sort_a[y]:
        judge += 1
    return judge

def process_queries(a, sort_a, Q, judge):
    for i in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        swap_elements(a, x, y)
        judge = update_judge_on_swap(a, sort_a, x, y, judge)
        if judge == 0:
            print(i + 1)
            return
    print(-1)

def solve():
    N = read_integer()
    a = read_list_of_integers()
    Q = read_integer()
    sort_a = sort_list(a)
    judge = count_mismatches(a, sort_a)
    if judge == 0:
        print(0)
    else:
        process_queries(a, sort_a, Q, judge)

if __name__ == '__main__':
    solve()