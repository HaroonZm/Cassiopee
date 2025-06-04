def create_table(n):
    return [i + 1 for i in range(n)]

def find_initial_target(m):
    return m - 1

def remove_person(table, taget):
    table.pop(taget)
    return table

def adjust_target_after_removal(taget):
    return taget - 1

def next_target(taget, k, table_len):
    return (taget + k) % table_len

def reduce_table(table, k, taget):
    while len(table) > 1:
        table = remove_person(table, taget)
        taget = adjust_target_after_removal(taget)
        taget = next_target(taget, k, len(table))
    return table

def get_last_person(table):
    return table[0]

def solve(n, k, m):
    table = create_table(n)
    taget = find_initial_target(m)
    table = reduce_table(table, k, taget)
    return get_last_person(table)

def input_triplet():
    return map(int, input().split())

def input_loop():
    ans = []
    while True:
        n, k, m = input_triplet()
        if check_exit(n, k, m):
            break
        ans.append(solve(n, k, m))
    return ans

def check_exit(n, k, m):
    return n == 0 and k == 0 and m == 0

def output_results(ans):
    print(*ans, sep='\n')

if __name__ == '__main__':
    ans = input_loop()
    output_results(ans)