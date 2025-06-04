import sys
read_input = sys.stdin.readline

def process_sequence():
    sequence_length = int(read_input())
    base_values = list(map(int, read_input().split()))
    computed_values = [0] * sequence_length
    computed_values[0] = base_values[0]

    for idx in range(sequence_length - 1):
        computed_values[idx] = min(computed_values[idx], base_values[idx])
        computed_values[idx + 1] = base_values[idx]

    print(sum(computed_values))

process_sequence()