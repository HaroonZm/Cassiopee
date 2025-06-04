import sys
import bisect
from collections import defaultdict

def read_int_list():
    return [int(element) for element in sys.stdin.readline().split()]

def read_single_int():
    return int(sys.stdin.readline())

def read_list_of_strings():
    return [list(element) for element in sys.stdin.readline().split()]

def read_string_as_char_list():
    return list(sys.stdin.readline())[:-1]

def read_multiple_integers(num_lines):
    return [read_single_int() for _ in range(num_lines)]

def read_multiple_int_lists(num_lines):
    return [read_int_list() for _ in range(num_lines)]

def read_multiple_string_lists(num_lines):
    return [read_list_of_strings() for _ in range(num_lines)]

sys.setrecursionlimit(1000000)
MODULO_CONSTANT = 1000000007

def process_and_validate_sequence():
    number_of_entries = read_single_int()
    event_times_by_label = defaultdict(lambda: [])

    for _ in range(number_of_entries):
        event_label, event_time_value = input().split()
        event_time_value = int(event_time_value)
        event_times_by_label[event_label].append(event_time_value)

    for label in event_times_by_label.keys():
        event_times_by_label[label].sort()

    sequence_length = read_single_int()
    current_time = 0

    for _ in range(sequence_length):
        event_label_query = input()
        if not event_times_by_label[event_label_query]:
            print("No")
            return

        position_of_next_time = bisect.bisect_right(event_times_by_label[event_label_query], current_time)
        if position_of_next_time == len(event_times_by_label[event_label_query]):
            print("No")
            return

        current_time = event_times_by_label[event_label_query][position_of_next_time]

    print("Yes")
    return

if __name__ == "__main__":
    process_and_validate_sequence()