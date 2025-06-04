def main():
    input_range_size, input_center = map(int, input().split())
    range_start = input_center - input_range_size + 1
    range_end = input_center + input_range_size
    lower_bound = -1000000
    upper_bound = 1000000
    for current_value in range(range_start, range_end):
        if lower_bound <= current_value <= upper_bound:
            print(current_value, end=' ')

if __name__ == "__main__":
    main()