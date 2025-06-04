def read_n():
    return input()

def is_zero(n):
    return n == 0

def prepare_ans():
    return {}

def get_group_and_name():
    group_name = raw_input().split(":")
    return group_name

def get_group(group_name):
    return group_name[0]

def get_names(group_name):
    names = group_name[1]
    return names[:-1].split(",")

def is_first(i):
    return i == 0

def set_first(group):
    return group

def add_to_ans(ans, group, names):
    ans[group] = set(names)

def get_all_keys(ans):
    return list(ans)

def should_continue(flag):
    return flag

def process_groups(ans, first):
    while True:
        for key in get_all_keys(ans):
            flag = 0
            if key == first:
                continue
            keys1 = get_all_keys(ans)
            for key1 in keys1:
                if key in ans[key1]:
                    ans[key1] |= ans[key]
                    ans[key1].discard(key)
                    flag = 1
        if not should_continue(flag):
            break

def print_first_ans_length(ans, first):
    print len(ans[first])

def main_loop():
    while True:
        n = read_n()
        if is_zero(n):
            break
        ans = prepare_ans()
        first = None
        for i in range(n):
            group_name = get_group_and_name()
            group = get_group(group_name)
            names = get_names(group_name)
            if is_first(i):
                first = set_first(group)
            add_to_ans(ans, group, names)
        process_groups(ans, first)
        print_first_ans_length(ans, first)

main_loop()