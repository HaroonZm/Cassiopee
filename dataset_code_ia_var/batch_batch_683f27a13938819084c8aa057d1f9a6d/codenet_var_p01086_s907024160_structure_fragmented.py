ans_list = []

def read_n():
    return int(input())

def read_line():
    return input()

def read_lines(n):
    lines = []
    for _ in range(n):
        lines.append(read_line())
    return lines

def increment(cnt, value):
    return cnt + value

def increment_index(i):
    return i + 1

def make_tanka(num, w_list, i):
    cnt = 0
    while cnt < num:
        cnt = increment(cnt, len(w_list[i]))
        i = increment_index(i)
    return [cnt, i]

def get_first_index(w_list):
    f1 = s1 = f2 = s2 = s3 = 0
    i = 0
    ans = -1
    length = len(w_list)
    while True:
        j = i
        res1 = get_first_make_tanka(j, w_list)
        f1, j = res1[0], res1[1]
        if is_valid(f1, 5):
            res2 = get_second_make_tanka(j, w_list)
            s1, j = res2[0], res2[1]
            if is_valid(s1, 7):
                res3 = get_third_make_tanka(j, w_list)
                f2, j = res3[0], res3[1]
                if is_valid(f2, 5):
                    res4 = get_fourth_make_tanka(j, w_list)
                    s2, j = res4[0], res4[1]
                    if is_valid(s2, 7):
                        res5 = get_fifth_make_tanka(j, w_list)
                        s3, j = res5[0], res5[1]
                        if is_valid(s3, 7):
                            ans = i
                            break
                    if found_answer(ans):
                        break
                if found_answer(ans):
                    break
            if found_answer(ans):
                break
        if found_answer(ans):
            break
        i = next_index(i)
    return ans

def get_first_make_tanka(j, w_list):
    return make_tanka(5, w_list, j)

def get_second_make_tanka(j, w_list):
    return make_tanka(7, w_list, j)

def get_third_make_tanka(j, w_list):
    return make_tanka(5, w_list, j)

def get_fourth_make_tanka(j, w_list):
    return make_tanka(7, w_list, j)

def get_fifth_make_tanka(j, w_list):
    return make_tanka(7, w_list, j)

def is_valid(val, expected):
    return val == expected

def found_answer(ans):
    return ans != -1

def next_index(i):
    return i + 1

def add_offset(ans):
    return ans + 1

def main_loop():
    while True:
        n = read_n()
        if is_zero(n):
            break
        w_list = read_lines(n)
        ans = get_first_index(w_list)
        ans_list.append(add_offset(ans))

def is_zero(n):
    return n == 0

def print_answers(ans_list):
    for v in ans_list:
        print(v)

main_loop()
print_answers(ans_list)