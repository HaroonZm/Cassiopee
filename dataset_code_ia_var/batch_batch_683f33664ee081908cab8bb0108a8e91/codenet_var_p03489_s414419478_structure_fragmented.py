from collections import defaultdict

def read_int():
    return int(input())

def split_line():
    return input().split()

def convert_to_int_list(str_list):
    return [int(i) for i in str_list]

def read_and_parse_int_list():
    return convert_to_int_list(split_line())

def increment_counter(dct, key):
    dct[key] += 1

def build_counter_list(nums):
    counter = defaultdict(int)
    for num in nums:
        increment_counter(counter, num)
    return counter

def process_one_key(x, kazu):
    if kazu[x] >= x:
        return kazu[x] - x
    else:
        return kazu[x]

def compute_answer(kazu):
    total = 0
    for key in kazu.keys():
        total += process_one_key(key, kazu)
    return total

def print_result(res):
    print(res)

def main():
    n = read_int()
    nums = read_and_parse_int_list()
    kazu = build_counter_list(nums)
    ans = compute_answer(kazu)
    print_result(ans)

main()