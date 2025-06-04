def main_entry_point():
    input_values_list = input().split()
    mapped_integers = map(int, input_values_list)
    summed_result = sum(mapped_integers)
    print(summed_result)

if __name__ == '__main__':
    main_entry_point()