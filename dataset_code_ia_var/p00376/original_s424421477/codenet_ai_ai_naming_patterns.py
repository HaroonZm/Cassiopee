def read_two_integers():
    return map(int, input().split())

def compute_difference(value_first, value_second):
    if value_first < value_second:
        return value_second - value_first
    else:
        return value_first - value_second

def main():
    input_first, input_second = read_two_integers()
    result_difference = compute_difference(input_first, input_second)
    print(result_difference)

main()