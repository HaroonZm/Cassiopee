from functools import reduce

def read_input():
    return input()

def is_termination_value(value):
    return value == "0000"

def pad_number(n):
    return n if len(n) >= 4 else n.zfill(4)

def all_digits_identical(n):
    comparisons = [n[0] == i for i in n]
    return reduce(lambda x, y: x and y, comparisons)

def sort_digits_ascending(n):
    return ''.join(sorted(n))

def sort_digits_descending(n):
    return ''.join(sorted(n, reverse=True))

def subtract_numbers_desc_asc(desc, asc):
    return str(int(desc) - int(asc))

def kaprekar_step(n):
    asc = sort_digits_ascending(n)
    desc = sort_digits_descending(n)
    result = subtract_numbers_desc_asc(desc, asc)
    return pad_number(result)

def count_kaprekar_iterations(n):
    count = 0
    while n != "6174":
        n = kaprekar_step(n)
        count += 1
    return count

def process_number(n):
    n = pad_number(n)
    if all_digits_identical(n):
        print("NA")
    else:
        print(count_kaprekar_iterations(n))

def main():
    while True:
        n = read_input()
        if is_termination_value(n):
            break
        process_number(n)

main()