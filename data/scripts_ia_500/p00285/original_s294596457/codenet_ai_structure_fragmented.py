def read_ints():
    return list(map(int, input().split()))

def read_pair():
    return map(int, input().split())

def calculate_rest(size):
    return 2 ** size - 1

def elec(bm, bw):
    bd = abs(bm - bw)
    return bd * (bd - 30) ** 2

def find_best_score(rest, index, mem, short_lst, long_lst):
    if mem[rest] is not None:
        return mem[rest]
    if rest == 0 or index < 0:
        return 0
    result = 0
    mask = 1
    count = 0
    while mask <= rest:
        if mask & rest:
            new_rest = rest & ~mask
            candidate = find_best_score(new_rest, index - 1, mem, short_lst, long_lst) + elec(short_lst[index], long_lst[count])
            result = max(result, candidate)
        mask <<= 1
        count += 1
    mem[rest] = result
    return result

def process_case(m, w):
    if m >= w:
        long_lst = read_ints()
        short_lst = read_ints()
        rest = calculate_rest(m)
    else:
        short_lst = read_ints()
        long_lst = read_ints()
        rest = calculate_rest(w)
    mem = [None] * (rest + 1)
    max_index = min(m, w) - 1
    return find_best_score(rest, max_index, mem, short_lst, long_lst)

def main_loop():
    while True:
        m, w = read_pair()
        if m == 0:
            break
        result = process_case(m, w)
        print(result)

def main():
    main_loop()

main()