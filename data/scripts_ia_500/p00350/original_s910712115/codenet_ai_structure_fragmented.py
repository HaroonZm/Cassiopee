def read_int():
    return int(raw_input())

def read_str():
    return raw_input()

def read_cmd():
    return raw_input().split()

def get_cmd_name(cmd_list):
    return cmd_list[0]

def pop_cmd_name(cmd_list):
    return cmd_list.pop(0)

def parse_set_params(params):
    x = int(params[0])
    y = int(params[1])
    z = params[2]
    return x, y, z

def parse_comp_params(params):
    a = int(params[0])
    b = int(params[1])
    c = int(params[2])
    d = int(params[3])
    return a, b, c, d

def get_prefix(u, x):
    return u[:x-1]

def get_suffix(u, y):
    return u[y:]

def create_replacement(z, length):
    return z * length

def assemble_set_string(prefix, replacement, suffix):
    return prefix + replacement + suffix

def execute_cmd_set(params, u):
    x, y, z = parse_set_params(params)
    prefix = get_prefix(u, x)
    suffix = get_suffix(u, y)
    replacement = create_replacement(z, y - x + 1)
    return assemble_set_string(prefix, replacement, suffix)

def extract_substring(u, start, end):
    return u[start-1:end]

def compare_substrings(s, t):
    if s < t:
        print "s"
    elif s > t:
        print "t"
    else:
        print "e"

def execute_cmd_comp(params, u):
    a, b, c, d = parse_comp_params(params)
    s = extract_substring(u, a, b)
    t = extract_substring(u, c, d)
    compare_substrings(s, t)

def main():
    n = read_int()
    u = read_str()
    q = read_int()
    for _ in range(q):
        cmd_list = read_cmd()
        cmd = get_cmd_name(cmd_list)
        pop_cmd_name(cmd_list)
        if cmd == 'comp':
            execute_cmd_comp(cmd_list, u)
        elif cmd == 'set':
            u = execute_cmd_set(cmd_list, u)

main()