from math import gcd as compute_gcd
def main():
    input_value = int(input())
    lcm_360_input = (360 * input_value) // compute_gcd(360, input_value)
    result = lcm_360_input // input_value
    print(result)
main()