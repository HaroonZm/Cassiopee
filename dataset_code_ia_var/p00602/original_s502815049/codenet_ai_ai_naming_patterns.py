import sys

def main():
    sys.setrecursionlimit(10000000)
    for input_line in sys.stdin:
        value_total, distance_min = map(int, input_line.split())
        sequence_presence = [False for sequence_index in range(2000)]
        prev_value_1 = prev_value_2 = 1
        for value_index in range(value_total):
            current_value = (prev_value_1 + prev_value_2) % 1001
            sequence_presence[current_value] = True
            prev_value_1, prev_value_2 = prev_value_2, current_value
        count_result = 0
        last_position = -10000
        for position_index in range(2000):
            if sequence_presence[position_index]:
                if position_index - last_position >= distance_min:
                    count_result += 1
                last_position = position_index
        print(count_result)

if __name__ == "__main__":
    main()