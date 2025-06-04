def read_input_line():
    return input()

def split_line_to_ints(line):
    return [int(s) for s in line.split(" ")]

def read_bib():
    return int(input())

def read_bibs(n):
    bibs = []
    for i in range(n):
        bibs.append(read_bib())
    return bibs

def get_range(start, end):
    return range(start, end)

def should_swap(a, b, k):
    return a % k > b % k

def do_swap(bibs, i):
    (bibs[i], bibs[i+1]) = (bibs[i+1], bibs[i])

def process_k_for_bibs(bibs, n, k):
    for i in get_range(0, n-1):
        if should_swap(bibs[i], bibs[i+1], k):
            do_swap(bibs, i)

def process_all_ks(bibs, n, m):
    for k in get_range(1, m+1):
        process_k_for_bibs(bibs, n, k)

def print_bib(bib):
    print(bib)

def print_all_bibs(bibs):
    for bib in bibs:
        print_bib(bib)

def main():
    line = read_input_line()
    nums = split_line_to_ints(line)
    n = nums[0]
    m = nums[1]
    bibs = read_bibs(n)
    process_all_ks(bibs, n, m)
    print_all_bibs(bibs)

main()