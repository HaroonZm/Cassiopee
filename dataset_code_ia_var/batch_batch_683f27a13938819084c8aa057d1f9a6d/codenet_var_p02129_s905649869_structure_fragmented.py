def read_input():
    return int(input())

def read_amida_input():
    return [int(x) for x in input().split()]

def create_initial_set():
    return [0,0,0,0,0,0]

def create_judge_list():
    return [[2,1,3],[1,3,2],[3,2,1],[2,3,1],[3,1,2],[1,2,3]]

def create_initial_id():
    return [1, 2, 3]

def swap_first_second(id_list):
    id_list[0], id_list[1] = id_list[1], id_list[0]

def swap_second_third(id_list):
    id_list[1], id_list[2] = id_list[2], id_list[1]

def apply_amida(amida, id_list):
    for j in range(1, len(amida)):
        if amida[j] == 0:
            swap_first_second(id_list)
        elif amida[j] == 1:
            swap_second_third(id_list)
    return id_list

def match_judge_result(id_list, judge_list, SET):
    for i in range(len(judge_list)):
        if id_list == judge_list[i]:
            increment_set(SET, i)

def increment_set(SET, idx):
    SET[idx] += 1

def process_each_amida(N, SET, judge_list):
    for _ in range(N):
        id_list = create_initial_id()
        amida = read_amida_input()
        final_id = apply_amida(amida, id_list)
        match_judge_result(final_id, judge_list, SET)

def check_condition1(SET):
    return SET[5] > 0

def check_condition2(SET):
    return SET[0] > 1 or SET[1] > 1 or SET[2] > 1

def check_condition3(SET):
    return (SET[0] > 0) and (SET[1] > 0) and (SET[4] > 0)

def check_condition4(SET):
    return (SET[0] > 0) and (SET[2] > 0) and (SET[4] > 0)

def check_condition5(SET):
    return (SET[0] > 0) and (SET[1] > 0) and (SET[3] > 0)

def check_condition6(SET):
    return (SET[0] > 0) and (SET[2] > 0) and (SET[3] > 0)

def check_condition7(SET):
    return (SET[1] > 0) and (SET[2] > 0) and (SET[4] > 0)

def check_condition8(SET):
    return (SET[3] > 0) and (SET[4] > 0)

def check_condition9(SET):
    return SET[3] > 2

def check_condition10(SET):
    return SET[4] > 2

def check_final_conditions(SET):
    if (check_condition1(SET) or
        check_condition2(SET) or
        check_condition3(SET) or
        check_condition4(SET) or
        check_condition4(SET) or
        check_condition5(SET) or
        check_condition6(SET) or
        check_condition7(SET) or
        check_condition8(SET) or
        check_condition9(SET) or
        check_condition10(SET)):
        return "yes"
    else:
        return "no"

def main():
    N = read_input()
    SET = create_initial_set()
    judge_list = create_judge_list()
    process_each_amida(N, SET, judge_list)
    result = check_final_conditions(SET)
    print(result)

main()