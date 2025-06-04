def main():
    input_count = int(input())
    height_list = []

    for index_input in range(input_count):
        height_list.append(int(input()))

    reduction_counter = 0
    total_sum = 1

    height_list_sorted = sorted(height_list, reverse=True)

    for index_height, current_height in enumerate(height_list_sorted):
        adjusted_height = current_height - reduction_counter
        if adjusted_height < 0:
            adjusted_height = 0
        total_sum += adjusted_height
        if index_height % 4 == 3:
            reduction_counter += 1

    print(total_sum)

if __name__ == "__main__":
    main()