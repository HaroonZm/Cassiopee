def get_readline():
    return open(0).readline

def get_writelines():
    return open(1, 'w').writelines

def create_set():
    return set()

def add_to_set(s, x):
    s.add(x)

def get_set_length(s):
    return len(s)

def is_in_set(s, x):
    return x in s

def output_set_length(s):
    return "%d\n" % get_set_length(s)

def output_in_set(s, x):
    return "%d\n" % is_in_set(s, x)

def process_insert_func():
    return lambda s, x: (add_to_set(s, x), output_set_length(s))[1]

def process_find_func():
    return lambda s, x: output_in_set(s, x)

def get_command_list():
    return [process_insert_func(), process_find_func()]

def parse_int_line(line):
    return int(line)

def parse_two_ints_line(line):
    return map(int, line.split())

def process_query(C, s, t, x):
    return C[t](s, x)

def main():
    readline = get_readline()
    writelines = get_writelines()
    s = create_set()
    C = get_command_list()
    Q = parse_int_line(readline())
    ans = []
    def process_single_query():
        t, x = parse_two_ints_line(readline())
        return process_query(C, s, t, x)
    for _ in range(Q):
        ans.append(process_single_query())
    writelines(ans)

main()