def read_n():
    return int(input())

def read_pair():
    return map(int, input().split())

def compute_segment_length(l, r):
    return r - l + 1

def process_single_pair():
    l, r = read_pair()
    return compute_segment_length(l, r)

def accumulate_segments(n):
    total = 0
    for _ in range(n):
        total = add_to_total(total, process_single_pair())
    return total

def add_to_total(current, value):
    return current + value

def print_result(result):
    print(result)

def main():
    n = read_n()
    answer = accumulate_segments(n)
    print_result(answer)

main()