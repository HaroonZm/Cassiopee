def read_input_line():
    try:
        return input()
    except:
        return None

def parse_line(line):
    return line.split()

def word_in_result(word, result):
    return word in result

def add_number_to_result(word, number, result):
    if word_in_result(word, result):
        append_number(word, number, result)
    else:
        init_number_list(word, number, result)

def append_number(word, number, result):
    result[word].append(number)

def init_number_list(word, number, result):
    result[word] = [number]

def sort_result_items(result):
    return sorted(result.items())

def convert_values_to_int_list(v):
    return list(map(int, v))

def sort_int_values(val):
    return sorted(val)

def format_output(k, val):
    return k + '\n' + ' '.join(map(str, val))

def process_inputs():
    result = {}
    while True:
        n = read_input_line()
        if n is None:
            break
        word, number = parse_line(n)
        add_number_to_result(word, number, result)
    return result

def print_result(result):
    sorted_items = sort_result_items(result)
    for k, v in sorted_items:
        val = convert_values_to_int_list(v)
        val_sorted = sort_int_values(val)
        output = format_output(k, val_sorted)
        print(output)

def main():
    result = process_inputs()
    print_result(result)

main()