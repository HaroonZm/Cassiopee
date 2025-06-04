def main():
    input_value_a, input_value_b, input_value_x = map(int, input().split())
    modulus_constant = 1000000007
    diff_value = input_value_x - input_value_b
    max_diff_value = max(diff_value, 0)
    denom_value = input_value_a - input_value_b
    div_result = max_diff_value // denom_value
    mult_result = div_result * input_value_b
    sum_result = input_value_x + mult_result
    final_result = sum_result % modulus_constant
    print(final_result)

if __name__ == "__main__":
    main()