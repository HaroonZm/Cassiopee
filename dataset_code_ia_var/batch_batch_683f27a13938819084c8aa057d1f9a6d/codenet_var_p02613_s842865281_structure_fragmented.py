def get_initial_list():
    return [0] * 4

def read_number_of_inputs():
    return int(input())

def read_result():
    return input()

def update_ac(counter_list, result):
    if result == "AC":
        counter_list[0] += 1

def update_wa(counter_list, result):
    if result == "WA":
        counter_list[1] += 1

def update_tle(counter_list, result):
    if result == "TLE":
        counter_list[2] += 1

def update_re(counter_list, result):
    if result == "RE":
        counter_list[3] += 1

def process_result(counter_list, result):
    update_ac(counter_list, result)
    update_wa(counter_list, result)
    update_tle(counter_list, result)
    update_re(counter_list, result)

def get_formatted_output(counter_list):
    return "AC x {0}\nWA x {1}\nTLE x {2}\nRE x {3}".format(
        counter_list[0], counter_list[1], counter_list[2], counter_list[3])

def print_output(formatted_output):
    print(formatted_output)

def main():
    li = get_initial_list()
    N = read_number_of_inputs()
    for _ in range(N):
        result = read_result()
        process_result(li, result)
    output = get_formatted_output(li)
    print_output(output)

main()