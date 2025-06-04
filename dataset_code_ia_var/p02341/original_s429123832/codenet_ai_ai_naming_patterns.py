def main_entry_point():
    input_n_value, input_k_value = map(int, input().split())
    output_answer_value = 0
    if input_n_value <= input_k_value:
        output_answer_value = 1
    print(output_answer_value)

if __name__ == "__main__":
    main_entry_point()