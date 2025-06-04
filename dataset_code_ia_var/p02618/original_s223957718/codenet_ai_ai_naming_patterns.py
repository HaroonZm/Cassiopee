from random import randint as rand_int, random as rand_float, seed as rand_seed
from math import exp as math_exp
from time import time as time_now
import sys

input_reader = sys.stdin.readline
CONST_INF = 9223372036854775808

def calc_score(day_count, decay_list, satisfaction_matrix, schedule_list):
    score_total = 0
    last_day_contest = [0]*26
    for day_idx, contest_idx in enumerate(schedule_list):
        last_day_contest[contest_idx] = day_idx + 1
        for i in range(26):
            score_total -= (day_idx + 1 - last_day_contest[i]) * decay_list[i]
        score_total += satisfaction_matrix[day_idx][contest_idx]
    return score_total

def update_score(day_count, decay_list, satisfaction_matrix, schedule_list, current_score, change_day_idx, new_contest_idx):
    score_updated = current_score
    last_day_contest = [0]*26
    prev_contest_idx = schedule_list[change_day_idx]
    for day_itr, contest_itr in enumerate(schedule_list, start=1):
        last_day_contest[contest_itr] = day_itr
        score_updated += (day_itr - last_day_contest[prev_contest_idx]) * decay_list[prev_contest_idx]
        score_updated += (day_itr - last_day_contest[new_contest_idx]) * decay_list[new_contest_idx]
    last_day_contest = [0]*26
    for day_itr, contest_itr in enumerate(schedule_list, start=1):
        if day_itr-1 == change_day_idx:
            last_day_contest[new_contest_idx] = day_itr
        else:
            last_day_contest[contest_itr] = day_itr
        score_updated -= (day_itr - last_day_contest[prev_contest_idx]) * decay_list[prev_contest_idx]
        score_updated -= (day_itr - last_day_contest[new_contest_idx]) * decay_list[new_contest_idx]
    score_updated -= satisfaction_matrix[change_day_idx][prev_contest_idx]
    score_updated += satisfaction_matrix[change_day_idx][new_contest_idx]
    return score_updated

def evaluate(day_count, decay_list, satisfaction_matrix, schedule_list, lookahead_days):
    score_eval = 0
    last_day_contest = [0]*26
    for day_idx, contest_idx in enumerate(schedule_list):
        last_day_contest[contest_idx] = day_idx + 1
        for i in range(26):
            score_eval -= (day_idx + 1 - last_day_contest[i]) * decay_list[i]
        score_eval += satisfaction_matrix[day_idx][contest_idx]
    for day_idx in range(len(schedule_list), min(len(schedule_list) + lookahead_days, day_count)):
        for i in range(26):
            score_eval -= (day_idx + 1 - last_day_contest[i]) * decay_list[i]
    return score_eval

def solve_greedy(day_count, decay_list, satisfaction_matrix):
    candidate_schedules = []
    for look_days in range(7, 9):
        temp_schedule = []
        best_local_score = -CONST_INF
        for day_idx in range(day_count):
            best_local_score = -CONST_INF
            best_contest_idx = 0
            for contest_idx in range(26):
                temp_schedule.append(contest_idx)
                score_eval = evaluate(day_count, decay_list, satisfaction_matrix, temp_schedule, look_days)
                if best_local_score < score_eval:
                    best_local_score = score_eval
                    best_contest_idx = contest_idx
                temp_schedule.pop()
            temp_schedule.append(best_contest_idx)
        candidate_schedules.append((best_local_score, temp_schedule))
    return max(candidate_schedules, key=lambda pair: pair[0])

def perform_local_search(day_count, decay_list, satisfaction_matrix, start_score, schedule_list):
    search_start_time = time_now()
    init_temp = 5500
    final_temp = 900
    time_limit = 1.96
    temperature = init_temp
    iter_count = 0
    elapsed_time = 0
    best_score_found = start_score
    best_schedule_found = schedule_list
    while elapsed_time < 1.3:
        if iter_count % 100 == 0:
            elapsed_time = (time_now() - search_start_time)
            if elapsed_time > time_limit:
                break
            normalized_time = elapsed_time / time_limit
            temperature = pow(init_temp, 1-normalized_time) * pow(final_temp, normalized_time)
        select_op = rand_int(1, 2 + iter_count // 10000)
        if select_op == 1:
            swap_day = rand_int(0, day_count - 1)
            swap_contest = rand_int(0, 25)
            temp_score = update_score(day_count, decay_list, satisfaction_matrix, schedule_list, start_score, swap_day, swap_contest)
            if start_score < temp_score or \
                    (temp_score > 4 * 10 ** 6 + iter_count * 10000 and
                        math_exp((start_score - temp_score)/temperature) > 0.5):
                schedule_list[swap_day] = swap_contest
                start_score = temp_score
        else:
            swap_day1 = rand_int(0, day_count - 1)
            swap_day2 = rand_int(0, day_count - 1)
            contest1 = schedule_list[swap_day1]
            contest2 = schedule_list[swap_day2]
            temp_score = update_score(day_count, decay_list, satisfaction_matrix, schedule_list, start_score, swap_day1, contest2)
            temp_score = update_score(day_count, decay_list, satisfaction_matrix, schedule_list, temp_score, swap_day2, contest1)
            if start_score < temp_score or \
                    (temp_score > 4 * 10 ** 6 + iter_count * 10000 and
                        math_exp((start_score - temp_score)/temperature) > 0.5):
                start_score = temp_score
                schedule_list[swap_day1] = contest2
                schedule_list[swap_day2] = contest1
        if best_score_found < start_score:
            best_score_found = start_score
            best_schedule_found = schedule_list
        iter_count += 1
    return best_schedule_found

if __name__ == '__main__':
    rand_seed(1)
    input_D = int(input_reader())
    input_C = [int(val) for val in input_reader().split()]
    input_S = [[int(val) for val in input_reader().split()] for _ in range(input_D)]
    initial_score, initial_schedule = solve_greedy(input_D, input_C, input_S)
    final_schedule = perform_local_search(input_D, input_C, input_S, initial_score, initial_schedule)
    for contest_value in final_schedule:
        print(contest_value + 1)