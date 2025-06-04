from itertools import combinations

def get_input():
    n = int(input())
    return n

def read_m():
    m = int(input())
    return m

def init_result_matrix(n):
    return [[None] * n for _ in range(n)]

def process_pair_input(result, n, m):
    for _ in range(m):
        x, y = parse_pair_input()
        update_result(result, x, y)

def parse_pair_input():
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    return x, y

def update_result(result, x, y):
    result[x][y] = True
    result[y][x] = False

def compute_t_count(result):
    return [lst.count(True) for lst in result]

def init_empty_index_and_nums(n):
    empty_index = [[] for _ in range(n)]
    empty_nums = [0] * n
    return empty_index, empty_nums

def fill_empty_index_and_nums(result, n, empty_index, empty_nums):
    for i in range(n):
        for j in range(i + 1, n):
            if is_entry_empty(result, i, j):
                append_empty(empty_index, empty_nums, i, j)

def is_entry_empty(result, i, j):
    return result[i][j] == None

def append_empty(empty_index, empty_nums, i, j):
    empty_index[i].append(j)
    empty_nums[i] += 1

def get_limit(n):
    return n // 2

def tuple_key(x, t_count):
    return (x, tuple(t_count))

def search(x, t_count, n, limit, empty_index, empty_nums, memo):
    return _search_recursive(x, t_count, n, limit, empty_index, empty_nums, memo)

def _search_recursive(x, t_count, n, limit, empty_index, empty_nums, memo):
    key = tuple_key(x, t_count)
    if key in memo:
        return memo[key]
    if is_finished(x, n):
        return 1
    choice_num = remaining_choices(limit, t_count, x)
    if not is_valid_choice(choice_num, empty_nums, x):
        return 0
    rest_num = get_rest_num(empty_nums, choice_num, x)
    total = run_combinations(x, t_count, n, limit, empty_index, empty_nums, memo, rest_num)
    memo[key] = total
    return total

def is_finished(x, n):
    return x == n

def remaining_choices(limit, t_count, x):
    return limit - t_count[x]

def is_valid_choice(choice_num, empty_nums, x):
    return 0 <= choice_num <= empty_nums[x]

def get_rest_num(empty_nums, choice_num, x):
    return empty_nums[x] - choice_num

def run_combinations(x, t_count, n, limit, empty_index, empty_nums, memo, rest_num):
    ret = 0
    for inds in combinations(empty_index[x], rest_num):
        new_count = new_count_list(t_count, inds)
        ret += search(x + 1, new_count, n, limit, empty_index, empty_nums, memo)
    return ret

def new_count_list(t_count, inds):
    new_count = t_count[:]
    for ind in inds:
        new_count[ind] += 1
    return new_count

def output_result(total):
    print(total)

def handle_problem():
    while True:
        n = get_input()
        if is_ending(n):
            break
        m = read_m()
        result = init_result_matrix(n)
        process_pair_input(result, n, m)
        t_count = compute_t_count(result)
        empty_index, empty_nums = init_empty_index_and_nums(n)
        fill_empty_index_and_nums(result, n, empty_index, empty_nums)
        memo = {}
        limit = get_limit(n)
        total = search(0, t_count, n, limit, empty_index, empty_nums, memo)
        output_result(total)

def is_ending(n):
    return n == 0

def main():
    handle_problem()

main()