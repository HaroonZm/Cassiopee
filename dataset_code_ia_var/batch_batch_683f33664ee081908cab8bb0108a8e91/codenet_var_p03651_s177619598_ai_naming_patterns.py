from fractions import gcd

def main():
    input_values = list(map(int, open(0).read().split()))
    num_elements = input_values[0]
    target_value = input_values[1]
    values_list = input_values[2:]
    common_gcd = values_list[0]
    for current_value in values_list:
        common_gcd = gcd(common_gcd, current_value)
    is_possible = (target_value <= max(values_list)) and (target_value % common_gcd == 0)
    print(("POSSIBLE" if is_possible else "IMPOSSIBLE"))

main()