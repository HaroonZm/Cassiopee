import sys
from collections import defaultdict

input_bytes = sys.stdin.buffer.read
input_line_bytes = sys.stdin.buffer.readline

parse_int = lambda: int(input_line_bytes())
parse_two_ints = lambda: map(int, input_line_bytes().split())
parse_int_list = lambda: list(map(int, input_line_bytes().split()))
parse_all_ints = lambda: map(int, input_bytes().split())
parse_str = lambda: input_line_bytes().rstrip().decode('utf-8')

def main():
    num_n, num_m = parse_two_ints()
    freq_count = defaultdict(int)
    for val in parse_all_ints():
        freq_count[val] += 1

    result_str = 'YES'
    for idx in range(1, num_n + 1):
        if freq_count[idx] % 2 == 1:
            result_str = 'NO'
            break

    print(result_str)

if __name__ == '__main__':
    main()