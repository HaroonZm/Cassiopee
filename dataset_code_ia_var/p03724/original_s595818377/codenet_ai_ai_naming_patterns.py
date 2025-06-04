import sys
from collections import Counter

def input_read():
    return sys.stdin.read()

def main():
    num_elements, seq_length = map(int, input().split())
    sequence_values = list(map(int, input_read().split()))
    value_counts = Counter(sequence_values)
    result_status = "YES"
    for count in value_counts.values():
        if count % 2 != 0:
            result_status = "NO"
    print(result_status)

main()