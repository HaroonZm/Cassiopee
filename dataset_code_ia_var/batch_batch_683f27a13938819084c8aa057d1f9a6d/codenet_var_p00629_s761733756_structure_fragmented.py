def main_loop():
    while True:
        in_tmp = read_input()
        if check_exit(in_tmp):
            break
        list_team = build_team_list(in_tmp)
        list_sorted = sort_teams(list_team)
        process_sorted_teams(list_sorted)

def read_input():
    return input()

def check_exit(in_tmp):
    return in_tmp == "0"

def build_team_list(team_count_input):
    team_count = to_int(team_count_input)
    return read_team_inputs(team_count)

def to_int(val):
    return int(val)

def read_team_inputs(team_count):
    res = []
    for _ in range(team_count):
        team_data = parse_team_input(input())
        res.append(team_data)
    return res

def parse_team_input(line):
    return list(map(int, line.split()))

def sort_teams(team_list):
    return sorted(team_list, key=custom_sort_key)

def custom_sort_key(x):
    return (-x[2], x[3], x[0])

def process_sorted_teams(list_sorted):
    cnt_passed = 0
    dict_passed = {}
    for item in list_sorted:
        if not contains_key(dict_passed, item[1]):
            init_dict_key(dict_passed, item[1])
        if can_pass(cnt_passed, dict_passed[item[1]]):
            print_item_id(item)
            increment_dict(dict_passed, item[1])
            cnt_passed = increment(cnt_passed)
        elif can_pass_2(cnt_passed, dict_passed[item[1]]):
            print_item_id(item)
            increment_dict(dict_passed, item[1])
            cnt_passed = increment(cnt_passed)
        elif can_pass_3(cnt_passed, dict_passed[item[1]]):
            print_item_id(item)
            increment_dict(dict_passed, item[1])
            cnt_passed = increment(cnt_passed)
        else:
            if cnt_passed >= 26:
                break

def contains_key(dictionary, key):
    return key in dictionary.keys()

def init_dict_key(dictionary, key):
    dictionary[key] = 0

def can_pass(cnt_passed, passed_value):
    return (cnt_passed < 10) and (passed_value < 3)

def can_pass_2(cnt_passed, passed_value):
    return (10 <= cnt_passed < 20) and (passed_value < 2)

def can_pass_3(cnt_passed, passed_value):
    return (20 <= cnt_passed < 26) and (passed_value < 1)

def print_item_id(item):
    print(item[0])

def increment(value):
    return value + 1

def increment_dict(dictionary, key):
    dictionary[key] += 1

main_loop()