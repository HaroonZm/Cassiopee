import io
import sys
import math

def get_input_n():
    return int(input())

def get_input_a_list():
    return list(map(int, input().split()))

def add_x_to_y():
    # Placeholder for future operation
    pass

def check_sorted_pair(a_lst, idx):
    return a_lst[idx] <= a_lst[idx + 1]

def is_condition_ok(lst):
    return all(check_sorted_pair(lst, i) for i in range(len(lst) - 1))

def flag_positive(a):
    return a >= 0

def flag_negative(a):
    return a < 0

def accumulate_sign_flags(a_lst):
    p_flag = False
    m_flag = False
    for a in a_lst:
        if flag_positive(a):
            p_flag = True
        else:
            m_flag = True
        if p_flag and m_flag:
            return 0
    return 1 if p_flag else -1

def check_plus_minus(lst):
    return accumulate_sign_flags(lst)

def list_to_formatted_answer(lst):
    ans = f"{len(lst)}\n"
    for y in lst:
        ans += f"{y[0]} {y[1]}\n"
    return ans

def get_first_nondecreasing_index(a_lst):
    for i in range(len(a_lst) - 1):
        if a_lst[i] > a_lst[i + 1]:
            return i + 1
    return -1

def get_max_index_and_value(a_lst):
    a_max = a_lst[0]
    x = 0
    for i in range(1, len(a_lst)):
        if a_max < a_lst[i]:
            a_max = a_lst[i]
            x = i
    return x, a_max

def get_left_to_right_moves(y, n):
    return [[i + 1, i + 2] for i in range(y, n - 1)]

def get_last_decreasing_index(a_lst):
    for i in range(len(a_lst) - 1, 0, -1):
        if a_lst[i] < a_lst[i - 1]:
            return i - 1
    return -1

def get_min_index_and_value(a_lst):
    a_min = a_lst[0]
    x = 0
    for i in range(1, len(a_lst)):
        if a_min > a_lst[i]:
            a_min = a_lst[i]
            x = i
    return x, a_min

def get_right_to_left_moves(y):
    return [[i + 1, i] for i in range(y, 0, -1)]

def find_max_and_min_indices_and_values(a_lst):
    i_max, a_max = 0, a_lst[0]
    i_min, a_min = 0, a_lst[0]
    for i in range(1, len(a_lst)):
        if a_max < a_lst[i]:
            a_max = a_lst[i]
            i_max = i
        if a_min > a_lst[i]:
            a_min = a_lst[i]
            i_min = i
    return i_max, a_max, i_min, a_min

def make_all_positive(a_lst, i_max, a_max, ans_lst):
    for i in range(len(a_lst)):
        if a_lst[i] < 0:
            a_lst[i] += a_max
            ans_lst.append([i_max + 1, i + 1])

def make_all_negative(a_lst, i_min, a_min, ans_lst):
    for i in range(len(a_lst)):
        if a_lst[i] >= 0:
            a_lst[i] += a_min
            ans_lst.append([i_min + 1, i + 1])

def handle_all_positive_case(a_lst, ans_lst):
    y = get_first_nondecreasing_index(a_lst)
    x, a_max = get_max_index_and_value(a_lst)
    if y != -1:
        ans_lst.append([x + 1, y + 1])
        ans_lst += get_left_to_right_moves(y, len(a_lst))

def handle_all_negative_case(a_lst, ans_lst):
    y = get_last_decreasing_index(a_lst)
    x, a_min = get_min_index_and_value(a_lst)
    if y != -1:
        ans_lst.append([x + 1, y + 1])
        ans_lst += get_right_to_left_moves(y)

def handle_mixed_sign_case(a_lst, ans_lst):
    i_max, a_max, i_min, a_min = find_max_and_min_indices_and_values(a_lst)
    if a_max > abs(a_min):
        make_all_positive(a_lst, i_max, a_max, ans_lst)
        y = get_first_nondecreasing_index(a_lst)
        if y != -1:
            ans_lst.append([i_max + 1, y + 1])
            ans_lst += get_left_to_right_moves(y, len(a_lst))
    else:
        make_all_negative(a_lst, i_min, a_min, ans_lst)
        y = get_last_decreasing_index(a_lst)
        if y != -1:
            ans_lst.append([i_min + 1, y + 1])
            ans_lst += get_right_to_left_moves(y)

def prepare_answer(ans_lst):
    return list_to_formatted_answer(ans_lst)

def solve(n, a_lst):
    if is_condition_ok(a_lst):
        return 0
    plus_minus = check_plus_minus(a_lst)
    ans_lst = []
    if plus_minus == 1:
        handle_all_positive_case(a_lst, ans_lst)
    elif plus_minus == -1:
        handle_all_negative_case(a_lst, ans_lst)
    else:
        handle_mixed_sign_case(a_lst, ans_lst)
    return prepare_answer(ans_lst)

def main():
    n = get_input_n()
    a_lst = get_input_a_list()
    if _DEB: logd(f"a_lst: {a_lst}")
    ans = str(solve(n, a_lst)).strip()
    print(ans)
    return ans

### DEBUG I/O ###
_DEB = 0   # 1:ON / 0:OFF

_INPUT = """\
2
-1 -3
"""
_EXPECTED = """\
2
2 3
3 3
"""

def logd(str):
    if _DEB: print(f"[deb] {str}")

### MAIN ###
if __name__ == "__main__":
    if _DEB:
        sys.stdin = io.StringIO(_INPUT)
        print("!! Debug Mode !!")

    ans = main()

    if _DEB:
        print()
        if _EXPECTED.strip() == ans.strip(): print("!! Success !!")
        else: print(f"!! Failed... !!\nANSWER:   {ans}\nExpected: {_EXPECTED}")