val_coeff_list = [0, 6000, 4000, 3000, 2000]
for idx_iter in range(4):
    input_type, input_count = map(int, input().split())
    output_value = input_count * val_coeff_list[input_type]
    print(output_value)