from itertools import combinations as comb

def get_n():
    return int(input())

def get_m():
    return int(input())

def initialize_result(n):
    return [[None] * n for _ in range(n)]

def read_pair():
    x, y = map(int, input().split())
    return x - 1, y - 1

def fill_result(result, m):
    for _ in range(m):
        x, y = read_pair()
        result[x][y] = True
        result[y][x] = False

def compute_t_count(result):
    return [row.count(True) for row in result]

def initialize_empty_structs(n):
    return [[] for _ in range(n)], [0] * n

def fill_empty_structs(n, result, empty_index, empty_nums):
    for i in range(n):
        for j in range(i + 1, n):
            if result[i][j] is None:
                empty_index[i].append(j)
                empty_nums[i] += 1

def compute_limit(n):
    return n // 2

def search(x, n, t_count, empty_index, empty_nums, limit):
    if x == n:
        return 1
    choice_num = limit - t_count[x]
    if choice_num < 0 or choice_num > empty_nums[x]:
        return 0
    rest_num = empty_nums[x] - choice_num
    ret = 0
    for inds in comb(empty_index[x], rest_num):
        new_count = t_count[:]
        for ind in inds:
            new_count[ind] += 1
        ret += search(x + 1, n, new_count, empty_index, empty_nums, limit)
    return ret

def process_case(n, m):
    result = initialize_result(n)
    fill_result(result, m)
    t_count = compute_t_count(result)
    empty_index, empty_nums = initialize_empty_structs(n)
    fill_empty_structs(n, result, empty_index, empty_nums)
    limit = compute_limit(n)
    return search(0, n, t_count, empty_index, empty_nums, limit)

def process_all_cases():
    while True:
        n = get_n()
        if n == 0:
            break
        m = get_m()
        print(process_case(n, m))

def main():
    process_all_cases()

main()