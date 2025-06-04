def read_input():
    return int(input())

def read_height_list():
    return list(map(int, input().split()))

def init_counters():
    return 0, 0

def get_initial_last(h):
    return h[0]

def update_cnt(last, x, cnt):
    if last >= x:
        return cnt + 1
    else:
        return 0

def update_cache(cache, cnt):
    if cache < cnt:
        return cnt
    return cache

def process_heights(h):
    cnt, cache = init_counters()
    last = get_initial_last(h)
    for x in get_remaining_heights(h):
        cnt = update_cnt(last, x, cnt)
        cache = update_cache(cache, cnt)
        last = update_last(x)
    return cache

def get_remaining_heights(h):
    return h[1:]

def update_last(x):
    return x

def main():
    n = read_input()
    h = read_height_list()
    result = process_heights(h)
    output_result(result)

def output_result(result):
    print(result)

main()