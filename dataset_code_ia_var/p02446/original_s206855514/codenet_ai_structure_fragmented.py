def get_input():
    return input()

def parse_int(s):
    return int(s)

def parse_int_list(s):
    return [int(x) for x in s.split()]

def check_length(n, li):
    assert n == len(li)

def format_output(l):
    return " ".join([str(x) for x in l])

def should_add(i, li):
    if i == 0:
        return True
    return li[i] > li[i-1]

def get_unique_indices(li):
    return [i for i in range(len(li)) if should_add(i, li)]

def unique_elements_from_indices(li, indices):
    return [li[i] for i in indices]

def unique(li):
    indices = get_unique_indices(li)
    return unique_elements_from_indices(li, indices)

def print_result(res):
    print(res)

def process():
    n_str = get_input()
    n = parse_int(n_str)
    li_str = get_input()
    li = parse_int_list(li_str)
    check_length(n, li)
    uniq = unique(li)
    out = format_output(uniq)
    print_result(out)

def run():
    process()

if __name__ == '__main__':
    run()