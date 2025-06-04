def read_input():
    n, q = map(int, raw_input().split())
    return n, q

def initialize_exist():
    return set([1])

def initialize_cup(n):
    return range(n + 2)

def initialize_now():
    return 1

def add_adjacent(exist, cup, now):
    exist.add(cup[now - 1])
    exist.add(cup[now + 1])

def read_swap():
    a, b = map(int, raw_input().split())
    return a, b

def update_now(now, a, b):
    if now == a:
        return b
    elif now == b:
        return a
    return now

def swap_cup(cup, a, b):
    tmp = cup[a]
    cup[a] = cup[b]
    cup[b] = tmp

def process_queries(q, cup, now, exist):
    for _ in xrange(q):
        a, b = read_swap()
        now = update_now(now, a, b)
        swap_cup(cup, a, b)
        add_adjacent(exist, cup, now)
    return now

def convert_exist_to_list(exist):
    return list(exist)

def count_valid(exist, n):
    ans = 0
    for i in xrange(len(exist)):
        if exist[i] != 0 and exist[i] != n + 1:
            ans += 1
    return ans

def print_ans(ans):
    print ans

def main():
    n, q = read_input()
    exist = initialize_exist()
    cup = initialize_cup(n)
    now = initialize_now()
    add_adjacent(exist, cup, now)
    now = process_queries(q, cup, now, exist)
    exist = convert_exist_to_list(exist)
    ans = count_valid(exist, n)
    print_ans(ans)

main()