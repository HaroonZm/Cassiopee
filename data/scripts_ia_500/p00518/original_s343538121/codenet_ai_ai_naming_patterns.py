import sys
from collections import Counter
from itertools import product

def count_valid_schedules(length, sequence):
    current_state_counts = Counter({(1, 0, 0): 1})
    for day_char in sequence:
        next_state_counts = Counter()
        for new_j, new_o, new_i in product((0, 1), repeat=3):
            if {'J': new_j, 'O': new_o, 'I': new_i}[day_char]:
                for (prev_j, prev_o, prev_i), count in current_state_counts.items():
                    if (new_j and prev_j) or (new_o and prev_o) or (new_i and prev_i):
                        next_state_counts[(new_j, new_o, new_i)] += count
        current_state_counts = Counter({state: cnt % 10007 for state, cnt in next_state_counts.items()})
    return sum(current_state_counts.values()) % 10007

def main(_args):
    n = int(input())
    sequence = input()
    result = count_valid_schedules(n, sequence)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])