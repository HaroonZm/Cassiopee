def read_input():
    return raw_input()

def parse_input(input_line):
    return map(int, input_line.split())

def get_number_of_entries(parsed_line):
    return parsed_line[0]

def get_time_from_entry(parsed_line, index):
    hour = parsed_line[2*index + 1]
    minute = parsed_line[2*index + 2]
    return hour * 60 + minute

def add_times_to_set(times_set, parsed_line):
    n = get_number_of_entries(parsed_line)
    for i in xrange(n):
        time = get_time_from_entry(parsed_line, i)
        times_set.add(time)

def convert_time_to_string(time):
    hour_str = str(time / 60)
    minute_str = str(time % 60).zfill(2)
    return ":".join([hour_str, minute_str])

def main():
    times = set()
    first_input = read_input()
    parsed_first = parse_input(first_input)
    add_times_to_set(times, parsed_first)
    second_input = read_input()
    parsed_second = parse_input(second_input)
    add_times_to_set(times, parsed_second)
    times_list = list(times)
    times_list.sort()
    formatted_times = [convert_time_to_string(t) for t in times_list]
    print " ".join(formatted_times)

main()