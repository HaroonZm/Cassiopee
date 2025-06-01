def read_N_M():
    return map(int, input().split())

def is_end_condition(N, M):
    return N == 0 and M == 0

def initialize_score():
    return [0]

def read_score_values(N):
    return [int(input()) for _ in range(N)]

def input_score(N):
    score = initialize_score()
    score_values = read_score_values(N)
    score.extend(score_values)
    return score

def create_contain_sum_dict():
    return {}

def calculate_now_score(score, i, j):
    return score[i] + score[j]

def is_now_score_not_in_contain_sum(now_score, contain_sum):
    return not contain_sum.get(now_score)

def add_now_score_to_container(now_score, contain_sum, two_score):
    contain_sum[now_score] = True
    two_score.append(now_score)

def generate_two_score_list(score):
    two_score = []
    contain_sum = create_contain_sum_dict()
    length = len(score)
    for i in range(length):
        for j in range(length):
            now_score = calculate_now_score(score, i, j)
            if is_now_score_not_in_contain_sum(now_score, contain_sum):
                add_now_score_to_container(now_score, contain_sum, two_score)
    return two_score

def sort_two_score(two_score):
    two_score.sort()

def cal_two_sum_score(score):
    two_score = generate_two_score_list(score)
    sort_two_score(two_score)
    return two_score

def initialize_left_pointer():
    return 0

def initialize_right_pointer(two_score):
    return len(two_score) - 1

def initialize_max_score():
    return 0

def sum_two_scores(two_score, left, right):
    return two_score[left] + two_score[right]

def update_max_score_if_smaller(max_score, now_score):
    return max(max_score, now_score)

def increment_left(left):
    return left + 1

def decrement_right(right):
    return right - 1

def is_now_score_less_than_M(now_score, M):
    return now_score < M

def is_now_score_greater_than_M(now_score, M):
    return now_score > M

def is_now_score_equal_to_M(now_score, M):
    return now_score == M

def cal_four_sum_score(two_score, M):
    left = initialize_left_pointer()
    right = initialize_right_pointer(two_score)
    max_score = initialize_max_score()
    while left != right:
        now_score = sum_two_scores(two_score, left, right)
        if is_now_score_less_than_M(now_score, M):
            max_score = update_max_score_if_smaller(max_score, now_score)
            left = increment_left(left)
        elif is_now_score_greater_than_M(now_score, M):
            right = decrement_right(right)
        elif is_now_score_equal_to_M(now_score, M):
            max_score = M
            break
    return max_score

def print_result(max_score):
    print(max_score)

def main():
    while True:
        N, M = read_N_M()
        if is_end_condition(N, M):
            break
        score = input_score(N)
        two_score = cal_two_sum_score(score)
        max_score = cal_four_sum_score(two_score, M)
        print_result(max_score)

if __name__ == "__main__":
    main()