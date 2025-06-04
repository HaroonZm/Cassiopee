def read_n_ani():
    return int(input())

def read_l_ans():
    return list(input())

def get_next_animal_case(pre_ani, now_ani, ans):
    if pre_ani == "S":
        return get_next_animal_case_S(now_ani, ans)
    else:
        return get_next_animal_case_W(now_ani, ans)

def get_next_animal_case_S(now_ani, ans):
    if now_ani == "S":
        return get_next_animal_S_S(ans)
    else:
        return get_next_animal_S_W(ans)

def get_next_animal_S_S(ans):
    if ans == "o":
        return "S"
    else:
        return "W"

def get_next_animal_S_W(ans):
    if ans == "o":
        return "W"
    else:
        return "S"

def get_next_animal_case_W(now_ani, ans):
    if now_ani == "S":
        return get_next_animal_W_S(ans)
    else:
        return get_next_animal_W_W(ans)

def get_next_animal_W_S(ans):
    if ans == "o":
        return "W"
    else:
        return "S"

def get_next_animal_W_W(ans):
    if ans == "o":
        return "S"
    else:
        return "W"

def get_next_animal(pre_ani, now_ani, ans):
    return get_next_animal_case(pre_ani, now_ani, ans)

def initialize_l_ani(first_ani):
    l_ani = []
    l_ani.append(first_ani)
    return l_ani

def append_second_animal(l_ani, last_ani, first_ani, l_ans):
    next_ani = get_next_animal(last_ani, first_ani, l_ans[0])
    l_ani.append(next_ani)
    return l_ani

def generate_full_ani_list(l_ani, n_ani, l_ans):
    for i in range(1, (n_ani - 1)):
        next_ani = get_next_animal(l_ani[i - 1], l_ani[i], l_ans[i])
        l_ani.append(next_ani)
    return l_ani

def check_valid(l_ani, n_ani, last_ani, l_ans):
    condition1 = (l_ani[(n_ani - 1)] == last_ani)
    next_first = get_next_animal(l_ani[(n_ani - 2)], l_ani[(n_ani - 1)], l_ans[(n_ani - 1)])
    condition2 = (next_first == l_ani[0])
    return condition1 and condition2

def solve_question(first_ani, last_ani, n_ani, l_ans):
    l_ani = initialize_l_ani(first_ani)
    l_ani = append_second_animal(l_ani, last_ani, first_ani, l_ans)
    l_ani = generate_full_ani_list(l_ani, n_ani, l_ans)
    if check_valid(l_ani, n_ani, last_ani, l_ans):
        return "ok", l_ani
    else:
        return "ng", l_ani

def try_one_config(fir_ani, las_ani, n_ani, l_ans):
    result, l_ani = solve_question(fir_ani, las_ani, n_ani, l_ans)
    if result == "ok":
        print(join_animals(l_ani))
        return True
    return False

def join_animals(l_ani):
    return "".join([i for i in l_ani])

def main_loop():
    n_ani = read_n_ani()
    l_ans = read_l_ans()
    configs = [
        ("S", "S"),
        ("S", "W"),
        ("W", "S"),
        ("W", "W"),
    ]
    ng_counter = 0
    for fir_ani, las_ani in configs:
        if try_one_config(fir_ani, las_ani, n_ani, l_ans):
            return
        else:
            ng_counter += 1
    if ng_counter == 4:
        print(-1)

main_loop()