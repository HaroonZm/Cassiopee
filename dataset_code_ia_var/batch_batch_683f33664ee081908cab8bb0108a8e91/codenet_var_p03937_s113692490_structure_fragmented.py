def read_dimensions():
    return input()

def parse_dimensions(dim_str):
    return map(int, dim_str.split())

def read_line():
    return input()

def count_hash_in_line(line):
    return line.count("#")

def update_ans(ans, count):
    return ans + count

def read_and_count_hashes(h):
    total_hashes = 0
    for _ in range(h):
        line = read_line()
        count = count_hash_in_line(line)
        total_hashes = update_ans(total_hashes, count)
    return total_hashes

def compute_required_hashes(h, w):
    return h + w - 1

def check_possibility(required, found):
    return "Possible" if required == found else "Impossible"

def output_result(result):
    print(result)

def main():
    dim_str = read_dimensions()
    h, w = parse_dimensions(dim_str)
    found_hashes = read_and_count_hashes(h)
    required_hashes = compute_required_hashes(h, w)
    result = check_possibility(required_hashes, found_hashes)
    output_result(result)

main()