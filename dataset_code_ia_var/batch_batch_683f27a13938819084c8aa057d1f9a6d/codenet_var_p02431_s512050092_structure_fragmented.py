def get_list():
    return list()

def read_input():
    return input()

def to_int(s):
    return int(s)

def get_length(lists):
    return len(lists)

def insert_at(lists, index, value):
    return lists.insert(index, value)

def push_back(lists, x):
    index = get_length(lists)
    return insert_at(lists, index, x)

def split_input(s):
    return s.split()

def get_item(lst, idx):
    return lst[idx]

def random_access(lists, p):
    value = get_item(lists, p)
    print_value(value)

def print_value(value):
    print(value)

def get_last_index(lists):
    return get_length(lists) - 1

def pop_back(lists):
    index = get_last_index(lists)
    return pop_at(lists, index)

def pop_at(lists, index):
    return lists.pop(index)

def decide_action(j, l):
    if to_int(j[0]) == 0:
        push_back(l, to_int(j[1]))
    elif to_int(j[0]) == 1:
        random_access(l, to_int(j[1]))
    else:
        pop_back(l)

def loop_actions(n, l):
    for i in range(n):
        raw_input = read_input()
        j = split_input(raw_input)
        decide_action(j, l)

def main():
    l = get_list()
    n = to_int(read_input())
    loop_actions(n, l)

if __name__ == '__main__':
    main()