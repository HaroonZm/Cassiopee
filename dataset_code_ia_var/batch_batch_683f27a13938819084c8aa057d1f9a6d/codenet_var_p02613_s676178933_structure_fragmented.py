def read_input():
    return input()

def parse_N():
    return int(read_input())

def initialize_counter():
    return {"AC":0, "WA":0, "TLE":0, "RE":0}

def get_status_from_input():
    return read_input()

def increment_counter(cnt, status):
    cnt[status] += 1

def process_one_input(cnt):
    status = get_status_from_input()
    increment_counter(cnt, status)

def process_all_inputs(N, cnt):
    for _ in range(N):
        process_one_input(cnt)

def format_output(label, value):
    return label + " x " + str(value)

def print_result(cnt):
    print(format_output("AC", cnt["AC"]))
    print(format_output("WA", cnt["WA"]))
    print(format_output("TLE", cnt["TLE"]))
    print(format_output("RE", cnt["RE"]))

def main():
    N = parse_N()
    cnt = initialize_counter()
    process_all_inputs(N, cnt)
    print_result(cnt)

main()