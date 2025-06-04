import collections
from operator import itemgetter

def read_input():
    return raw_input()

def parse_initial_line(line):
    return map(int, line.split())

def should_exit(num_people, num_border):
    return num_people == 0 and num_border == 0

def process_person_line(line):
    items = line.split()
    items = [int(s) for s in items]
    if items[0] != 0:
        del items[0]
        return items
    return []

def gather_all_numbers(num_people):
    all_numbers = []
    for _ in range(num_people):
        line = read_input()
        numbers = process_person_line(line)
        all_numbers.extend(numbers)
    return all_numbers

def count_occurrences(numbers):
    return collections.Counter(numbers)

def has_no_data(counter):
    return not counter

def prepare_sorted_items(counter):
    return sorted(counter.items(), key=itemgetter(0))

def print_result_for_case(counter, sorted_items, num_border):
    for key, value in sorted(sorted_items, key=itemgetter(1), reverse=True):
        if value >= num_border:
            print key
            return
        else:
            print "0"
            return

def main():
    while True:
        max_value = 1  # Kept from original, though unused
        line = read_input()
        num_people, num_border = parse_initial_line(line)
        if should_exit(num_people, num_border):
            break
        numbers = gather_all_numbers(num_people)
        counter = count_occurrences(numbers)
        if has_no_data(counter):
            print "0"
        else:
            sorted_items = prepare_sorted_items(counter)
            print_result_for_case(counter, sorted_items, num_border)

main()