def get_input_numbers():
    return tuple(int(n) for n in input().split(' '))

def read_data_entry():
    temp = input().split(' ')
    key = temp[0]
    start = int(temp[1])
    end = int(temp[2])
    length = end - start + 1
    return key, [length, end]

def build_data_dict(inputnum):
    data = {}
    for _ in range(inputnum):
        key, val = read_data_entry()
        data[key] = val
    return data

def read_target():
    return int(input())

def process_target(targ, data):
    for k, v in data.items():
        if v[0] <= targ <= v[1]:
            result = k + ' ' + str(targ - v[0] + 1)
            print_result(result)
            return
    print_result("Unknown")

def process_outputs(outputnum, data):
    for _ in range(outputnum):
        targ = read_target()
        process_target(targ, data)

def print_result(result):
    print(result)

def is_end(inputnum, outputnum):
    return inputnum == 0 and outputnum == 0

def main_loop():
    inputnum, outputnum = get_input_numbers()
    while not is_end(inputnum, outputnum):
        data = build_data_dict(inputnum)
        process_outputs(outputnum, data)
        inputnum, outputnum = get_input_numbers()

def main():
    main_loop()

main()